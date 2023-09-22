from linkedlist import LinkedList
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.input_list()
    linked_list.display()
    res = linked_list.calculate()
    print(f"The result is {res}")