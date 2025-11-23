'''
Binary search works for already sorted arrays.
'''
# Time Complexity: O(log(n))
# Space Complexity: O(1)
def binary_search(arr, target):
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
def binary_search_recursive(arr, target):
    def dfs(l, r):
        if l > r:
            return None
        m = l + (r - l) // 2
        if arr[m] > target:
            return dfs(l, m-1)
        elif arr[m] < target:
            return dfs(m+1, r)
        return m

    return dfs(0, len(arr) - 1)


if __name__ == "__main__":
    test_cases = [
        ([2,3,7,8,9], 7),
        ([1,4,5], 5),
        ([10,20,30,40], 40),
        ([2,4,4,4,9], 4),
        ([1,3,5,7], 2),
        ([], 123),
        ([123], 123),
    ]

    for case in test_cases:
        res = binary_search_recursive(*case)
        print(res)
