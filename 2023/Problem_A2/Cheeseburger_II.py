# Cheeseburger_II

file = open("Input.txt", "r")

def solve():
    A, B, C = map(int,file.readline().split(" "))

    # single burger buy

    ans_count = C // A

    # Double Burger Buy

    ans_count = max (ans_count, 2 * (C // B - 1))

    # 1 Single + Double Remining 
    ans_count = max(ans_count, 2 * ((C - A )// B + 1))


    T = int(file.readline())

    print("Test Case:", T)

    for i in range(1, T + 1):
        print("Case #" + 1 + ":" + solve())