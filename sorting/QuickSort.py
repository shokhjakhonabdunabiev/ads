'''
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
'''

# Time Complexity: O(n*log(n))
# Space Complexity: O(1)
def quick_sort(arr: list) -> list:
    def qs(arr: list, l: int, r: int):
        if l >= r:
            return

        pivotIdx = partition(arr, l, r)
        qs(arr, l, pivotIdx - 1)
        qs(arr, pivotIdx + 1, r)

    qs(arr, 0, len(arr) - 1)
    return arr

def partition(arr: list, l: int, r: int) -> int:
    pivot = arr[r]
    idx = l - 1

    for i in range(l, r):
        if arr[i] <= pivot:
            idx += 1
            arr[i], arr[idx] = arr[idx], arr[i]
    
    idx += 1
    arr[r], arr[idx] = arr[idx], pivot
    return idx


if __name__ == "__main__":
    arr = [4,5,6,7,2,3,4,-1]
    print(quick_sort(arr))