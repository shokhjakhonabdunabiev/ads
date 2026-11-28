"""
Binary search works for already sorted arrays.
"""


def binary_search(arr: list[int], target: int) -> int | None:
    """
    Time complexity: O(log(n))
    Space complexity: O(1)
    """
    l, r = 0, len(arr) - 1
    while l <= r:
        m = l + (r - l) // 2
        if arr[m] > target:
            r -= 1
        elif arr[m] < target:
            l += 1
        else:
            return m
    return None


# Remember about base case in recursion!
def binary_search_recursive(arr: list[int], target: int) -> int | None:
    def dfs(l, r):
        if l > r:
            return None
        m = l + (r - l) // 2
        if arr[m] > target:
            return dfs(l, m - 1)
        elif arr[m] < target:
            return dfs(m + 1, r)
        return m

    return dfs(0, len(arr) - 1)


if __name__ == "__main__":
    test_cases = [
        ([2, 3, 7, 8, 9], 7, 2),
        ([1, 4, 5], 5, 2),
        ([10, 20, 30, 40], 40, 3),
        ([2, 4, 4, 4, 9], 4, 2),
        ([1, 3, 5, 7], 2, None),
        ([], 123, None),
        ([123], 123, 0),
    ]

    for *input, expected in test_cases:
        actual = binary_search_recursive(*input)
        assert actual == expected, (
            f"binary_search_recursive({input}) returned {actual}, expected {expected}"
        )

    print("All tests passed!")
