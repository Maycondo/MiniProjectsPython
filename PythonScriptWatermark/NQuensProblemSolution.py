from typing import List

# Solves the N-Queens problem by placing N queens on an N x N chessboard.
# Resolve o problema das N-Rainhas colocando N rainhas em um tabuleiro de xadrez n * n
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = [] # List to store the valid board configurations. # Lista para armazenar as configuracoes validas do tabuleiro.
        board = [['.' for _ in range(n)] for _ in range(n)] # Initialize an n x n board with '.' representing empty cells. 
        # Inicializa um tabuleiro n * n com '.' representando celulas vazias.

        # Function to check if placing a queen at (row, col) is valid.
        # Funcao para verificar se colocar uma rainha em (linha, coluna) e valido 
        def is_valid(row, col):
            for i in range(row):          # Check the same column. # Verifica a mesma coluna.
                if board[i][col] == 'Q':  # Checks for another queen in the same column. # Verifica se ha outra rainha na mesma coluna.
                    return False          # Return False if a queen is found. # Retorna False se uma rainha for encontrada.
                
            i, j = row - 1, col - 1  # Check the upper-left diagonal. # Verifica a diagonal superior esquerda.

            while i >= 0 and j >= 0:      # Iterate through the diagonal cells. # Itera pelas celulas diagonais.
                if board[i][j] == 'Q':    # Checks for another queen in the diagonal. # Verifica se ha outra rainha na diagonal.
                    return False          # Return False if a queen is found. # Retorna False se uma rainha for encontrada.
                i -= 1
                j -= 1

            i, j = row - 1, col + 1  # Check the upper-right diagonal. # Verifica a diagonal superior direita.

            while i >= 0 and j < n:      # Iterate through the diagonal cells. # Itera pelas celulas diagonais.
                if board[i][j] == 'Q':   # Checks for another queen in the diagonal. # Verifica se ha outra rainha na diagonal.
                    return False         # Return False if a queen is found. # Retorna False se uma rainha for encontrada.
                i -= 1
                j += 1
            return True  # Return True if placing the queen is valid. # Retorna True se colocar a rainha for valido.
           
        def backtrack(row): # Backtracking function to place queens row by row. # Funcao de backtracking para colocar rainhas linha por linha.
            if row == n:                                 # All queens are placed successfully. # Todas as rainas foram colocadas com sucesso.
                res.append([''.join(r) for r in board])  # Add the current board configuration to the result list. # Adiciona a configuracao atual do tabuleiro a lista de resultados.
                return 
            for col in range(n):           # Iterate through each column in the current row. # Itera por cada coluna na linha atual.
                if is_valid(row, col):     # Check if placing a queen at (row, col) is valid. # Verifica se colocar uma rainha em (linha, coluna)
                    board[row][col] = 'Q'  # Place the queen at (row, col). # Coloca a rainha em (linha, coluna).
                    backtrack(row + 1)     # Recursively try to place queens in the next row. # Recursivamente tenta colocar rainhas na proxima linha.
                    board[row][col] = '.' # Remove the queen (backtrack). # Remove a rainha (backtrack).
        backtrack(0) # Start the backtracking process from the first row. # Inicia o processo de backtracking a partir da primeira linha.   
        return res # Return the list of valid board configurations. # Retorna a lista de configuracoes validas do tabuleiro.
    