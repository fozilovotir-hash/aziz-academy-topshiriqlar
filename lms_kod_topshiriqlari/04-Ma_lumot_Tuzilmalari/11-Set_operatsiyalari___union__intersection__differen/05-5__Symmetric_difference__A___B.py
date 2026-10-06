a = set(map(int, input().split()))
b = set(map(int, input().split()))
res = a.symmetric_difference(b)
if not res:
    print("BO'SH")
else:
    print(*sorted(res))