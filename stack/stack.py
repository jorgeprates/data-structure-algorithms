class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, element):
        node = Node(element)
        node.next = self.top
        self.top = node
        self.size += 1


    def pop(self):
        if self.size > 0:
            self.top = self.top.next
            self.size -= 1
        else:
            raise IndexError('Stack is empty')

    def peek(self):
        if self.size > 0:
            return self.top.data
        raise IndexError('Stack is empty')
    
    def __str__(self):
        node = self.top
        string = ""
        for _ in range(self.size):
            if node:
                string += f"{node.data}\n"
                node = node.next
        return string
            

