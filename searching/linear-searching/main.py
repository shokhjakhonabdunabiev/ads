"""
Given array and target element to search in array, return index of the element.
If element is not in array, return None
"""


def liner_search(arr: list[int], target: int) -> int | None:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    for i, element in enumerate(arr):
        if element == target:
            return i
    return None


if __name__ == "__main__":
    test_cases = [
        ([2, 3, 7, 8, 9], 7, 2),
        ([1, 4, 5], 5, 2),
        ([10, 20, 30, 40], 40, 3),
        ([2, 4, 4, 4, 9], 4, 1),
        ([1, 3, 5, 7], 2, None),
        ([], 123, None),
        ([123], 123, 0),
    ]

    for *input, expected in test_cases:
        actual = liner_search(*input)
        assert actual == expected, (
            f"liner_search({input}) returned {actual}, expected {expected}"
        )

    print("All tests passed!")
