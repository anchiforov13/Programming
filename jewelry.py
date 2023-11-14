import copy
from validation import *
from int_validation import positive_int_validity, positive_float_validity
class Jewelry:
    def __init__(self, ID, title, code, material, jewelry_type, date_of_creation, price):
        self._ID = ID
        self._title = title
        self._code = code
        self._material = material
        self._jewelry_type = jewelry_type
        self._date_of_creation = date_of_creation
        self._price = price

    @property
    def ID(self):
        return self._ID

    @property
    def title(self):
        return self._title

    @property
    def code(self):
        return self._code

    @property
    def material(self):
        return self._material

    @property
    def jewelry_type(self):
        return self._jewelry_type

    @property
    def date_of_creation(self):
        return self._date_of_creation

    @property
    def price(self):
        return self._price
    
    @ID.setter
    @validate_positive_int
    def ID(self, value):
        self._ID = value

    @title.setter
    @validate_by_regex(r"^[a-zA-Z\s]+$", "The name should only contain letters of the alphabet")
    def title(self, value):
        self._title = value

    @code.setter
    @validate_by_regex(r"^\w{5}/\w-\w{2}$", "Error. The code should be in the correct format")
    def code(self, value):
        self._code = value

    @material.setter
    @validate_in_group(["gold", "silver", "platinum"], "Invalid material option")
    def material(self, value):
        self._material = value

    @jewelry_type.setter
    @validate_in_group(["rings", "earrings", "bracelets"], "Invalid type of jewelry")
    def jewelry_type(self, value):
        self._jewelry_type = value

    @date_of_creation.setter
    @validate_date
    def date_of_creation(self, value):
        if Validator.is_valid_date(value):
            self._date_of_creation = value

    @price.setter
    @validate_by_regex(r"^\d+\.\d[1-9]?$", "Please enter a valid price")
    @validate_positive_float
    def price(self, value):
        self._price = value

    def __str__(self):
        return ", ".join([f"{attr[1:].capitalize()}: {val}" for attr, val in self.__dict__.items()])
    
    @property
    def state(self):
        return self.__dict__
 
    def save(self):
        return SnapShot(self.state)
 
    def restore(self, snapshot):
        self.__dict__ = snapshot.get_state()

class JewelryCollection:
    def __init__(self):
        self.collection = []
        self.collection_history = {}

    def add_jewelry(self, jewelry):
        if any(existing_jewelry.ID == jewelry.ID for existing_jewelry in self.collection):
            print(f"Error: Jewelry with ID {jewelry.ID} already exists in the collection.")
            return False
        else:
            self.collection.append(jewelry)
            self.collection_history[jewelry.ID] = JewelryHistory(jewelry)
        return True

    def remove_jewelry_by_id(self, ID):
        for jewelry in self.collection:
            if jewelry.ID == ID:
                self.collection.remove(jewelry)
                del self.collection_history[ID]
                return True
        return False

    def edit_jewelry_by_id(self, ID, new_jewelry_data):
        for jewelry in self.collection:
            if jewelry.ID == ID:
                self.collection_history[ID].save()
                for attr, val in new_jewelry_data.__dict__.items():
                    setattr(jewelry, attr[1:], val)
                return True
        return False

    def search_jewelry(self, query):
        results = []
        for jewelry in self.collection:
            for attr, val in jewelry.__dict__.items():
                if query.lower() in str(val).lower():
                    results.append(jewelry)
                    break
        return results

    def sort_jewelry(self, key):
        self.collection.sort(key=key)

    def display_collection(self):
        for jewelry in self.collection:
            print(jewelry)

    def __iter__(self):
        return iter(self.collection)
 
    def __getitem__(self, item):
        return self.collection[item]
    
    def revert_jewelry_by_id(self, jewelry_id):
        while True:
            version_index = input("How many versions to go back? ")
            if version_index == '' or positive_int_validity(version_index):
                for jewelry in self.collection:
                    if jewelry.ID == jewelry_id:
                        jewelry_history = self.collection_history[jewelry_id]
                        if version_index:
                            jewelry_history.redo(int(version_index))
                        else:
                            jewelry_history.undo()
            else:
                print("Please enter an integer. ")
                continue
            break

