def partition(nums, left, right):
    pivot = nums[left]
    l = left + 1
    r = right

    while l <= r:
        if nums[l] < pivot < nums[r]:
            nums[l], nums[r] = nums[r], nums[l]
        elif nums[l] >= pivot:
            l += 1
        elif nums[r] <= pivot:
            r += 1
    nums[left], nums[r] = nums[r], nums[left]
    return r

def quicksort(nums):
    left = 0
    right = len(nums) - 1
    idx = 0

    # while True:
    #     idx = partition(nums, left, right)
    #     if idx == 0:
    #         break
    #     elif idx > 0:
    #         right = idx - 1
    #     elif idx < 0:
    #         left = idx + 1
    while True:
        idx = partition(nums, left, right)
        if idx == len(nums)-1:
            break
        elif idx < len(nums)-1:
            left = idx + 1
        elif idx > len(nums)-1:
            right = idx - 1
    return nums

nums = [1, 2, 3, 4, 5, 6, 7]
# print(quicksort(nums))



################################
# recursive
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

def partition1(nums, low, high):
    pivot = nums[low]
    l = low + 1
    k = high 
    for i in range(high, low, -1):
        if nums[i] > pivot:
            nums[k], nums[i] = nums[k], nums[i]
            k -= 1
    nums[low], nums[k] = nums[k], nums[low]
    print(nums, k)
    return k

def qsort(nums, low, high):
    if low < high:
        pi = partition(nums, low, high)
        qsort(nums, low, pi - 1)
        qsort(nums, pi + 1, high)
    return nums

def qsort1(nums, low, high):
    if low < high:
        pi = partition1(nums, low, high)
        qsort(nums, low, pi - 1)
        qsort(nums, pi + 1, high)
    return nums

nums = [4,2,7,3,6,1,0,5,3]
# nums = [1,2,3,4,5,6,7,8,9]
# nums = [9,8,7,6,5,4,3,2,1]
# nums = [3,2,1,5,6,4]
print(qsort(nums, 0, len(nums)-1))
print("\n\n")
nums = [4,2,7,3,6,1,0,5,3]

print(qsort1(nums, 0, len(nums)-1))