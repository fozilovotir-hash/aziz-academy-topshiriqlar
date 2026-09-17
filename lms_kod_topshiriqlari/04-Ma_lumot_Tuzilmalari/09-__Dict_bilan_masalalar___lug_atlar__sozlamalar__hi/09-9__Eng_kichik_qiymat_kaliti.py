n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)
min_key = min(d, key=d.get)
print(min_key)