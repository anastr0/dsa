

def twosum(arr, target):
    # sorted arr
    i = 0
    j = len(arr) - 1

    while i<j:
        sum = arr[i] + arr[j]
        if sum == target:
            return True
        elif sum < target:
            i += 1
        else:
            j -= 1
    return False


def twosum_unsorted(arr, target):
    # unsorted arr

    arr.sort()
    i = 0
    j = len(arr) - 1

    while i<j:
        sum = arr[i] + arr[j]
        if sum == target:
            return True
        elif sum < target:
            i += 1
        else:
            j -= 1
    return False

arr = [10, 20, 35, 50] 
target=30

print(twosum(arr, target))


print(twosum_unsorted([10, 4, 2, 20, 56, 3], 0))

def pair_closest_to_zero(arr):
    arr.sort()

    i = 0
    j = len(arr)-1
    closest_sum = arr[0] + arr[-1]

    while i < j:
        sum = arr[i] + arr[j]
        if abs(sum) < abs(closest_sum):
            closest_sum = sum
        if abs(sum) == abs(closest_sum):
            closest_sum = abs(sum)
        if sum == 0:
            return 0
        elif sum < 0:
            i += 1
        else:
            j -= 1
    return closest_sum


print(pair_closest_to_zero([0, -8, -6, 3]))


def threesum(arr, target):
    arr.sort()
    n = len(arr)
    seen = {}

    for i in range(n):
        first = arr[i]
        diff = target - first

        if diff in seen:
            j, k = seen[diff]
            if i != j and i != k:
                print("YASS")
                return [first, arr[j], arr[k]]
        l = i
        r = n-1
        while l<r:
            s = arr[l]+arr[r]
            if s==diff:
                return [first, arr[l], arr[r]]
            if s < diff:
                l += 1
            else:
                r -= 1
            seen[s] = [l, r]
    return False

print(threesum([12, 3, 4, 1, 6, 9], 24))
arr = [2, 10, 12, 4, 8]
print(threesum(arr, 9))
arr = [1, 2, 3, 4, 5]
print(threesum(arr, 9))

def threesum_closest(arr, target):
    arr.sort()
    n = len(arr)
    closest_sum = float('inf')

    if len(arr) < 4:
        return sum(arr)

    for i in range(n):
        first = arr[i]
        diff = target - first

        l = i
        r = n-1
        while l<r:
            s = arr[l]+arr[r]
            if s==diff:
                print([first, arr[l], arr[r]])
                return target
            if s < diff:
                l += 1
            else:
                r -= 1

            total_sum = s+first
            if abs(closest_sum-target) > abs(total_sum-target):
                closest_sum = total_sum
            if abs(closest_sum-target) == abs(total_sum-target):
                closest_sum = max(closest_sum, total_sum)
    return closest_sum


nums = [-1,2,1,-4]
target = 1

print("\n\nthreesum_closest")
print(threesum_closest(nums, target))

nums = [0,0,0]
target = 1
print(threesum_closest(nums, target))
    