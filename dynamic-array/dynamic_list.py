class DynamicIntArray:
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.size = 0
        self.data = [0] * capacity

    def resize(self, newCapacity):
        self.capacity = newCapacity
        newData = [0] * newCapacity
        for i in range(self.size):
            newData[i] = self.data[i]
        self.data = newData


    def append(self, element):
        if self.size < self.capacity:
            self.data[self.size] = element
            self.size += 1
        else:
            self.resize(self.capacity*2)
            self.data[self.size] = element
            self.size += 1


    def remove_at(self, index):
        """ efeito dominó
        
            percebemos que self.size sempre 'apontará' para uma vaga a frente de self.data,
            logo a vaga que self.size aponta nunca terá elemento algum.

            !!! se self.size for menor ou igual a 25% da capacidade, ou seja, 1/4 da capacidade devemos diminuir a capacidade
            pela metade.
        """

        if index < 0:
            raise IndexError('Index out of range')

        # if self.size < self.capacity // 4:
        #     self.resize(self.capacity//2)

        if index < self.size:
            for i in range(index, self.size):
                if self.data[i] == self.data[self.size - 1]:
                    self.data[i] = 0
                else:
                    self.data[i] = self.data[i + 1]
        else:
            raise IndexError('Index out of range')
        self.size -= 1


    def insert(self, index, element):     
        """
            encontramos o elemento que se encontra na posição que desejamos inserir o novo elemento.
            a partir daí temos que realocar todos os elementos que se encontram da posição do elemento
            encontrato para uma posição a frente

            feito podemos inserir o elemento novo na posição desejada
        """

        if index < 0 or index >= self.size:
            raise IndexError('Index out of range')

        if self.size == self.capacity:
            self.resize(self.capacity*2)

        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]

        self.data[index] = element
        self.size += 1

        print(self.data)


        
        