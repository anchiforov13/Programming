import re
from datetime import datetime
from int_validation import positive_float_validity

class Validator:
    @staticmethod
    def is_valid_name(name):
        pattern = "^[a-zA-Z]+$"
        if re.match(pattern, name):
            return True
        else:
            print("The name should only contain letters of the alphabet")
            return False

    @staticmethod
    def is_valid_code(code):
        pattern = r"^\w{5}/\w-\w{2}$"
    
        if re.match(pattern, code):
            return True
        else:
            print("Error. The code should be in the correct format")
            return False

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
        pattern = r"^\d+\.\d{2}$"
        if positive_float_validity(price) and re.match(pattern, price):
            return True
        else:
            print("Please enter a valid price")
            return False
    
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
