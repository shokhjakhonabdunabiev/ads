'''
Kadane's Algorithm

Finds the max sum subarray.
'''

# TC - O(n)
def kadanes(nums: list[int]) -> int:
    max_sum = nums[0]
    curr_sum = 0
    for n in nums:
        curr_sum = max(curr_sum, 0)
        curr_sum += n
        max_sum = max(max_sum, curr_sum)
    return max_sum


# Return the left and right index of the max subarray sum,
# assuming there's exactly one result (no ties).
# Sliding window variation of Kadane's: O(n)
def slidingWindow(nums: list[int]):
    max_sum = nums[0]
    curr_sum = 0
    
    max_l, max_r = 0, 0
    l = 0

    for r in range(len(nums)):
        if curr_sum < 0:
            curr_sum = 0
            l = r
        
        curr_sum += nums[r]
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_l, max_r = l, r
    
    return [max_l, max_r]