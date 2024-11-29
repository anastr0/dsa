


def pow(val: int, exp: int) -> int:
    # square and multiply algorithm
    # used in modular exponentiation
    if exp == 0:
        return 1

    if exp == 1 or val == 0 or val == 1:
        return val

    ans = 1
    base = val

    while exp > 0:
        if exp%2:
            exp -= 1
            ans *= base
        else:
            exp = exp//2
            base = base*base
    return ans


def nthroot(n: int, m:int) -> int:
    # answer space = [1..m]
    # 
    #  binary search - until pow(x, n)==m

    low = 0
    high = m-1
    while low < high:
        mid = low + (high-low)//2

        m_val = pow(mid, n)

        if m_val == m:
            return m
        elif m_val < m:
            low = mid + 1
        else:
            high = mid - 1

    return low if pow(low, n)==m else -1


print(nthroot(5, 32768))