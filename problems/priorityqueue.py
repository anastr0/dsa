# def min_platforms(arr, dep):
#     if len(arr) == 0:
#         return 0

#     plat_count = 1
#     plat_schedule = {0: dep[0]}

#     for i in range(1, len(arr)):
#         vacant_plat_found = False
#         print('plat_no', plat_schedule)
#         for plat_no in range(plat_count):
#             if plat_schedule[plat_no] < arr[i]:
#                 plat_schedule[plat_no] = dep[i]
#                 vacant_plat_found = True
#                 break
        
#         if not vacant_plat_found:
#             plat_count += 1
#             plat_schedule[plat_count-1] = dep[i]

#     return plat_count


from heapq import heapify, heappop, heappush

def min_platforms(arr, dep):
    min_platforms = 0
    timings = [(a, d) for a, d in zip(arr, dep)]  # space O(n)
    timings.sort() 

    pq = []
    for timing in timings:
        start, end = timing
        while pq and pq[0][1] <= start:
            heappop(pq)
        heappush(pq, timing)
        min_platforms = max(min_platforms, len(pq))
    return min_platforms

arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

print(arr)
print(dep)
print(min_platforms(arr, dep))


def min_rooms(meetings):
    print("Min rooms required for meetings: ", meetings)
    minrooms = 0
    meetings.sort()  # O(nlogn)

    pq = []
    for meeting in meetings:
        start, end  = meeting
        if pq and start >= pq[0][1]:
            heappop(pq)
        heappush(pq, meeting)
        minrooms = max(minrooms, len(pq))
    return minrooms


print(min_rooms([[1,4], [2,5], [7,9]]))

# CPU schedule - single threaded

# def cpu_schedule(tasks):
#     print("\n\nCPU schedule for tasks:", tasks)
#     schedule = []
#     pq = []
#     tasks.sort()
#     i = 0
#     test = []
#     for task in tasks:
#         enq, proc = task
#         while pq and pq[0][2] <= enq:
#             prio = heappop(pq)
#             schedule.append(prio[1])
#         heappush(pq, (proc, i, (enq+proc-1)))
      
#         i += 1
#     while pq:
#         prio = heappop(pq)
#         schedule.append(prio[1])
#     return schedule



def cpu_schedule(tasks):
    n = len(tasks)

    for j in range(n):
        tasks[j].append(j)
    tasks.sort(key=lambda x: x[0])
    schedule = []
    pq = []
    arrival_time = tasks[0][0]
    i = 0
    while i < n:
        if tasks[i][0] == arrival_time:
            heappush(pq, [tasks[i][1], tasks[i][2]])
        else:
            break
        i += 1

    while (pq):
        prio = heappop(pq)
        schedule.append(prio[1])
        arrival_time += (prio[0])

        while i<n and tasks[i][0] <= arrival_time:
            heappush(pq, [tasks[i][1], tasks[i][2]])
            i += 1
        
        if not pq and i < n:
            arrival_time = tasks[i][0]
            while i < n:
                if tasks[i][0] == arrival_time:
                    heappush(pq, [tasks[i][1], tasks[i][2]])
                else:
                    break
                i += 1
    return schedule


tasks = [[1,2],[2,4],[3,2],[4,1]]
print(cpu_schedule(tasks))