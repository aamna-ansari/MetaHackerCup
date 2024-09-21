def try_sum(a, sum_val):
    skipped = 0
    l = 0
    r = len(a) - 1
    res = sum_val//2 
    
    while l <= r:
        if a[l] + a[r] == sum_val:
            l += 1
            r -= 1
        else:
            skipped += 1
            if a[l] + a[r] < sum_val:
                res = sum_val - a[l]
                l += 1
            else:
                res = sum_val - a[r]
                r -= 1
    return res if skipped <= 1 and res > 0 else float('inf')

def solve():
    N = int(input())
    if N == 1:  # Special case where there's only one element in the list
        return 1
    sz = 2 * N - 1
    a = list(map(int, input().split()))
    a.sort()
    ans = min(
        try_sum(a, a[1] + a[sz - 1]) if len(a) > 1 else float('inf'),  # remove first
        try_sum(a, a[0] + a[sz - 1]) if len(a) > 1 else float('inf'),  # remove middle
        try_sum(a, a[0] + a[sz - 2]) if len(a) > 2 else float('inf')   # remove last
    )
    return -1 if ans == float('inf') else ans

def main():
    T = int(input())
    for t in range(1, T + 1):
        print(f"Case #{t}: {solve()}")


main()