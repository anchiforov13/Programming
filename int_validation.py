def int_validity(some_string):
    try:
        int(some_string)
        return True
    except ValueError:
        return False