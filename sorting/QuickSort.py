"""
Implement QuickSort:
    quicksort consists of two parts, partitioning and recursing two halfs

    recursion:
        1. stop on base case where l >= r
        2. get pivotIndex using partition function
        3. call recursion on arr [l:pivotIdx - 1]
        3. call recursion on arr [pivotidx+1, r]
        4. return arr

    partitioning:
        1. pick a pivot (usually last element of array)
        2. init idx to l - 1
        2. go through all elements with two pointers [l, r)
            2.1 when we find element less or equal to pivot
                2.1.1 increment idx
                2.1.2 swap cur element with element at idx
        3. swap pivot with final idx
"""


def quick_sort(nums: list[int]) -> None:
    """
    In-place quick sort. No extra memory is used.

    Time complexity: O(n*log(n))
    Space complexity: O(1)
    """

    def partition(low: int, high: int) -> int:
        pivot = nums[high]
        i = low - 1
        for j in range(low, high):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1

    def sort(low: int, high: int) -> None:
        if low >= high:
            return
        pivot_idx = partition(low, high)
        sort(low, pivot_idx - 1)
        sort(pivot_idx + 1, high)

    sort(0, len(nums) - 1)


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
        quick_sort(actual)
        assert actual == expected, (
            f"quick_sort({input}) returned {actual}, expected {expected}"
        )

    print("All tests passed!")
