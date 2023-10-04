import re
from datetime import datetime
from int_validation import positive_float_validity

class Validator:
    @staticmethod
    def is_valid_name(name):
        pattern = "^[a-zA-Z]+$"
        if re.match(pattern, name.strip()):
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

            return True
        except ValueError:
            print("Please enter the date in the correct format.")
            return False