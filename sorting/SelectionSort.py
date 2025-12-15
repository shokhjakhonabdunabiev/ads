'''
SelectionSort
'''

# TC - O(n^2)
def selection_sort(nums: list[int]) -> list[int]:
    n = len(nums)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums


if __name__ == "__main__":
    nums = [3,4,9,5,7,2,1,8,6]
    print(selection_sort(nums))