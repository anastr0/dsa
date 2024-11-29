
def possible_n_meetings(n, start, end):
    p = [(start[0], end[0])]
    pm = [1]
    for i in range(1, len(start)):
        if start[i] >= p[-1][1]:
            p.append((start[i], end[i]))
            pm.append(i+1)
    return pm

if __name__=="__main__":
    N = 6
    start = [1,3,0,5,8,5]
    end =  [2,4,5,7,9,9]

    print(possible_n_meetings(N, start, end))