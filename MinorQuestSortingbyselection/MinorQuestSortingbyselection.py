
# Page 54 from the book "Grokking Algorithms" by Aditya Bhargava
# Pagina 54 do livro "Entendendo Algoritmos" por Aditya Bhargava

# Function to find the index of the smallest element in the array 
# Funcao para encontrar o indice do menor elemento no array
def MinorQuest(arr): 

    smaller = arr[0]   # Assume the fist element is the smallest # Assume que o primeiro elemento e o menor
    smaller_index = 0  # Initialize the index of the smallest element # Inicializa o indice do menor elemento

    for i in range(1, len(arr)):  
        # Loop through the array starting from the second element 
        # Percorre o array a partir do segundo elemento
        
        if arr[i] < smaller:   
            # If the current element is smaller than the smallest found so far 
            # Se o elemento aatual for menor que o menor encontrado ate agora
                   
            smaller = arr[i]    # Update the smallest element # Atuliza o menor elemento
            smaller_index = i   # Update the index of the smallest element # Atualiza o indice do menor elemento

    return smaller_index     # Return the index of the smallest element # Retorna o indice do menor elemento

# Function to sort the array using selection sort algorithm
# Funcao para ordenar o array usando o algoritmo de ordenacao por selecao
def SortingbySelection(arr):

    newArr = []  # Initialize a new array to hold the sorted elements # Inicializa um novo array para guardaa os elementos ordenados 

    for i in range(len(arr)):            # Loop through the original array # Percorre o array original 
        smaller = MinorQuest(arr)        # Find the index of the smallest element # Encontra o indice do menor elemento
        newArr.append(arr.pop(smaller))  # Append the smallest element to the new array and remove it from the original array
    return newArr                        # Return the sorted array # Retorna o array ordenado

print(SortingbySelection([5, 3, 6, 2, 10]))  



