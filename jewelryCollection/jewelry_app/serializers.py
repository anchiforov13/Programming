from rest_framework import serializers
from .models import Jewelry

class JewelrySerializer(serializers.ModelSerializer):

    """
    Serializer for the Jewelry model.

    Attributes:
    - `ID` (int): The unique identifier of the Jewelry item.
    - `title` (str): The title of the Jewelry item.
    - `code` (str): The code of the Jewelry item.
    - `material` (str): The material of the Jewelry item.
    - `jewelry_type` (str): The type of the Jewelry item.
    - `date_of_creation` (str): The date of creation of the Jewelry item (YYYY-MM-DD).
    - `price` (float): The price of the Jewelry item.

    Meta:
    - `model` (class): The model class associated with the serializer.
    - `fields` (tuple): The fields to include in the serialized output.

    Example Usage:
    ```python
    # Creating a new Jewelry item
    data = {
        'ID': 1,
        'title': 'Ruby Bracelet',
        'code': '41789/5-45',
        'material': 'Platinum',
        'jewelry_type': 'Bracelets',
        'date_of_creation': '2023-03-20',
        'price': 1250.75
    }
    serializer = JewelrySerializer(data=data)
    if serializer.is_valid():
        jewelry_item = serializer.save()
    ```

    Note:
    - This serializer is designed to work with the Jewelry model.
    - The `Meta` class provides information about the model and fields.
    - The `example_usage` section demonstrates how to use the serializer for creating a new Jewelry item.

    """
    
    class Meta:
        model = Jewelry
        fields = '__all__'