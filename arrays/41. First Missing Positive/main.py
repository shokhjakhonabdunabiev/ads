'''
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Constraints:
    1 <= nums.length <= 105
    -2^31 <= nums[i] <= 2^31 - 1

    
Some questions that can be asked:
    - Can array contain duplicates?
    - Can we modify array in-place?
    - Can array be empty?
    - Does array contain negative numbers?
'''
# Time Complexity - O(n)
# Space Complexity - O(n)
def firstMissingPositive(nums: list[int]) -> int:
    n = len(nums)
    seen = [False] * (n + 1)

    for num in nums:
        if 0 < num <= n:
            seen[num] = True
    
    for i in range(1, n + 1):
        if not seen[i]:
            return i
    
    return n + 1

# Time Complexity - O(n)
# Space Complexity - O(1)
def firstMissingPositive1(nums: list[int]):
    n = len(nums)
    i = 0
    while i < n:
        correct_index = nums[i] - 1
        if 0 < nums[i] <= n and nums[i] != nums[correct_index]:
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            i += 1
    
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1


if __name__ == "__main__":
    test_cases = [
        [1,2,0],
        [3,4,-1,1],
        [7,8,9,11,12],
        [-5],
    ]

    for test_case in test_cases:
        res = firstMissingPositive1(test_case)
        print(res)
