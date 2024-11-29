# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         n = len(nums)
#         low = 0
#         high = n-1
#         pivot = -1

#         while low < high:
#             mid = low + (high-low)//2 if pivot == -1 else mid

#             if nums[mid] == target:
#                 return mid
            
#             if pivot == -1:
#                 if nums[mid-1] > nums[mid]:
#                     pivot = mid
#                     low = pivot
#                     high = pivot - 1
#                     break
#                 if nums[mid] > nums[mid+1]:
#                     pivot = mid+1
#                     low = pivot + 1
#                     high = pivot

#                 if nums[mid] < target:
#                     low = mid + 1
#                 else:
#                     high = mid - 1

#         return nums[low] if nums[low] == target else -1


def search_in_rotated_array(arr, target):
    return 1

def binary_search(arr, l, r, target):
    while l <= r:
        mid = l + (r-l)//2
        print(arr[mid], l, r)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid-1


# def binary_search_rotated(arr,l,r,target):
#     while l <= r:
#         mid = l+(r-l)//2

#         # if mid is target, return
#         # if mid is pivot, compute k
#         # else, continue binary search
#         if arr[mid] == target:
#             return mid
#         elif (mid > 0 and arr[mid-1] < arr[mid]) and (mid < len(arr)-1 and arr[mid] > arr[mid+1]):
#             k = 1
#             break
#         elif arr[mid] < target:
#             l = mid + 1
#         else:
#             r = mid - 1
    
#     n = len(arr)
#     l = k+1
#     r = k



nums = [1,2,3,4,5,6,7,8,9]

print(binary_search(nums, 0, len(nums)-1, 7))


def binary_search_rotated(arr, l, r, target):
    n = len(arr)
    k = n-1
    for i in range(1, n):
        if arr[i-1] < arr[i] and (i<n-1 and arr[i] > arr[i+1]):
            k = i
            break

    l = (k+1) % n
    r = k

    while l!=r:
        mid = None 

