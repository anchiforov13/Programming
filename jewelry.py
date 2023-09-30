class Jewelry:
    def __init__(self, ID, title, code, material, jewelry_type, date_of_creation, price):
        self.ID = ID
        self.title = title
        self.code = code
        self.material = material
        self.jewelry_type = jewelry_type
        self.date_of_creation = date_of_creation
        self.price = price

    def __str__(self):
        return f"ID: {self.ID}, Title: {self.title}, Code: {self.code}, Material: {self.material}, " \
               f"Type: {self.jewelry_type}, Date of Creation: {self.date_of_creation}, Price: {self.price}"

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
            if query in str(jewelry):
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
    return collection

def save_collection_to_file(filename, collection):
    with open(filename, 'w') as file:
        for jewelry in collection.collection:
            file.write(f"{jewelry.ID},{jewelry.title},{jewelry.code},{jewelry.material},"
                       f"{jewelry.jewelry_type},{jewelry.date_of_creation},{jewelry.price}\n")