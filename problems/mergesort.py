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







# def merge(arr, l, m, r): # l=0, m=0, r=1
#     i = l
#     j = m+1

#     temp_arr = []

#     while i <= m and j <= r:  # i=0, j=1
#         if arr[i] < arr[j]:
#             temp_arr.append(arr[i])
#             i += 1
#         else:
#             temp_arr.append(arr[j])
#             j += 1
    
#     while j <= r:
#         temp_arr.append(arr[j])
#         j += 1
#     while i <= m:
#         temp_arr.append(arr[i])
#         i += 1
#     # print(temp_arr)
#     for x in range(len(temp_arr)):
#         arr[l+x] = temp_arr[x]
#     print(l, m, r, arr[l:r+1])

def mergesort_mergeintervals(arr, l, r):
    if l < r:
        m = l + (r-l)//2
        # print(l, m, r)
        mergesort_mergeintervals(arr, l, m)
        mergesort_mergeintervals(arr, m+1, r)
        merge_intervals(arr, l, m, r)

def merge_intervals(arr, l, m, r):
    i = l
    j = m+1

    temp_err = []
    print(arr[l:r+1])
    while i<=m and j<=r:
        a,b = arr[i]
        c,d = arr[j]
        if a <= c <= b:
            temp_err.append([a, max(b,d)])
            i+=1
            j+=1
        elif c <= a <= b:
            temp_err.append([c, max(b,d)])
            i+=1
            j+=1
        elif a<c:
            temp_err.append([a,b])
            i += 1
        else:
            temp_err.append([c,d])
            j += 1

    while i<=m:
        temp_err.append(arr[i])
        i += 1
    while j<=r:
        temp_err.append(arr[j])
        j += 1

    for x in range(len(temp_err)):
        arr[l+x] = temp_err[x]
    
    for y in range(len(temp_err)+l, r+1):
        arr[y] = [-1, -1]

    print(l, m, r, 'temp_arr', temp_err)
    print("\n")

if __name__=="__main__":
    # arr = [3,6,2,8,5,3,9,10,0,3,6]
    # arr = [[1,3],[2,6],[8,10],[15,18]]
    arr= [[2,3],[4,5],[6,7],[8,9],[1,10]]
    #arr = [12, 11, 13, 5, 6, 7]
    print(arr)
    print("\n\n")
    mergesort_mergeintervals(arr, 0, len(arr)-1)

    print([i for i in arr if i!=float('inf')])

    arr = [4,2,7,1,0,9,2,2,1,0,0,10]
    print(mergesort(arr, 0, len(arr)-1))
    print(arr)


