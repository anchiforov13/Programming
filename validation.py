import re
from datetime import datetime
from int_validation import int_validity, positive_int_validity, float_validity, positive_float_validity

class Validator:
    @staticmethod
    def is_valid_age(age):
        if positive_int_validity(age):
            if 0 <= int(age) <= 100:
                return True
            else:
                print("Make sure that the age is in the range [0; 100]")
                return False
        else:
            return False

    @staticmethod
    def is_valid_name(name):
        if not bool(re.match("^[a-zA-Z\s]+$", name)):
            print("The name should only contain letters of the alphabet")
            return False
        else:
            return True

    @staticmethod
    def is_valid_code(code):
        if not bool(re.match("^[0-9*/*-**]+$", code)):
            print("Error. The code should be in the correct format")
            return False
        else:
            return True

    @staticmethod
    def is_valid_material(material):
        if not material in ["gold", "silver", "platinum"]:
            print("Invalid material option")
            return False
        else:
            return True

    @staticmethod
    def is_valid_type(jewelry_type):
       if not jewelry_type in ["rings", "earrings", "bracelets"]:
           print("Invalid type of jewelry")
           return False
       else:
           return True

    @staticmethod
    def is_valid_price(price):
        return positive_float_validity(price)
    
    @staticmethod
    def is_valid_date(date_str):
        try:
            date_format = "%Y-%m-%d"  
            date = datetime.strptime(date_str, date_format)
            today = datetime.today()

            if date > today:
                print("The date can't be in the future. Try again.")
                return False

            return True
        except ValueError:
            print("Please enter the date in the correct format.")
            return False
