"""
SelectionSort
"""


def selection_sort(nums: list[int]) -> None:
    """
    In-place sorting of the list. No extra memory is used.

    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    n = len(nums)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]


if __name__ == "__main__":
    nums = [3, 4, 9, 5, 7, 2, 1, 8, 6]
    selection_sort(nums)
    print(nums)

    nums = [-3, -4, 9, -5, 7, -2, 1, 8, 6]
    selection_sort(nums)
    print(nums)
