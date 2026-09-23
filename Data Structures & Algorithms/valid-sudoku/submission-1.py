class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        col_hm = [[0] * 10 for _ in range(10)]
        sq_hm = [[[0] * 10 for _ in range(3)] for _ in range(3)]


        for i in range(9):
            
            row_hm = [0] * 10

            for j in range(9):

                
                
                if board[i][j] == ".":
                    continue
                else:
                    n = int(board[i][j])

                # Comprobacion por filas
                if row_hm[n] == 1:
                    return False
                else:
                    row_hm[n] = 1

                # comprobacion por columnas
                if col_hm[j][n] == 1:
                    return False
                else:
                    col_hm[j][n] = 1

                # Comprobacion por cuadrados
                if sq_hm[i // 3][j // 3][n] == 1:
                    return False
                else:
                    sq_hm[i // 3][j // 3][n] = 1

        return True