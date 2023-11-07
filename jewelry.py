from validation import Validator
from int_validation import positive_int_validity
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
        if Validator.is_valid_name(value):
            self._title = value

    @code.setter
    def code(self, value):
        if Validator.is_valid_code(value):
            self._code = value

    @material.setter
    def material(self, value):
        if Validator.is_valid_material(value):
            self._material = value

    @jewelry_type.setter
    def jewelry_type(self, value):
        if Validator.is_valid_type(value):
            self._jewelry_type = value

    @date_of_creation.setter
    def date_of_creation(self, value):
        if Validator.is_valid_date(value):
            self._date_of_creation = value

    @price.setter
    def price(self, value):
        if Validator.is_valid_price(value):
            self._price = value

    def __str__(self):
        return ", ".join([f"{attr}: {val}" for attr, val in self.__dict__.items()])

class JewelryCollection:
    def __init__(self):
        self.collection = []

    def add_jewelry(self, jewelry):
        self.collection.append(jewelry)

    def remove_jewelry_by_id(self, ID):
        for jewelry in self.collection:
            if jewelry.ID == ID:
                self.collection.remove(jewelry)
                return True

    def edit_jewelry_by_id(self, ID, new_jewelry_data):
        for jewelry in self.collection:
            if jewelry.ID == ID:
                jewelry.title = new_jewelry_data.title
                jewelry.code = new_jewelry_data.code
                jewelry.material = new_jewelry_data.material
                jewelry.jewelry_type = new_jewelry_data.jewelry_type
                jewelry.date_of_creation = new_jewelry_data.date_of_creation
                jewelry.price = new_jewelry_data.price

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

def read_collection_from_file(filename):
    collection = JewelryCollection()
    try:
        with open(filename, 'r') as file:
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