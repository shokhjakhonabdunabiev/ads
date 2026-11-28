# def bucket_sort(self, lst: list[int], K) -> None:
#     """
#     Sorts a list of integers using K buckets
#
#     Time complexity: O(n)
#     Space complexity: O(n + k), where k is the number of buckets
#     """
#     buckets = [[] for _ in range(K)]
#
#     # place elements into buckets
#     shift = min(lst)
#     max_val = max(lst) - shift
#     bucket_size = max(1, max_val / K)
#     for i, elem in enumerate(lst):
#         # same as K * lst[i] / max(lst)
#         index = (elem - shift) // bucket_size
#         # edge case for max value
#         if index == K:
#             # put the max value in the last bucket
#             buckets[K - 1].append(elem)
#         else:
#             buckets[index].append(elem)
#
#     # sort individual buckets
#     for bucket in buckets:
#         bucket.sort()
#
#     # convert sorted buckets into final output
#     sorted_array = []
#     for bucket in buckets:
#         sorted_array.extend(bucket)
#
#     # common practice to mutate original array with sorted elements
#     # perfectly fine to just return sorted_array instead
#     for i in range(len(lst)):
#         lst[i] = sorted_array[i]


def bucket_sort(nums: list[int]) -> list[int]:
    if not nums:
        return nums

    max_val, min_val = max(nums), min(nums)

    bucket_range = (max_val - min_val) / len(nums)
    buckets = [[] for _ in range(len(nums) + 1)]

    for i in nums:
        if i == max_val:
            bucket_idx = len(nums) - 1
        else:
            bucket_idx = int((i - min_val) / bucket_range)
        buckets[bucket_idx].append(i)

    for bucket in buckets:
        bucket.sort()

    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result


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
        actual = bucket_sort(input)
        assert actual == expected, (
            f"bucket_sort({input}) returned {actual}, expected {expected}"
        )

    print("All tests passed!")
