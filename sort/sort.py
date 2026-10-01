######## bubbleSort 

# lista = list(map(int, input("Informe os números da lista: ").split()))
# print(f"Lista informada: {lista}")

def bubbleSort(arr):
    for i in arr:
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                aux = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = aux

# bubbleSort(lista)
# print(f"lista ordenada: {lista}")

######## QuickSort



