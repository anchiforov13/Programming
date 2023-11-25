from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status
from .models import Jewelry
from .serializers import JewelrySerializer
from django.db.models import Q
from django.core.exceptions import FieldError


# Create your views here.

DATABASE_FILE = 'jewelry_collection.txt'

class JewelryListCreateView(generics.ListCreateAPIView):
    queryset = Jewelry.objects.all()
    serializer_class = JewelrySerializer

    def get(self, request, *args, **kwargs):
        sort_param = self.request.query_params.get('sort', None)
        sort_type = self.request.query_params.get('sort_type', 'asc')
        if sort_param:
            try:
                result = Jewelry.objects.all().order_by(f'{"" if sort_type == "asc" else "-"}{sort_param}')
                serializers = JewelrySerializer(result, many=True)
                return Response({'status': 'success', 'jewelry': serializers.data}, status=200)
            except FieldError:
                return Response({'status': 'error', 'message': 'Invalid sort parameter'}, status=400)
            
        search_query = self.request.query_params.get('search', None)

        if search_query:
            result = Jewelry.objects.filter(
                Q(ID__icontains=search_query) |
                Q(title__icontains=search_query) |
                Q(code__icontains=search_query) |
                Q(material__icontains=search_query) |
                Q(jewelry_type__icontains=search_query) |
                Q(date_of_creation__icontains=search_query) |
                Q(price__icontains=search_query)
            )
        else:
            result = Jewelry.objects.all()

        offset = int(self.request.query_params.get('offset', 0))
        limit = int(self.request.query_params.get('limit', result.count()))
        result = result[offset:offset + limit]

        serializer = JewelrySerializer(result, many=True)
        return Response({'status': 'success', 'jewelry': serializer.data, 'count': Jewelry.objects.count()}, status=200)

    def post(self, request):  
        serializer = JewelrySerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            with open(DATABASE_FILE, 'a') as file:
                file.write(','.join(map(str, serializer.data.values())) + '\n')
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class JewelryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Jewelry.objects.all()
    serializer_class = JewelrySerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({'status': 'success', "jewelry": serializer.data}, status=200)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'status': 'success', 'message': 'Jewelry deleted successfully'}, status=204)

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        try:
            instance = Jewelry.objects.get(ID=instance.ID)
        except Jewelry.DoesNotExist:
            return Response({'status': 'error', 'message': 'Jewelry with the given ID does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = JewelrySerializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)