class DynamicIntArray:
    def __init__(self, capacity=2):
        if capacity <= 0:
            raise ValueError("Capacidade inicial deve ser maior que 0.")
        self.capacity = capacity        # Tamanho real do array interno
        self.size = 0                   # Quantos elementos o usuário colocou
        self.data = [0] * self.capacity # Cria Array estático interno (só de inteiros)

    def is_empty(self):
        """
        Indica se o array está vazio.

        Retorno:
            bool: True se não há elementos (size), False caso contrário.
        """
        return self.size == 0

    def get(self, index):
        """
        Retorna o elemento no índice informado.

        Parâmetros:
            index (int): Índice do elemento (0 <= index < size).

        Retorno:
            int: Valor armazenado naquele índice.

        Exceções:
            IndexError("Indice Fora dos Limites."): se index estiver fora dos limites.
        """
        if index < 0 or index >= self.size:
            raise IndexError("Indice Fora dos Limites.")
        return self.data[index]

    def set(self, index, value):
        """
        Substitui o valor no índice informado por um novo valor inteiro.

        Parâmetros:
            index (int): Índice alvo (0 <= index < size).
            value (int): Novo valor a ser armazenado.

        Exceções:
            IndexError("Indice Fora dos Limites."): se index estiver fora dos limites.
        """
        if index < 0 or index >= self.size:
            raise IndexError("Indice Fora dos Limites.")
        self.data[index] = value

    def append(self, value):
        """
        Insere um valor inteiro ao final do array, redimensionando se preciso.
        O Redimensionamento é feito dobrando o tamanho do array, chamando _resize.

        Parâmetros:
            value (int): Valor a ser adicionado no fim.
        """
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        self.data[self.size] = value
        self.size += 1

    def _resize(self, new_capacity): 
        """
        Redimensiona o array interno para new_capacity, copiando os elementos existentes.

        Parâmetros:
            new_capacity (int): Nova capacidade interna (>= 2 em reduções).

        Observações:
            - Este método preserva a ordem dos elementos.
            - Em crescimento, normal dobrar a capacidade.
            - Em redução, encolhe pela metade quando size <= 1/4 da capacity, 
            mas nunca abaixo de 2.
        """
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

    def remove_at(self, index):
        """
        Remove e retorna o elemento no índice informado, deslocando os seguintes à esquerda.

        Parâmetros:
            index (int): Índice do elemento a remover (0 <= index < size).

        Retorno:
            int: Valor removido. (Retornar o Valor Removido)

        Exceções:
            IndexError: se index estiver fora dos limites.

        Detalhes:
            - Após remover, se size <= 1/4 capacity (mínimo 2) chama _resize.
        """
        if index < 0 or index >= self.size:
            raise IndexError("Indice Fora dos Limites.")

        # SEU CÓDIGO AQUI

    
lista = DynamicIntArray()


#============ SAIDAS DE TESTE ============

if lista.is_empty():
    print("Lista vazia!")
else:
    print("Lista tem elementos.")

print("Adicionando o 10;")
lista.append(10)
print("Lista: ", lista) 

print("Adicionando o 20;")
lista.append(20)
print("Lista: ", lista)

print("Adicionando o 30;")
lista.append(30)
print("Lista: ", lista)
print("Tamanho da Lista para o usuário: ", lista.size)
print("Tamanho real (capacidade) da Lista internamente: ", lista.capacity)

print("Adicionando o 40;")
lista.append(40)
print("Lista: ", lista)

print("Adicionando o 50;")
lista.append(50)
print("Lista: ", lista)        

print("Elemento na posição 2: ", lista.get(2))    

print("Trocando elemento no índice 2 para 99.")   
lista.set(2, 99)
print("Lista: ", lista)       


print("Removendo elemento no indice 1 se existir.") 
lista.remove_at(1) 
print("Lista: ", lista)

print("Removendo mais um elementos no indice 2.") 
lista.remove_at(2)
print("Lista: ", lista)

print("Removendo mais um elementos no indice 0.") 
lista.remove_at(0)
print("Lista: ", lista)