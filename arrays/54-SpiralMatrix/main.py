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

def spiralOrder2(matrix: list[list[int]]) -> int:
    if len(matrix) == 0:
        return []
    
    res = []
    rows, cols = len(matrix), len(matrix[0])
    direction = 1
    i, j = 0, -1

    while rows * cols > 0:
        for _ in range(cols):
            j += direction
            res.append(matrix[i][j])
        rows -= 1
        for _ in range(rows):
            i += direction
            res.append(matrix[i][j])
        cols -= 1
        direction *= -1
    return res

# Constrains mentions that -100 <= matrix[i][j] <= 100
# Space Complexity: might require additonal space to track visited elements,
# if we cant modift matrix in-place
def spiralOrder3(matrix: list[list[int]]) -> int:
    if len(matrix) == 0:
        return []
    res = []

    VISITED = 101
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    current_direction = 0
    change_direction = 0
    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, 0
    res.append(matrix[0][0])
    matrix[0][0] = VISITED

    while change_direction < 2:
        while True:
            next_row = row + directions[current_direction][0]
            next_col = col + directions[current_direction][1]

            if not (0 <= next_row < rows and 0 <= next_col < cols):
                break
            if matrix[next_row][next_col] == VISITED:
                break
            
            change_direction = 0
            row, col = next_row, next_col
            res.append(matrix[row][col])
            matrix[row][col] = VISITED
        
        current_direction = (current_direction + 1) % 4
        change_direction += 1
    return res

if __name__ == '__main__':
    test_cases = [
        [
            [1,2,3],
            [4,5,6],
            [7,8,9],
        ],
        [
            [1,2,3,4,5,6],
        ],
        []
    ]

    for i, test_case in enumerate(test_cases):
        res = spiralOrder3(test_case)
        print(f"Case {i + 1}:", res)

