
def job_seq():
    # Jobs = [(1,4,20),(2,1,10),(3,1,40),(4,1,30)]
    # N = 4

    N = 5
    Jobs = [(1,2,100),(2,1,19),(3,2,27),(4,1,25),(5,1,15)]
    Jobs.sort(key=lambda x: x[2], reverse=True)

    jobs_count = 0
    jobs_time_profit_map = {}
    total_profit = 0

    for i in range(N):
        idx, deadline, profit = Jobs[i]

        for t in range(deadline, 0, -1):
            if t not in jobs_time_profit_map:
                jobs_time_profit_map[t] = idx
                jobs_count += 1
                total_profit += profit
                break


        # if time in jobs_time_profit_map:
        #     if jobs_time_profit_map[time] < profit:
        #         total_profit += (profit - jobs_time_profit_map[time])
        #         jobs_time_profit_map[time] = profit
        # else:
        #     jobs_time_profit_map[time] = profit
        #     total_profit += profit
        #     jobs_count += 1
    
    return jobs_count, total_profit


print(job_seq())