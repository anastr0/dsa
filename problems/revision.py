#merge sort
def merge(arr, l, m, r):
    temp = []
    i = l
    j = m+1

    while i<=m and j<=r:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    
    temp.extend(arr[i:m+1])
    temp.extend(arr[j:r+1])
    
    for k in range(len(temp)):
        arr[l+k] = temp[k]


def mergesort(arr, l, r):
    if l < r:
        m = l + (r-l)//2
        mergesort(arr, l, m)
        mergesort(arr, m+1, r)
        merge(arr, l, m, r)

print("Merge Sort")
arr = [4,2,7,1,0,9,2,2,1,0,0,10]
print(mergesort(arr, 0, len(arr)-1))
print(arr)

# quicksort
def partition(nums, low, high):
    pivot = nums[low]
    l = low + 1
    r = high
    # print('pivot=', pivot, 'l=', l, 'r=', r)
    while l <= r:
        if nums[l] > pivot > nums[r]:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        elif nums[l] <= pivot:
            l += 1
        elif nums[r] >= pivot:
            r -= 1
        # print(nums, l, r)
    nums[low], nums[r] = nums[r], nums[low]
    print(nums, r)
    return r

def qsort(nums, low, high):
    if low < high:
        pi = partition(nums, low, high)
        qsort(nums, low, pi - 1)
        qsort(nums, pi + 1, high)
    return nums

# heapsort

from heapq import heapify, heappop

def heapsort(nums):
    heapify(nums)
    op = []
    while nums:
        op.append(heappop(nums))
    return op

nums = [5,2,8,4,0,1,5,3,1,1,0,1,1,3,8]
print("Heapsort of nums: ", nums)
print(heapsort(nums))

# monotonic stack

def monotinic_stack_increasing(nums):

    stack = []

    for num in nums:

        while stack and stack[-1] > num:
            stack.pop()
        
        stack.append(num)
    return stack

nums = [3, 1, 4, 1, 5, 9, 2, 6]
         
print(monotinic_stack_increasing(nums))


def monotinic_stack_decreasing(nums):

    stack = []

    for num in nums:

        while stack and stack[-1] < num:
            stack.pop()
        
        stack.append(num)
    return stack

print(monotinic_stack_decreasing(nums))