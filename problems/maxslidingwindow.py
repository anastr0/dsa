def maxsliding(nums, k):
    maxs = []
    n = len(nums)
    if n < k:
        return max(nums)

    from heapq import heappush, heappop

    heap = []
    heappush(heap, -nums[0])
    l = 0
    r = 1

    while r < n:
        if r < k:
            heappush(heap, max(-heap[0], nums[r]))
            continue
        

        

    return maxs


nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(nums)
print(maxsliding(nums, k))

required_op = [3,3,5,5,6,7]
print(required_op)