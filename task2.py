from linkedlist import LinkedList
from int_validation import int_validity, positive_int_validity

def menu(l: LinkedList):
    while True:
        p = input("1 to input list, 2 to generate randomly, 3 to insert element, 4 to delete element, 5 to display list, 6 to calculate main task, 0 to exit: ")
        match(p):
            case "1":
                while True:
                    n = input("Enter the number of elements: ")
                    if not positive_int_validity(n):
                        continue
                    n = int(n)
                    i = 0
                    while i < n:
                        data = (input("Enter the element: "))
                        if int_validity(data):
                            l.append(int(data))
                            i += 1
                    break
            case "2":
                while True:
                    a = input("Enter the start of the range: ")
                    b = input("Enter the end of the range: ")
                    n = input("Enter the number of elements to generate: ")
                    if not int_validity(a) or not int_validity(b) or not positive_int_validity(n):
                        continue
                    if int(b) < int(a): 
                        print("Error. The start of range should be less than the end of range.")
                        continue
                    a, b, n = int(a), int(b), int(n)
                    l.generate_list(a, b, n)
                    break
            case "3":
                while True:
                    data = input("Enter the element to insert: ")
                    k = input("Enter the position: ")
                    if not int_validity(data) or not positive_int_validity(k):
                        continue
                    data, k = int(data), int(k)
                    l.insert(data, k)
                    break
            case "4":
                while True:
                    k = input("Enter position for the element to be deleted: ")
                    if not positive_int_validity(k):
                        continue
                    k = int(k)
                    l.delete(k)
                    break
            case "5":
                l.display()
            case "6":
                print(l.calculate())
            case "0":
                return
            case _ :
                print("Error. Choose a valid option")

if __name__ == "__main__":
    linked_list = LinkedList()
    menu(linked_list)