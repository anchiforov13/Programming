def int_validity(some_string):
    try:
        int(some_string)
        return True
    except ValueError:
        print("Invalid input. Please enter an integer")
        return False
    
def positive_int_validity(some_string):
    if int_validity(some_string) and int(some_string) <= 0:
        print("Invalid input. The integer has to be positive")
        return False
    elif not int_validity(some_string):
        return False
    else:
        return True
    
def float_validity(some_string):
    try:
        float(some_string)
        return True
    except ValueError:
        print("Invalid input. Please enter a float number.")
        return False
    
def positive_float_validity(some_string):
    if float_validity(some_string) and float(some_string) <= 0:
        print("Invalid input. The float number has to be positive")
        return False
    elif not float_validity(some_string):
        return False
    else:
        return True