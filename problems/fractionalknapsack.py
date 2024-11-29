


def frac_knapsack():
    N = 3
    W = 50
    values = [100,60,120]
    weight = [20,10,30]
    MAX_VAL = 0

    val_unit = [[(v/w), v, w] for v,w in zip(values, weight)]
    val_unit.sort(reverse=True)

    i = 0
    while W > 0 and i < N:
        if W > val_unit[i][2]:
            W -= val_unit[i][2]
            MAX_VAL += val_unit[i][1]
        else:
            MAX_VAL += W * val_unit[i][0]
            W = 0
        print(MAX_VAL, W)
        i += 1
    return MAX_VAL

print(frac_knapsack())