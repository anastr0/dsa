# https://leetcode.com/problems/longest-common-subsequence/description/

# def possible_subsequences(arr, idx, subarr, all):
#     print(f"\n\nrecurr: arr: {arr}\nidx:{idx}\nsubarr:{subarr}\nall:{all}")
#     if idx == len(arr):
#         if len(subarr) != 0:
#             all.append(subarr)
#     else:
#         print(f"without arr[{idx}]: {arr[idx]}")
#         possible_subsequences(arr, idx+1, subarr, all)
#         print(f"without arr[{idx}]: {arr[idx]}")
#         possible_subsequences(arr, idx+1, subarr+[arr[idx]], all)
#     print("recurr end, all: ", all)
#     return all

# arr = [1, 2, 3]
# print(possible_subsequences(arr, 0, [], []))


def lis(arr):
    n = len(arr)

    LIS_of = [1]*n
    


