
# Page 59 from the book "Grokking Algorithms" by Aditya Bhargava
# Pagina 59 do livro "Entendendo Algoritmos" por Aditya Bhargava    

# Recursi Algotihm Implementation in Python
# Implementacao de Algoritmo Recursivo em Python
def SearchingFortheKey(main_box):
    key = main_box.create_one_kiy_for_searching() # Create a list to hold boxes to search

    while key:   # While there are boxes to search # Enquanto houver caixas para procurar 
        box = key.take_main() # Take the main box to search # Pega a caixa principal para procurar 
        for item in box:   # Loop through the item in the box # Percorre os itens na caixa
            if item.is_a_box():   # If the item is a box # Se o item for uma caixa
                key.append(item)  # Append the box to the list of boxes to search # Adiciona a caixa a lista de caixas para procurar
            elif item.is_a_key(): # If the item is a key # Se o item for uma chave
                return item       # Return the found key # Retorna a chave encontrada

# Recursive version of the Searching for the key algorithm
# Versao recursiva do algoritmo de Procurar a chave 
def SearchingFortheKeyRecursive(box):

    for item in box:   # Loop through the items in the box # Percorre os itens na caixa
        if item.is_a_box(): # If the item is a box # Se o item for uma caixa 
            SearchingFortheKeyRecursive(item) # Recursively search the box # Procura recursivamente na caixa
        elif item.is_a_key(): # If the item is a key # Se o item for uma chave
            print("Key found!") # Print key found message # Imprime a mensagem de chave encontrada
    