import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def input_from_keyboard(self):
        n = int(input("Enter the number of elements: "))
        for _ in range(n):
            data = int(input("Enter the element: "))
            self.append(data)

    def generate_random(self, a, b, n):
        for _ in range(n):
            data = random.randint(a, b)
            self.append(data)

    def insert_at_position(self, data, k):
        new_node = Node(data)
        if k == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        count = 0
        while current and count < k - 1:
            current = current.next
            count += 1
        if current is None:
            print("Error. Current position does not exist in the list.")
        else:
            new_node.next = current.next
            current.next = new_node

    def delete_at_position(self, k):
        if k == 0:
            if self.head:
                self.head = self.head.next
            else:
                print("The list is empty")
            return
        current = self.head
        count = 0
        while current and count < k - 1:
            current = current.next
            count += 1
        if current is None or current.next is None:
            print("Error. Current position does not exist in the list.")
        else:
            current.next = current.next.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

if __name__ == "__main__":
    linked_list = LinkedList()

    print("1. Entering the elements:")
    linked_list.input_from_keyboard()
    linked_list.display()

    print("\n2. Generating random elements from range [a, b]:")
    linked_list.generate_random(1, 10, 5)
    linked_list.display()

    print("\n3. Adding element to position k:")
    data = int(input("Enter element to add: "))
    k = int(input("Enter the position: "))
    linked_list.insert_at_position(data, k)
    linked_list.display()

    print("\n4. Deleting element from position k:")
    k = int(input("Enter position to delete: "))
    linked_list.delete_at_position(k)
    linked_list.display()