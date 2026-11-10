class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grid = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                value =  board[row][col]

                if value ==".":
                    continue
                box = (row//3*3) +col//3

                if value in rows[row] or value in cols[col] or value in grid[box]:
                    return False
                rows[row].add(value)
                cols[col].add(value)
                grid[box].add(value)
        return True
        