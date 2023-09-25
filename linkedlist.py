import random
from int_validation import int_validity

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

    def validity_check(self, some_string):
            return int_validity(some_string)

    def input_list(self):
        while True:
            n = input("Enter the number of elements to add: ")
            if not self.validity_check(n) or int(n) < 0:
                print("Error. The number of elements has to be a positive integer.")
                continue
            n = int(n)
            i = 0
            while i < n:
                data = (input("Enter the element: "))
                if self.validity_check(data):
                    self.append(int(data))
                    i += 1
                else:
                    print("Invalid input. Please enter integer values.")
            break

    def generate_list(self):
        while True:
            a = input("Enter the start of the range: ")
            b = input("Enter the end of the range: ")
            n = input("Enter the number of elements to generate: ")
            if not self.validity_check(a) or not self.validity_check(b) or not self.validity_check(n):
                print("Invalid input. Please enter integer values.")
                continue
            if int(b) < int(a): 
                print("Error. The start of range should be less than the end of range.")
                continue
            if int(n) < 0:
                print("Error. The number of elements has to be a positive integer.")
                continue
            a, b, n = int(a), int(b), int(n)
            for _ in range(n):
                data = random.randint(a, b)
                self.append(data)
            break

    def insert(self):
        while True:
            data = input("Enter data for a new element: ")
            k = input("Enter position for the new element: ")

            if not self.validity_check(data) or not self.validity_check(k):
                print("Invalid input. Please enter integer values.")
                continue

            data = int(data)
            k = int(k)

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

            if current is None or k < 0:
                print("Error. Current position does not exist in the list.")
                continue
            else:
                new_node.next = current.next
                current.next = new_node
            break

    def delete(self):
        while True:
            k = input("Enter position for the element to be deleted: ")

            if not self.validity_check(k):
                print("Invalid input. Please enter integer values.")
                continue

            k = int(k)

            if k == 0:
                if self.head:
                    self.head = self.head.next
                else:
                    print("Error. The list is empty.")
                break

            current = self.head
            count = 0

            while current and count < k - 1:
                current = current.next
                count += 1

            if current is None or current.next is None or k < 0:
                print("Error. Current position does not exist in the list.")
                continue
            else:
                current.next = current.next.next
            break

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