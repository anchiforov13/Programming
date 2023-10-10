from validation import Validator
from jewelry import Jewelry, read_collection_from_file, save_collection_to_file
from int_validation import positive_int_validity

def menu():
    while True:
        filename = input("Enter the file name: ")
        jewelry_collection = read_collection_from_file(filename)
        if jewelry_collection is not None:
            break
    while True:
        p = input("\n1 to enter a new item, 2 to delete by ID, 3 to edit by ID, 4 to search with key, 5 to sort, 6 to show collection, 0 to exit: ")
        match(p):
            case "1":
                while True:
                    ID = input("Enter ID: ")
                    if not Validator.is_valid_id(ID):
                        continue
                    title = input("Enter title: ")
                    if not Validator.is_valid_name(title):
                        continue
                    code = input("Enter code: ")
                    if not Validator.is_valid_code(code):
                        continue
                    material = input("Enter material (gold/silver/platinum): ")
                    if not Validator.is_valid_material(material):
                        continue
                    jewelry_type = input("Enter type (rings/earrings/bracelets): ")
                    if not Validator.is_valid_type(jewelry_type):
                        continue
                    date_of_creation = input("Enter date of creation: ")
                    if not Validator.is_valid_date(date_of_creation):
                        continue
                    price = input("Enter price: ")
                    if not Validator.is_valid_price(price):
                        continue
                    price = float(price)

                    new_jewelry = Jewelry(ID, title, code, material, jewelry_type, date_of_creation, price)
                    jewelry_collection.add_jewelry(new_jewelry)
                    save_collection_to_file(filename, jewelry_collection)
                    print("Item added successfully.")
                    break

            case "2":
                ID = input("Enter jewelry ID to delete: ")
                if (jewelry_collection.remove_jewelry_by_id(ID)):
                    print(f"Item with ID {ID} has been deleted.")
                    save_collection_to_file(filename, jewelry_collection)
                else:
                    print("ID not found.")

            case "3":
                while True:
                    ID = input("Enter jewelry ID to edit: ")
                    title = input("Enter new title: ")
                    if not Validator.is_valid_name(title):
                        continue
                    code = input("Enter new code: ")
                    if not Validator.is_valid_code(code):
                        continue
                    material = input("Enter new material (gold/silver/platinum): ")
                    if not Validator.is_valid_material(material):
                        continue
                    jewelry_type = input("Enter new type (rings/earrings/bracelets): ")
                    if not Validator.is_valid_type(jewelry_type):
                        continue
                    date_of_creation = input("Enter new date of creation: ")
                    if not Validator.is_valid_date(date_of_creation):
                        continue
                    price = input("Enter new price: ")
                    if not Validator.is_valid_price(price):
                        continue
                    price = float(price)

                    new_jewelry_data = Jewelry(ID, title, code, material, jewelry_type, date_of_creation, price)
                    jewelry_collection.edit_jewelry_by_id(ID, new_jewelry_data)
                    save_collection_to_file(filename, jewelry_collection)
                    print(f"Item with ID {ID} has been modified.")
                    break

            case "4":
                query = input("Enter keyword for search: ")
                results = jewelry_collection.search_jewelry(query)
                if results:
                    print("Search results:")
                    for result in results:
                        print(result)
                else:
                    print("No results found.")

            case "5":
                while True:
                    sort_choice = input("1 to sort by ID, 2 — title, 3 — material, 4 — type, 5 — date of creation, 6 — price ")
                    key = None
                    
                    match(sort_choice):
                        case "1":
                            key = lambda x: x.ID
                        case "2":
                            key = lambda x: x.title
                        case "3":
                            key = lambda x: x.material
                        case "4":
                            key = lambda x: x.jewelry_type
                        case "5":
                            key = lambda x: x.date_of_creation
                        case "6":
                            key = lambda x: x.price
                        case _:
                            print("Error. Please enter a valid option.")
                            continue
                    jewelry_collection.sort_jewelry(key)
                    print("Collection sorted by given key")
                    break

            case "6":
                jewelry_collection.display_collection()

            case "0":
                return

            case _:
                print("Error. Please enter a valid option.")

if __name__ == "__main__":
    menu()