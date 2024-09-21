T = int(input()) 

for t in range(1 , T +1 ):
    print(f"Case {t}", end = '')

    R, C, A, B = map(int, input().split())

    print("YES" if R > C else "No")