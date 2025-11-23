import math

# Time Complexity: O(sqrt(N))
# Space Complexity: O(1)
def jump_search(arr, target):
    n = len(arr)
    jump_by = math.floor(math.sqrt(n))
    i = jump_by
    while i < n and arr[i] <= target:
        i += jump_by
    
    start = max(0, i - jump_by)
    end = min(i, n)
    for j in range(start, end):
        if arr[j] == target:
            return j
        
    return None

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
        res = jump_search(*case)
        print(res)
