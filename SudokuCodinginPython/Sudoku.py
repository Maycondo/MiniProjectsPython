from typing import List

class Solution:
    "Solves the Sudoku puzzle by filling the empty cells."
    "Resolve o quebra-cabeça Sudoku preenchendo as celulas vazias."
    def solveSudoku(self, board: List[List[str]]) -> None:
        "Modifies board in-place to solve the Sudoku puzzle"
        "Modifica o tabuleiro no local para resolver o quebra-cabeça Sudoku"
        def is_valid(r , c , ch):
            "Checks if placing ch at board[r][c] is valid."
            "Verifica se colocar ch em board[r][c] e valido."
            for i in range(9):
                "Check row, column, and 3x3 sub-box."
                "Verifica linha, coluna e sub-caixa 3x3."
                if board[r][i] == ch or board[i][c] == ch:
                    return False 
                "Check 3x3 sub-box."
                "Verifica sub-caixa 3x3."
                if board[3 * (r // 3) + i // 3][3 * (c // 3) + i % 3] == ch:
                    return False
            "Returns True if placing ch is valid."
            "Retorna True se colocar ch for valido."
            return True
        
        "Backtracking function to fill the board."
        "Funcao de backtracking para preencher o tabuleiro."
        def backtrack():
            "Tries to fill the board using backtracking."
            "Tenta preencher o tabuleiro usando backtracking."
            for i in range(9):
                "Iterate through each cell in the board."
                "Itera por cada celula no tabuleiro."
                for j in range(9):
                    "Find an empty cell."
                    "Encontra uma celula vazia."
                    if board[i][j] == '.':
                        "Try placing digits 1-9 in the empty cell"
                        "Tenta colocar digitos 1-9 na celula vazia"
                        for ch in map(str, range(1, 10)):
                            "Check if placing ch is valid."
                            if is_valid(i, j, ch):
                                board[i][j] = ch
                                "Recursively try to fill the rest of the board."
                                "Recursivamente tenta preencher o resto do tabuleiro."
                                if backtrack():
                                    "Return True if the board is successfully filled."
                                    "Retorna True se o tabuleiro for preenchido com sucesso."
                                    return True
                                board[i][j] = '.'
                        "Return False if no valid digit can be placed."
                        "Retorna False se nenhum digito valido puder ser colocado."
                        return False
            "Return True if the entire board is filled."
            "Retorna True se o tabuleiro inteiro estiver preenchido."
            return True
        backtrack()
                            
