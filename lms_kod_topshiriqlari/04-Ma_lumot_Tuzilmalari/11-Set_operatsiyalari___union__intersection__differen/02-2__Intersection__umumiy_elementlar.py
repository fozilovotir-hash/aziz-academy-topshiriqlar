a = set(map(int, input().split()))
b = set(map(int, input().split()))
res = a.intersection(b)
if not res:
    print("BO'SH")
else:
    print(*sorted(res))