def input_jewelry():
        while True:
            ID = input("Enter ID: ")
            if not positive_int_validity(ID):
                continue
            title = input("Enter title: ")
            if not Validator.is_valid_by_regex(
                    title, "^[a-zA-Z\s]+$", "The name should only contain letters of the alphabet"):
                continue
            code = input("Enter code: ")
            if not Validator.is_valid_by_regex(
                    code, r"^\w{5}/\w-\w{2}$", "Error. The code should be in the correct format"):
                continue
            material = input("Enter material (gold/silver/platinum): ")
            if not Validator.is_valid_by_being_in_group(
                    material.lower(), ["gold", "silver", "platinum"], "Invalid material option"):
                continue
            jewelry_type = input("Enter type (rings/earrings/bracelets): ")
            if not Validator.is_valid_by_being_in_group(
                    jewelry_type.lower(), ["rings", "earrings", "bracelets"], "Invalid type of jewelry"):
                continue
            date_of_creation = input("Enter date of creation: ")
            if not Validator.is_valid_date(date_of_creation):
                continue
            price = input("Enter price: ")
            if not (Validator.is_valid_by_regex(
                    price, r"^\d+\.\d{2}$", "Please enter a valid price") and
                    positive_float_validity(price)):
                continue
            price = float(price)
            break
        return Jewelry(ID, title, code, material, jewelry_type, date_of_creation, price)

def read_collection_from_file(filename):
    collection = JewelryCollection()
    
    attribute_validators = {
        "ID": positive_int_validity,
        "title": lambda value: Validator.is_valid_by_regex(value, r"^[a-zA-Z\s]+$", "The name should only contain letters of the alphabet"),
        "code": lambda value: Validator.is_valid_by_regex(value, r"^\w{5}/\w-\w{2}$", "Error. The code should be in the correct format"),
        "material": lambda value: Validator.is_valid_by_being_in_group(value, ["gold", "silver", "platinum"], "Invalid material option"),
        "jewelry_type": lambda value: Validator.is_valid_by_being_in_group(value, ["rings", "earrings", "bracelets"], "Invalid type of jewelry"),
        "date_of_creation": Validator.is_valid_date,
        "price": lambda value: Validator.is_valid_by_regex(value, r"^\d+\.\d[1-9]?$", "Please enter a valid price") and positive_float_validity(value),
    }

    try:
        with open(filename) as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) == len(attribute_validators):
                    jewelry_data = {}
                    for attribute, value, validator in zip(attribute_validators.keys(), data, attribute_validators.values()):
                        if not validator(value):
                            break
                        jewelry_data[attribute] = value
                    else:
                        jewelry = Jewelry(**jewelry_data)
                        collection.add_jewelry(jewelry)
                else:
                    print(f"Error. Not enough attributes.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None
    return collection

def save_collection_to_file(filename, collection):
    with open(filename, 'w') as file:
        for jewelry in collection.collection:
            for i, (attr, val) in enumerate(jewelry.__dict__.items()):
                file.write(f"{val}")
                if i < len(jewelry.__dict__) - 1:
                    file.write(',')
            file.write('\n')

class SnapShot:
    def __init__(self, state):
        self.state = copy.deepcopy(state)
 
    def get_state(self):
        return self.state
 
 
class JewelryHistory:
    MAX_LENGTH = 100
 
    def __init__(self, jewelry):
        self.jewelry = jewelry
        self.history = []
 
    def save(self):
        snapshot = self.jewelry.save()
        self.history.append(snapshot)
        if len(self.history) > JewelryHistory.MAX_LENGTH:
            self.history.pop(0)

    def undo(self):
        if not self.history:
            print("This item has no history.")
        else:
            snapshot = self.history.pop()
            self.jewelry.restore(snapshot)
 
    def redo(self, ind):
        if not self.history:
            print("This item has no history.")
        elif ind > len(self.history):
            print("Version not found.")
        else:
            snapshot = self.history.pop(-1*ind)
            self.jewelry.restore(snapshot)