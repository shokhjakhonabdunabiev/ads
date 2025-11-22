'''
Given an m x n matrix, return all elements of the matrix in spiral order.

Questions to ask:
    - Can matrix be empty? If yes think about empty matrix case (cols should be 0 not len(matrix[0]))

Sample input:
    Case 1:
        [
          col --> cols
            [1,2,3], row
            [4,5,6], ↓
            [7,8,9], rows
        ]

    Case 2:
        [
            [1,2,3,4,5,6],
        ]

    Case 3:
        []
'''

# Time complexity - O(m*n), where m is the length of rows, n - the length of columns
# Space complexity - O(1), if output array is not considered
def spiralOrder(matrix: list[list[int]]) -> list[int]:
    if len(matrix) == 0:
        return []
    
    res = []
    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, 0

    while row < rows and col < cols:
        for c in range(col, cols):
            res.append(matrix[row][c])
        row += 1

        for r in range(row, rows):
            res.append(matrix[r][cols - 1])
        cols -= 1

        if row >= rows or col >= cols:
            break

        for c in range(cols - 1, col - 1, -1):
            res.append(matrix[rows - 1][c])
        rows -= 1

        for r in range(rows - 1, row - 1, -1):
            res.append(matrix[r][col])
        col += 1

    return res

if __name__ == '__main__':
    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
    ]

    res = spiralOrder(matrix)
    print(res)
