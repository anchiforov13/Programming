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

    def input_list(self):
        n = int(input("Enter the number of elements: "))
        for _ in range(n):
            data = int(input("Enter the element: "))
            self.append(data)

    def generate_list(self):
        a = int(input("Enter the start of the range: "))
        b = int(input("Enter the end of the range: "))
        n = int(input("Enter the number of elements to generate: "))
        for _ in range(n):
            data = random.randint(a, b)
            self.append(data)

    def insert(self, data, k):
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

    def delete(self, k):
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

    def calculate(self):
        lastPosIndex = -1
        index = 0
        current = self.head
        product = 1
        while current:
            if current.data > 0:
                lastPosIndex = index
            current = current.next
            index += 1

        if lastPosIndex == -1:
            print("The list has no positive elements.")
            return None

        current = self.head
        for i in range(lastPosIndex):
            product *= current.data
            current = current.next
        
        return product

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.input_list()
    linked_list.display()
    res = linked_list.calculate()
    print(f"The result is {res}")