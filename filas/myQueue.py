from node import Node

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
           self.tail.next = node
           self.tail = node
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError('Queue is empty')

        elem = self.head.data
        self.head = self.head.next
        self.size -= 1
        return elem

    def peek(self):
        if self.size == 0:
            raise IndexError('Queue is empty')

        elem = self.head.data
        return elem

    def __repr__(self):
        string = ""
        node = self.head
        for _ in range(self.size):
            if node:
                string += f"{node.data} "
                node = node.next
        return string


    def __str__(self):
        return self.__repr__()

fila = Queue()

fila.push(3)
fila.push(33)
fila.push(344)
fila.push(24)

print(fila)

fila.pop()

print(fila)

fila.peek()