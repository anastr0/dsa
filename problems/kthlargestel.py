def partition(nums, left, right, count):
    pivot = nums[left]
    l = left + 1
    r = right 

    print("Partition started with pivot, l, r", pivot, l, r, nums)
    while l<=r:
        if nums[l] < pivot < nums[r]:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        elif nums[l] >= pivot:
            l += 1
        elif nums[r] <= pivot:
            r -= 1
        count += 1

        print(nums)

    print("partition ended", nums)
    nums[left], nums[r] = nums[r], nums[left]
    print("swap after partition", nums)
    print("returning idx (r)", r)
    return r, count

def kthlargest(nums: list[int], k: int) -> int:
    left = 0
    right = len(nums)-1
    kth = 0
    count = 0

    while True:
        idx, count = partition(nums, left, right, count)
        if idx == k-1:
            print("YESS")
            kth = nums[idx]
            break
        elif idx < k-1:
            left = idx + 1
        elif idx > k-1:
            right = idx - 1
        print(idx, nums)
        count += 1
    print(count)
    return kth 

# nums = [3,2,1,5,6,4]
nums = [8, 7, 6, 5, 4, 3, 2, 1]
# nums = [1, 2, 3, 4, 5, 6, 7, 8]
k = 2
print(kthlargest(nums, k))