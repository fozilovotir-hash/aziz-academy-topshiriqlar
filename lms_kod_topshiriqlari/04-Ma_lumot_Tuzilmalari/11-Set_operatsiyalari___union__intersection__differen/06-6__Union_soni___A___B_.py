a = set(map(int, input().split()))
b = set(map(int, input().split()))
res = len(a.union(b))
print(res)