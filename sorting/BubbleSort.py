'''
Bubble Sort is classic sorting for learning purposes.
'''
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def bubble_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    cnt = 0 # this is used to test how many times inner loop is run for already sorted arrays
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j+1]:
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        cnt += 1
        if not swapped:
            break
    return arr, cnt


if __name__ == "__main__":
    test_cases = [
        [],
        [42],
        [1, 2, 3, 4, 5, 6],
        [6, 5, 4, 3, 2, 1],
        [7, 7, 7, 7, 7],
        [4, 2, 7, 1, 5, 3, 6],
        [-3, -1, -7, 2, 5, 0],
        [3, 5, 2, 3, 8, 1, 5]
    ]

    for case in test_cases:
        res, cnt = bubble_sort(case)
        print(res, cnt)
