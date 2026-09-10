from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, element):
        if not self.head: # se não existir o primeiro nó da lista
            self.head = Node(element)
            self._size += 1
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(element)
            self._size += 1

    def _getnode(self, index):
        if index < 0:
            raise IndexError('Index out of range')

        node = self.head
        
        for i in range(index):
            if node:
                node = node.next  # () => () => () => None | index == 3 ->  IndexError | index == 2 -> node.element da posição 2
            else:
                raise IndexError('Index out of range')

        return node

    def __getitem__(self, index):
        # get element through index
        node = self._getnode(index)

        if node:
            return node.element

        raise IndexError('Index out of range')

    def __setitem__(self, index, value):
        # set element through index
        node = self._getnode(index)

        if node:
            node.element = value
        else:
            raise IndexError('Index out of range')

    def search_index(self, p_element):
        # get index through element
        node = self.head
        index = 0

        while node:
            if node.element != p_element:
                node = node.next
                index += 1
            else:
                return index

        raise ValueError('Invalid index')

    def insert(self, index, element):
        if index == 0:          # special case if we want to insert on the beggining of the list
            node = Node(element)
            node.next = self.head # self.head already point to the nexts elements, so we dont lost the chain
            self.head = node
            self._size += 1
        else:
            nodeBackPosition = self._getnode(index - 1)
            node = Node(element)
            nodePosition = nodeBackPosition.next

            node.next = nodePosition
            nodeBackPosition.next = node
            self._size += 1

    def remove(self, index):
        if index == 0:
            if self.head:
                self.head = self.head.next
                self._size -= 1
        else:
            nodeBackPosition = self._getnode(index - 1)
            if nodeBackPosition.next:
                node = nodeBackPosition.next
                nodeFrontPosition = node.next
            else:
                raise IndexError('Index out of range')

            nodeBackPosition.next = nodeFrontPosition
            self._size -= 1
            
    def __str__(self):
        node = self.head
        string = ""
        for i in range(self._size):
            string += f"{node.element} "
            node = node.next

        return string

    def __len__(self):
        return self._size