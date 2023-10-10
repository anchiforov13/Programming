import re
from datetime import datetime
from int_validation import positive_float_validity, positive_int_validity

def validate_id(func):
    def wrapper(id):
        if positive_int_validity(id):
            return func(id)
        else:
            print("The ID should be a positive integer")
            return False
    return wrapper

def validate_name(func):
    def wrapper(name):
        pattern = "^[a-zA-Z]+$"
        if re.match(pattern, name.strip()):
            return func(name)
        else:
            print("The name should only contain letters of the alphabet")
            return False
    return wrapper

def validate_code(func):
    def wrapper(code):
        pattern = r"^\w{5}/\w-\w{2}$"
        if re.match(pattern, code):
            return func(code)
        else:
            print("Error. The code should be in the correct format")
            return False
    return wrapper

def validate_material(func):
    def wrapper(material):
        if not material in ["gold", "silver", "platinum"]:
            print("Invalid material option")
            return False
        else:
            return func(material)
    return wrapper

def validate_type(func):
    def wrapper(jewelry_type):
        if not jewelry_type in ["rings", "earrings", "bracelets"]:
            print("Invalid type of jewelry")
            return False
        else:
            return func(jewelry_type)
    return wrapper

def validate_price(func):
    def wrapper(price):
        pattern = r"^\d+\.\d{2}$"
        if positive_float_validity(price) and re.match(pattern, price):
            return func(price)
        else:
            return False
    return wrapper

def validate_date(func):
    def wrapper(date_str):
        try:
            date_format = "%Y-%m-%d"  
            date = datetime.strptime(date_str, date_format)
            today = datetime.today()

            if date > today:
                print("The date can't be in the future. Try again.")
                return False
            
            yy, mm, dd = date_str.split('-')
            yy, mm, dd = int(yy), int(mm), int(dd)
            if(mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
                max_days=31
            elif(mm==4 or mm==6 or mm==9 or mm==11):
                max_days=30
            elif(yy%4==0 and yy%100!=0 or yy%400==0):
                max_days=29
            else:
                max_days=28

            if not 1 <= mm <= 12 or not 1 <= dd <= max_days:
                print("Invalid date.")
                return False

            return func(date_str)
        except ValueError:
            print("Please enter the date in the correct format.")
            return False
    return wrapper

class Validator:
    @staticmethod
    @validate_id
    def is_valid_id(id):
        return True

    @staticmethod
    @validate_name
    def is_valid_name(name):
        return True

    @staticmethod
    @validate_code
    def is_valid_code(code):
        return True

    @staticmethod
    @validate_material
    def is_valid_material(material):
        return True

    @staticmethod
    @validate_type
    def is_valid_type(jewelry_type):
       return True

    @staticmethod
    @validate_price
    def is_valid_price(price):
        return True
    
    @staticmethod
    @validate_date
    def is_valid_date(date_str):
        return True