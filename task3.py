from jewelry import read_collection_from_file, save_collection_to_file, input_jewelry
from int_validation import positive_int_validity

def menu():
    while True:
        filename = input("Enter the file name: ")
        jewelry_collection = read_collection_from_file(filename)
        if jewelry_collection is not None:
            break
    while True:
        p = input(
            "\n1 to enter a new item, 2 to delete by ID, 3 to edit by ID, 4 to search with key, 5 to sort, 6 to show collection, 7 to undo/redo, 0 to exit: ")
        match (p):
            case "1":
                    new_jewelry = input_jewelry()
                    if jewelry_collection.add_jewelry(new_jewelry):
                        save_collection_to_file(filename, jewelry_collection)
                        print("Item added successfully.")
                        
            case "2":
                ID = input("Enter jewelry ID to delete: ")
                if jewelry_collection.remove_jewelry_by_id(ID):
                    print(f"Item with ID {ID} has been deleted.")
                    save_collection_to_file(filename, jewelry_collection)
                else:
                    print("ID not found.")
 
            case "3":
                while True:
                    new_jewelry_data = input_jewelry()
                    edit_id = new_jewelry_data.ID
                    if jewelry_collection.edit_jewelry_by_id(edit_id, new_jewelry_data):
                        save_collection_to_file(filename, jewelry_collection)
                        print(f"Item with ID {edit_id} has been modified.")
                        break
                    else:
                        print("ID not found.")
 
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
                    sort_choice = input(
                        "1 to sort by ID, 2 — title, 3 — material, 4 — type, 5 — date of creation, 6 — price ")
 
                    match sort_choice:
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
 
            case "7":
                while True:
                    jewelry_id = input("Enter ID of jewelry to undo: ")
                    if not positive_int_validity(jewelry_id):
                        print("Invalid ID.")
                        continue
                    jewelry_collection.revert_jewelry_by_id(jewelry_id)
                    save_collection_to_file(filename, jewelry_collection)
                    break
            case "0":
                return
 
            case _:
                print("Error. Please enter a valid option.")

if __name__ == "__main__":
    menu()