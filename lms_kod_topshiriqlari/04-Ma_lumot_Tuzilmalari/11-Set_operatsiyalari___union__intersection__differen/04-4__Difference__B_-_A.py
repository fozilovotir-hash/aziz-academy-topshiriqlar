a = set(map(int, input().split()))
b = set(map(int, input().split()))
res = b.difference(a)
if not res:
    print("BO'SH")
else:
    print(*sorted(res))