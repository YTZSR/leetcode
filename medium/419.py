class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ans = 0
        if len(board) == 0:
            return 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    ans += 1
                    if i - 1 >= 0 and board[i-1][j] == 'X':
                        ans -= 1
                    elif j - 1 >= 0 and board[i][j-1] == "X":
                        ans -= 1
        return ans
                        

                    