'''
CountingSort
'''

# TC: O(n + k)
def counting_sort(nums: list[int]) -> list[int]:
    k = max(nums)
    counts = [0] * (k + 1)
    for num in nums:
        counts[num] += 1

    start_idx = 0
    for i, cnt in enumerate(counts):
        counts[i] = start_idx
        start_idx += cnt
    
    sorted_nums = [0] * len(nums)

    for num in nums:
        sorted_nums[counts[num]] = num
        counts[num] += 1
    
    for i in range(len(nums)):
        nums[i] = sorted_nums[i]
    
    return nums


def counting_sort_optimized(lst: list[int]) -> None:
    """
    Sorts a list of integers (handles shifting of integers to range 0 to K)
    """
    shift = min(lst)
    K = max(lst) - shift
    counts = [0] * (K + 1)
    for elem in lst:
        counts[elem - shift] += 1

    # we now overwrite our original counts with the starting index
    # of each element in the final sorted array
    starting_index = 0
    for i, count in enumerate(counts):
        counts[i] = starting_index
        starting_index += count

    sorted_lst = [0] * len(lst)
    for elem in lst:
        sorted_lst[counts[elem - shift]] = elem
        # since we have placed an item in index counts[elem], we need to
        # increment counts[elem] index by 1 so the next duplicate element
        # is placed in appropriate index
        counts[elem - shift] += 1

    # common practice to copy over sorted list into original lst
    # it's fine to just return the sorted_lst at this point as well
    for i in range(len(lst)):
        lst[i] = sorted_lst[i]
    return lst

def counting_sort(arr: list[int]) -> list[int]:
    if not arr:
        return arr
        
    min_num = min(arr)
    max_num = max(arr)
    count = [0] * (max_num - min_num + 1)
    
    shift = -min_num
    for num in arr:
        count[num + shift] += 1
    
    i = 0
    for num, cnt in enumerate(count):
        for _ in range(cnt):
            arr[i] = num - shift
            i += 1
    
    return arr

if __name__ == "__main__":
    nums = [3,4,9,5,7,2,1,8,6]
    print(counting_sort(nums))