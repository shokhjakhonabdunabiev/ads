'''
Implement insertion sort

Insertion sort is rly fast for:
 - nearly sorted arrays
 - short arrays
'''

# Time Complexity: O(n^2)
# Space Complexity: O(1)
def insertion_sort(arr: list) -> list:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j -= 1
        j += 1
        arr[j] = key
    return arr


if __name__ == "__main__":
    arr = [4,5,6,7,2,3,4,-1]
    print(insertion_sort(arr))
