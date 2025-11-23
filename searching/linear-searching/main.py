'''
Given array and target element to search in array, return index of the element.
If element is not in array, return None
'''
# Time Complexity: O(n)
# Space Complexity: O(1)
def liner_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i
    return None

if __name__ == "__main__":
    test_cases = [
        ([3,8,2,7,9], 7),
        ([5,1,4], 5),
        ([10,20,30,40], 40),
        ([2, 4, 4, 4, 9], 4),
        ([1, 3, 5, 7], 2),
        ([], 123)
    ]

    for test_case in test_cases:
        res = liner_search(*test_case)
        print(res)