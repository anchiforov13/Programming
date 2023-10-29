import copy
from validation import Validator
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
    def ID(self, value):
        if positive_int_validity(value):
            self._ID = value

    @title.setter
    def title(self, value):
        if Validator.is_valid_by_regex(
                value, r"^[a-zA-Z\s]+$", "The name should only contain letters of the alphabet"):
            self._title = value

    @code.setter
    def code(self, value):
        if Validator.is_valid_by_regex(
                value, r"^\w{5}/\w-\w{2}$", "Error. The code should be in the correct format"):
            self._code = value

    @material.setter
    def material(self, value):
        if Validator.is_valid_by_being_in_group(value, ["gold", "silver", "platinum"], "Invalid material option"):
            self._material = value

    @jewelry_type.setter
    def jewelry_type(self, value):
        if Validator.is_valid_by_being_in_group(value, ["rings", "earrings", "bracelets"], "Invalid type of jewelry"):
            self._jewelry_type = value

    @date_of_creation.setter
    def date_of_creation(self, value):
        if Validator.is_valid_date(value):
            self._date_of_creation = value

    @price.setter
    def price(self, value):
        if (Validator.is_valid_by_regex(value, r"^\d+\.\d[1-9]?$", "Please enter a valid price") and
                positive_float_validity(value)):
            self._price = value

    def __str__(self):
        return f"ID: {self._ID}, Title: {self._title}, Code: {self._code}, Material: {self._material}, " \
               f"Type: {self._jewelry_type}, Date of Creation: {self._date_of_creation}, Price: {self._price}"
    
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
        self.collection.append(jewelry)
        self.collection_history[jewelry.ID] = JewelryHistory(jewelry)

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
                jewelry.title = new_jewelry_data.title or jewelry.title
                jewelry.code = new_jewelry_data.code or jewelry.code
                jewelry.material = new_jewelry_data.material or jewelry.material
                jewelry.jewelry_type = new_jewelry_data.jewelry_type or jewelry.jewelry_type
                jewelry.date_of_creation = new_jewelry_data.date_of_creation or jewelry.date_of_creation
                jewelry.price = new_jewelry_data.price or jewelry.price

    def search_jewelry(self, query):
        results = []
        for jewelry in self.collection:
            if query.lower() in jewelry.title.lower() or query.lower() in jewelry.code.lower() or query.lower() in jewelry.material.lower() or query.lower() in jewelry.jewelry_type.lower():
                results.append(jewelry)
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
        version_index = input("How many versions to go back? ")
        for jewelry in self.collection:
            if jewelry.ID == jewelry_id:
                jewelry_history = self.collection_history[jewelry_id]
                if version_index:
                    jewelry_history.redo(int(version_index))
                else:
                    jewelry_history.undo()

def read_collection_from_file(filename):
    collection = JewelryCollection()
    try:
        with open(filename) as file:
            for line in file:
                data = line.strip().split(',')
                ID, title, code, material, jewelry_type, date_of_creation, price = data
                jewelry = Jewelry(ID, title, code, material, jewelry_type, date_of_creation, float(price))
                collection.add_jewelry(jewelry)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None
    return collection

def save_collection_to_file(filename, collection):
    with open(filename, 'w') as file:
        for jewelry in collection.collection:
            file.write(f"{jewelry.ID},{jewelry.title},{jewelry.code},{jewelry.material},"
                       f"{jewelry.jewelry_type},{jewelry.date_of_creation},{jewelry.price}\n")
            
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
        else:
            snapshot = self.history.pop(-1*ind)
            self.jewelry.restore(snapshot)