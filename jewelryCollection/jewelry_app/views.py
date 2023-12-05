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
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# Create your views here.

response_example_200 = {
    'status': 'success',
    'jewelry': [{'ID': 1, 'title': 'Example Jewelry', 'code': '123', 'material': 'Gold', 'jewelry_type': 'Ring',
                 'date_of_creation': '2023-01-01', 'price': 500.0}]
}

response_example_204 = {'status': 'success', 'message': 'Jewelry deleted successfully'}

response_example_400 = {'status': 'error', 'message': 'Invalid input'}

response_example_404 = {'detail': 'Not found'}


class JewelryListCreateView(generics.ListCreateAPIView):

    queryset = Jewelry.objects.all()
    serializer_class = JewelrySerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('sort', openapi.IN_QUERY, description="Parameter to sort by", type=openapi.TYPE_STRING),
            openapi.Parameter('sort_type', openapi.IN_QUERY, description="Sort type ('asc' or 'desc')", type=openapi.TYPE_STRING),
            openapi.Parameter('search', openapi.IN_QUERY, description="Search query", type=openapi.TYPE_STRING),
            openapi.Parameter('offset', openapi.IN_QUERY, description="Offset", type=openapi.TYPE_INTEGER),
            openapi.Parameter('limit', openapi.IN_QUERY, description="Limit", type=openapi.TYPE_INTEGER),
        ],
        responses={
            200: openapi.Response('Success', schema=openapi.Schema(type=openapi.TYPE_OBJECT), examples={'application/json': response_example_200}),
            400: openapi.Response('Invalid sort parameter', schema=openapi.Schema(type=openapi.TYPE_OBJECT), examples={'application/json': response_example_400}),
        },
    )
    def get(self, request, *args, **kwargs):
        sort_param = self.request.query_params.get('sort', None)
        sort_type = self.request.query_params.get('sort_type', 'asc')
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

        if sort_param:
            try:
                result = result.order_by(f'{"" if sort_type == "asc" else "-"}{sort_param}')
                serializers = JewelrySerializer(result, many=True)
            except FieldError:
                return Response({'status': 'error', 'message': 'Invalid sort parameter'}, status=400)

        offset = int(self.request.query_params.get('offset', 0))
        limit = int(self.request.query_params.get('limit', result.count()))
        if limit != result.count():
            result = result[offset*limit:offset*limit + limit]
        else:
            result = result[offset:]

        serializer = JewelrySerializer(result, many=True)
        return Response({'status': 'success', 'jewelry': serializer.data, 'count': Jewelry.objects.count()}, status=200)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'ID': openapi.Schema(type=openapi.TYPE_INTEGER),
                'title': openapi.Schema(type=openapi.TYPE_STRING),
                'code': openapi.Schema(type=openapi.TYPE_STRING),
                'material': openapi.Schema(type=openapi.TYPE_STRING),
                'jewelry_type': openapi.Schema(type=openapi.TYPE_STRING),
                'date_of_creation': openapi.Schema(type=openapi.TYPE_STRING, format='date'),
                'price': openapi.Schema(type=openapi.TYPE_NUMBER),
            },
            required=['title', 'code', 'material', 'jewelry_type', 'date_of_creation', 'price'],
        ),
        responses={
            200: openapi.Response('Success', schema=openapi.Schema(type=openapi.TYPE_OBJECT), examples={'application/json': response_example_200}),
            400: openapi.Response('Bad Request', schema=openapi.Schema(type=openapi.TYPE_OBJECT), examples={'application/json': response_example_400}),
        },
    )
    def post(self, request):  
        serializer = JewelrySerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class JewelryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Jewelry.objects.all()
    serializer_class = JewelrySerializer

    @swagger_auto_schema(
        responses={
            200: openapi.Response('Success', schema=openapi.Schema(type=openapi.TYPE_OBJECT), examples={'application/json': response_example_200}),
            404: openapi.Response('Not Found', schema=openapi.Schema(type=openapi.TYPE_OBJECT), examples={'application/json': response_example_404}),
        },
    )
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({'status': 'success', "jewelry": serializer.data}, status=200)

    @swagger_auto_schema(
        responses={
            204: openapi.Response('Jewelry deleted successfully', schema=openapi.Schema(type=openapi.TYPE_OBJECT), examples={'application/json': response_example_204}),
            404: openapi.Response('Not Found', schema=openapi.Schema(type=openapi.TYPE_OBJECT), examples={'application/json': response_example_404}),
        },
    )
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'status': 'success', 'message': 'Jewelry deleted successfully'}, status=204)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'title': openapi.Schema(type=openapi.TYPE_STRING),
                'code': openapi.Schema(type=openapi.TYPE_STRING),
                'material': openapi.Schema(type=openapi.TYPE_STRING),
                'jewelry_type': openapi.Schema(type=openapi.TYPE_STRING),
                'date_of_creation': openapi.Schema(type=openapi.TYPE_STRING, format='date'),
                'price': openapi.Schema(type=openapi.TYPE_NUMBER),
            },
            required=['title', 'code', 'material', 'jewelry_type', 'date_of_creation', 'price'],
        ),
        responses={
            200: openapi.Response('Success', schema=openapi.Schema(type=openapi.TYPE_OBJECT), examples={'application/json': response_example_200}),
            400: openapi.Response('Bad Request', schema=openapi.Schema(type=openapi.TYPE_OBJECT), examples={'application/json': response_example_400}),
            404: openapi.Response('Jewelry with the given ID does not exist', schema=openapi.Schema(type=openapi.TYPE_OBJECT), examples={'application/json': response_example_404}),
        },
    )
    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            instance = Jewelry.objects.get(ID=instance.ID)
        except Jewelry.DoesNotExist:
            return Response({'status': 'error', 'message': 'Jewelry with the given ID does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer_data = {k: v[0] for k, v in dict(request.data).items()}
        serializer_data['ID'] = instance.ID
        serializer = JewelrySerializer(instance, data=serializer_data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)