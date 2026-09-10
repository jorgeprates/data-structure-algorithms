class DynamicIntArray:
    def __init__(self, capacity=2):
        if capacity <= 0:
            raise ValueError("Capacidade inicial deve ser maior que 0.")
        self.capacity = capacity        # Tamanho real do array interno
        self.size = 0                   # Quantos elementos o usuário colocou
        self.data = [0] * self.capacity # Cria Array estático interno (só de inteiros)

    def is_empty(self):
        #TODO: Retornar True se a lista estiver vazia, False caso contrário
        if self.size == 0:
            return True
        else:
            return False

    def get(self, index):
        #TODO: Retornar o valor do elemento no índice fornecido. Lançar IndexError se o índice for inválido.
        if index < 0 or index >= self.capacity:
            raise IndexError('Index out of range!')

        return self.data[index]


    def set(self, index, value):
        #TODO: Definir o valor do elemento no índice fornecido. Lançar IndexError se o índice for inválido.
        if index < 0 or index >= self.capacity:
            raise IndexError('Index out of range!')
        
        self.data[index] = value
        
        

    def append(self, value):
        #TODO: Adicionar um elemento ao final da lista. Redimensionar o array interno se necessário.
        if self.size < self.capacity:
            self.data[self.size] = value
            self.size += 1
        else:
            self._resize(self.capacity*2)
            self.data[self.size] = value
            self.size += 1

    def _resize(self, new_capacity):
        if new_capacity > self.capacity:
            print(f"⏫ Redimensionando de {self.capacity} para {new_capacity}")
        else:
            print(f"⏬ Redimensionando de {self.capacity} para {new_capacity}")
        new_data = [0] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def __str__(self):
        return str(self.data[:self.size])


lista = DynamicIntArray()

# Saída: Lista vazia!
if lista.is_empty():
    print("Lista vazia!")
else:
    print("Lista tem elementos.")

print("Adicionando o 10;")
lista.append(10)
#Saída: Lista:  [10] 
print("Lista: ", lista) 
print("Tamanho da Lista para o usuário: ", lista.size)
print("Tamanho real da Lista internamente: ", lista.capacity)
print()

print("Adicionando o 20;")
lista.append(20)
#Saída: Lista:  [10, 20] 
print("Lista: ", lista)
print("Tamanho da Lista para o usuário: ", lista.size)
print("Tamanho real da Lista internamente: ", lista.capacity)
print()

print("Adicionando o 30;")
lista.append(30)
print("Lista: ", lista)
print("Tamanho da Lista para o usuário: ", lista.size)
print("Tamanho real da Lista internamente: ", lista.capacity)
print()


print("Adicionando o 40;")
lista.append(40)
print("Lista: ", lista)
print("Tamanho da Lista para o usuário: ", lista.size)
print("Tamanho real da Lista internamente: ", lista.capacity)
print()

print("Adicionando o 50;")
lista.append(50)
# Saída: [10, 20, 30, 40, 50]   
print("Lista: ", lista)
print("Tamanho da Lista para o usuário: ", lista.size)
print("Tamanho real da Lista internamente: ", lista.capacity)
print()        
