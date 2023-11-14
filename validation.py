import re
from datetime import datetime
from int_validation import positive_int_validity, positive_float_validity

def validate_positive_int(func):
    def wrapper(self, value):
        if positive_int_validity(value):
            func(self, value)
    return wrapper

def validate_positive_float(func):
    def wrapper(self, value):
        if positive_float_validity(value):
            func(self, value)
    return wrapper

def validate_by_regex(pattern, message):
    def wrapper(func):
        def inner(self, value):
            if Validator.is_valid_by_regex(value, pattern, message):
                func(self, value)
        return inner
    return wrapper

def validate_in_group(group, message):
    def wrapper(func):
        def inner(self, value):
            if Validator.is_valid_by_being_in_group(value, group, message):
                func(self, value)
        return inner
    return wrapper

def validate_date(func):
    def wrapper(self, value):
        if Validator.is_valid_date(value):
            func(self, value)
    return wrapper

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