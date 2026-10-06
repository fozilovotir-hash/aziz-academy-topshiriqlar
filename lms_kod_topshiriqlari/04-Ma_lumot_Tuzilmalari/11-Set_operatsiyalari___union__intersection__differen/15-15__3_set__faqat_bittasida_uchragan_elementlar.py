a = set(map(int, input().split()))
b = set(map(int, input().split()))
c = set(map(int, input().split()))
only_a = a - b - c
only_b = b - a - c
only_c = c - a - b
res = only_a | only_b | only_c
if not res:
    print("BO'SH")
else:
    print(*sorted(res))