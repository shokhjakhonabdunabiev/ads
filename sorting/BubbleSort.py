"""
Bubble Sort is classic sorting for learning purposes.
"""


def bubble_sort(nums: list[int]) -> int:
    """
    In-place sorting of the array. No extra space is used.

    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    n = len(nums)
    cnt = 0  # track how many times inner loop is run
    for i in range(n):
        has_swapped = False
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                has_swapped = True
        cnt += 1
        if not has_swapped:
            break
    return cnt


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
        inner_loop_cnt = bubble_sort(actual)
        assert actual == expected, (
            f"bubble_sort({input}) returned {actual}, expected {expected}"
        )
        print(f"Inner loop count for input {input} is {inner_loop_cnt}")

    print("All tests passed!")
