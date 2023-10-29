import re
from datetime import datetime

class Validator:
    @staticmethod
    def is_valid_by_regex(param, regex, message):
        if re.match(regex, str(param).strip()):
            return True
        print(message + f": {param}")
        return False
 
    @staticmethod
    def is_valid_by_being_in_group(param, group, message):
        if param.lower() in group:
            return True
        print(message + f": {param}")
        return False
 
    @staticmethod
    def is_valid_date(date_str):
        try:
            date_format = "%Y-%m-%d"
            date = datetime.strptime(date_str, date_format)
            today = datetime.today()
 
            if date > today:
                print("The date can't be in the future. Try again." + f": {date_str}")
                return False
 
            return True
        except ValueError:
            print("Please enter the date in the correct format." + f": {date_str}")
            return False