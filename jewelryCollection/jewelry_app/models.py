from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from datetime import date

# Create your models here.
class Jewelry(models.Model):
    ID_validator = [MinValueValidator(1, message="ID should be a positive integer.")]
    title_validator = [RegexValidator(r"^[a-zA-Z\s]+$", message="The name should only contain letters of the alphabet.")]
    code_validator = [RegexValidator(r"^\w{5}/\w-\w{2}$", message="Error. The code should be in the correct format.")]
    material_validator = [RegexValidator(r"^(gold|silver|platinum)$", message="Invalid material option.")]
    jewelry_type_validator = [RegexValidator(r"^(rings|earrings|bracelets)$", message="Invalid type of jewelry.")]
    date_of_creation_validator = [MaxValueValidator(date.today(), message="The date can't be in the future.")]
    price_validator = [RegexValidator(r"^\d+\.\d[0-9]?$", message="Please enter a valid price.")]

    ID = models.PositiveIntegerField(primary_key=True, validators=ID_validator)
    title = models.CharField(max_length=255, validators=title_validator)
    code = models.CharField(max_length=10, validators=code_validator)
    material = models.CharField(max_length=20, validators=material_validator)
    jewelry_type = models.CharField(max_length=20, validators=jewelry_type_validator)
    date_of_creation = models.DateField(validators=date_of_creation_validator)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=price_validator)

    def __str__(self):
        return f"{self.title} ({self.ID})"