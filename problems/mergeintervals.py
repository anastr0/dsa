def merge(arr1: list[list[int]], arr2: list[list[int]]) -> list[list[int]]:
    n1 = len(arr1)
    n2 = len(arr2)
    i = j = 0
    merged_arr = []
    while i<n1 and j<n2:
        a, b = arr1[i]
        c, d = arr2[j]
        s, e = merged_arr[-1] if merged_arr else [-1, -1]

        if s <= a <= e:
            print("comparing overlap with merged_last", 'arrl', arr1[i], 'merged_last', merged_arr[-1], 'merged_interval[-1]' , [s, max(b, e)])
            merged_arr[-1] = [s, max(b, e)]
            i += 1
        elif s <= c <= e:
            print("comparing overlap with merged_last", 'arrr', arr2[j], 'merged_last', merged_arr[-1], 'merged_interval[-1]' , [s, max(d, e)])
            merged_arr[-1] = [s, max(d, e)]
            j += 1
        elif a <= c <= b:
            print("comparing overlap", 'arrl', arr1[i], 'arrr', arr2[j], 'interval added', [a, max(b, d)])
            merged_arr.append([a, max(b, d)])
            i += 1
            j += 1
        elif c <= a <= d:
            print("comparing overlap", 'arrr', arr2[j], 'arrl', arr1[i], 'interval added', [c, max(b, d)])
            merged_arr.append([c, max(b, d)])
            j += 1
            i += 1
        elif a < c:
            print("comparing sort", 'arrl', arr1[i], 'arrr', arr2[j], 'interval added', [a, b])
            merged_arr.append([a, b])
            i += 1
        else:
            print("comparing sort", 'arrr', arr2[j], 'arrl', arr1[i], 'interval added', [c, d])
            merged_arr.append([c, d])
            j += 1

    while i < n1:
        a, b = arr1[i]
        s, e = merged_arr[-1]
        if s <= a <= e:
            merged_arr[-1] = [s, max(b, e)]
        else:
            merged_arr.append([a, b])
        i += 1

    while j < n2:
        c, d = arr2[j]
        s, e = merged_arr[-1]
        if s <= c <= e:
            merged_arr[-1] = [s, max(d, e)]
        else:
            merged_arr.append([c, d])
        j += 1

    print("merged arr", merged_arr)
    return merged_arr

def mergesort(arr: list[list[int]]) -> list[list[int]]:
    n = len(arr)
    if n <= 1:
        return arr

    m = n // 2
    arrl = mergesort(arr[:m])
    arrr = mergesort(arr[m:])
    print("\n")
    print(n, m, 'arr1', arrl, 'arr2', arrr)
    return merge(arrl, arrr)

def merge_intervals(arr):
    merged_arr = []

    arr.sort() # O(nlogn)

    for i in arr:
        start, end = merged_arr[-1] if merged_arr else [-1, -1]

        if start <= i[0] <= end:
            merged_arr[-1] = [start, max(i[1], end)]
        else:
            merged_arr.append(i)
    return merged_arr


if __name__=="__main__":
    # arr= [[2,3],[4,5],[6,7],[8,9],[1,10]]
    # arr = [[1,3],[2,6],[8,10],[15,18]]
    # arr = [[1,4],[0,2],[3,5]]
    arr = [[2,3],[5,5],[2,2],[3,4],[3,4]]
    print(arr)
    print("\n\n")


    # sorted_arr = mergesort(arr)

    opt_arr = merge_intervals(arr)
    # print(sorted_arr)

    print(opt_arr)