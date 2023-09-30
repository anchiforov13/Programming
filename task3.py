from validation import Validator
from jewelry import Jewelry, JewelryCollection, read_collection_from_file, save_collection_to_file

def menu():
    while True:
        p = input("\n1 to enter a new item, 2 to delete by ID, 3 to edit by ID, 4 to search with key, 5 to sort, 6 to show collection, 0 to exit: ")
        match(p):
            case "1":
                while True:
                    ID = input("Enter ID: ")
                    title = input("Enter title: ")
                    code = input("Enter code: ")
                    material = input("Enter material (gold/silver/platinum): ")
                    jewelry_type = input("Enter type (rings/earrings/bracelets): ")
                    date_of_creation = input("Enter date of creation: ")
                    price = float(input("Enter price: "))

                    if Validator.is_valid_age(ID) and Validator.is_valid_name(title) and Validator.is_valid_code(code) and Validator.is_valid_material(material) and Validator.is_valid_type(jewelry_type) and Validator.is_valid_name(date_of_creation) and Validator.is_valid_price(price):
                        new_jewelry = Jewelry(ID, title, code, material, jewelry_type, date_of_creation, price)
                        jewelry_collection.add_jewelry(new_jewelry)
                        save_collection_to_file(filename, jewelry_collection)
                        print("Item added successfully.")
                    else:
                        continue
                    break

            case "2":
                ID = input("Enter jewelry ID to delete: ")
                if (jewelry_collection.remove_jewelry_by_id(ID)):
                    print(f"Item with ID {ID} has been deleted.")
                    save_collection_to_file(filename, jewelry_collection)
                else:
                    print("ID not found.")

            case "3":
                ID = input("Enter jewelry ID to edit: ")
                title = input("Enter new title: ")
                code = input("Enter new code: ")
                material = input("Enter new material (gold/silver/platinum): ")
                jewelry_type = input("Enter new type (rings/earrings/bracelets): ")
                date_of_creation = input("Enter new date of creation: ")
                price = float(input("Enter new price: "))

                if Validator.is_valid_age(ID) and Validator.is_valid_name(title) and Validator.is_valid_code(code) and Validator.is_valid_material(material) and Validator.is_valid_type(jewelry_type) and Validator.is_valid_name(date_of_creation) and Validator.is_valid_price(price):
                    new_jewelry_data = Jewelry(ID, title, code, material, jewelry_type, date_of_creation, price)
                    jewelry_collection.edit_jewelry_by_id(ID, new_jewelry_data)
                    save_collection_to_file(filename, jewelry_collection)
                    print(f"Item with ID {ID} has been modified.")
                else:
                    continue

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
                    sort_choice = input("1 to sort by ID, 2 — title, 3 — material, 4 — type, 5 — date of creation, 6 — price")
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
    filename = "jewelry_collection.txt"
    jewelry_collection = read_collection_from_file(filename)
    menu()