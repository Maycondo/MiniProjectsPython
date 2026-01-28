
# Page 27 from the book "Grokking Algorithms" by Aditya Bhargava 
# Pagina 27 do livro "Entendendo Algoritmos" por Aditya Bhargava

# Binary Search Implementation in Python # Pequisa Binaria implementacao em Python
def BinarySearch(list, item):
    low = 0                 # Initialize the low poiter # Inicializa o ponteiro baixo
    high = len(list) - 1    # Initialize the high pointer # Inicializa o ponteiro alto 

    while low <= high:      # While the low pointer is less than or equal to the high pointer 
        #                   # Enquanto o ponteiro baixo for menor ou igual ao ponteiro alto 

        mid = (low + high) // 2 # Calculate the mid index # Calcula o indice do meio 
        guess = list[mid]       # Get the middle element # Pega o elemento do meio

        if guess == item:       # If the middle element is the target item # Se o elemento do meio for o item alvo
            return mid          # Return the index of the found item # Retorna o indice do item encontrado 
        
        if guess > item:        # If the middle element is greater than the target item # Se o elemento do meio for maior que o item alvo
            high = mid - 1      # Move the high pointer to mid - 1 # Move o ponteiro alto para mid - 1

        else:                   # If the middle element is less than the target item # Se o elemento do meio for menor que o item alvo 
            low = mid + 1
    return None                 # Return None if the item is not found # Retorna None se o item nao for encontrado


my_list = [1, 3, 5, 7, 9]
print(BinarySearch(my_list, 3))  # Output: 1print(BinarySearch(my_list, -1)) # Output: Nonefrom typing import List  
print(BinarySearch(my_list, -1)) # Output: None