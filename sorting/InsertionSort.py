"""
Implement insertion sort

Insertion sort is rly fast for:
 - nearly sorted arrays
 - short arrays
"""


def insertion_sort(nums: list[int]) -> None:
    """
    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key


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
        insertion_sort(actual)
        assert actual == expected, (
            f"insertion_sort({input}) returned {actual}, expected {expected}"
        )

    print("All tests passed!")
