a = set(map(int, input().split()))
b = set(map(int, input().split()))
result = sorted(a.union(b))
print(*result)