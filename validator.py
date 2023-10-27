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
    def is_valid_price(price):
        pattern = r"^\d+\.\d{2}$"
        if positive_float_validity(price) and re.match(pattern, price):
            return True
        else:
            print("Please enter a valid price")
            return False
        
    @staticmethod
    def is_valid_date(date_str, min_date=None):
        try:
            date_format = "%Y-%m-%d"  
            date = datetime.strptime(date_str, date_format)
            today = datetime.today()

            if date > today:
                print("The date can't be in the future. Try again.")
                return False
            
            if min_date and date < min_date:
                print(f"The date should be greater than or equal to {min_date.strftime('%Y-%m-%d')}")
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