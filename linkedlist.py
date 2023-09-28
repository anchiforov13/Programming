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

    def generate_list(self, start, end, num):
            for _ in range(num):
                data = random.randint(start, end)
                self.append(data)

    def insert(self, element, position):
            new_node = Node(element)

            if position == 0:
                new_node.next = self.head
                self.head = new_node
                return

            current = self.head
            count = 0

            while current and count < position - 1:
                current = current.next
                count += 1

            if current is None:
                print("Error. Current position does not exist in the list.")
            else:
                new_node.next = current.next
                current.next = new_node

    def delete(self, position):
        if position == 0:
            if self.head:
                self.head = self.head.next
            else:
                print("Error. The list is empty.")
                
        current = self.head
        count = 0

        while current and count < position - 1:
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