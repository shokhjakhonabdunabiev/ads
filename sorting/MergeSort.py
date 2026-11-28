"""
Merge Sort
"""


def merge_sort(nums: list[int]) -> list[int]:
    """
    Time complexity: O(n*log(n))
    Space complexity: O(n)
    """
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)


def merge(left: list[int], right: list[int]) -> list[int]:
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


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
        actual = merge_sort(input)
        assert actual == expected, (
            f"merge_sort({input}) returned {actual}, expected {expected}"
        )

    print("All tests passed!")
