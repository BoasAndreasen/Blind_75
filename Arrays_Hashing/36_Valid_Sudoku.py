class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Row
        for i in range(len(board)):
            s = set()
            l = []
            for j in range(len(board[i])):
                if board[i][j] != '.':
                    s.add(board[i][j])
                    l.append(board[i][j])
            if len(s) != len(l):
                return False

        # Column
        for i in range(len(board)):
            s = set()
            l = []
            for j in range(len(board[i])):
                if board[j][i] != '.':
                    l.append(board[j][i])
                    s.add(board[j][i])
            if len(s) != len(l):
                return False

        # Grid
        for i in range(1, len(board), 3):
            for j in range(1, len(board), 3):
                s = set()
                l1 = []
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if board[i - k][j + l] != '.':
                            l1.append(board[i + k][j + l])
                            s.add(board[i - k][j + l])

                if len(s) != len(l1):
                    return False
                
        return True
