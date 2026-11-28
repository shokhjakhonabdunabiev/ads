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
    test_cases = [
        ([], []),
        ([42], [42]),
        ([1, 2, 4, 3, 5, 6], [1, 2, 3, 4, 5, 6]),
        ([6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6]),
        ([7, 7, 7, 7, 7], [7, 7, 7, 7, 7]),
        ([4, 2, 7, 1, 5, 3, 6], [1, 2, 3, 4, 5, 6, 7]),
        ([-3, -1, -7, 2, 5, 0], [-7, -3, -1, 0, 2, 5]),
        ([3, 5, 2, 3, 8, 1, 5], [1, 2, 3, 3, 5, 5, 8]),
    ]

    for input, expected in test_cases:
        actual = (
            input.copy()
        )  # copy of the input, for error message, since the input is sorted in-place
        selection_sort(actual)
        assert actual == expected, (
            f"selection_sort({input}) returned {actual}, expected {expected}"
        )

    print("All tests passed!")
