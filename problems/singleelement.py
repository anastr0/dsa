
def get_single(nums: list[int]) -> int:

    n = len(nums)
    low = 0
    high = n - 1

    while low < high:
        mid = low + (high-low)//2
        if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
            return nums[mid]
        elif (mid%2==0 and nums[mid] == nums[mid-1]) or (mid%2!=0 and nums[mid] == nums[mid+1]):
            high = mid - 1
        elif (mid%2!=0 and nums[mid] == nums[mid-1]) or (mid%2==0 and nums[mid] == nums[mid+1]):
            low = mid + 1

    return nums[low]

nums = [1,1,2,3,3,4,4,8,8]
indx = [0,1,2,3,4,5,6,7,8]
low = 0
high = 3
mid = 1
print(nums)
print(get_single(nums))