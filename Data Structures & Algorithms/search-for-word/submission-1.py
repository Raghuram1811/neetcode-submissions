class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def backtrack(row, col, curr_str):

            if curr_str == word:
                return True
            
            if row<0 or row >=len(board) or col < 0 or col >= len(board[row]):
                return False

            if len(curr_str) >= len(word):
                return False
            
            if board[row][col] != word[len(curr_str)]:
                return False
            
            curr_char = board[row][col]
            board[row][col] = "$"

            res = (backtrack(row+1, col, curr_str+curr_char) or
                backtrack(row-1, col, curr_str+curr_char) or 
                backtrack(row, col+1, curr_str+curr_char) or 
                backtrack(row, col-1, curr_str+curr_char))

            board[row][col] = curr_char

            return res

        for row in range(len(board)):
            for col in range(len(board[row])):
                if backtrack(row, col, ""):
                    return True
        
        return False