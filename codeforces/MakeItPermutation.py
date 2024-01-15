def min_permutation_cost(a, c, d):
    n = len(a)
    missing = n - len(set(a))
    extra = len(a) - n
    if missing == 0 and extra == 0:
        return 0
    elif missing > 0 and extra == 0:
        return d * missing
    elif missing == 0 and extra > 0:
        return c * extra
    else:
        # Option 1: Insert missing elements first, then remove extra elements
        cost1 = d * missing + c * extra
        # Option 2: Remove extra elements first, then insert missing elements
        cost2 = c * extra + d * (missing - extra)
        return min(cost1, cost2)

n,c,d=5,1, 5
a=[1, 2, 3, 5, 6]
print(min_permutation_cost(a,c,d))