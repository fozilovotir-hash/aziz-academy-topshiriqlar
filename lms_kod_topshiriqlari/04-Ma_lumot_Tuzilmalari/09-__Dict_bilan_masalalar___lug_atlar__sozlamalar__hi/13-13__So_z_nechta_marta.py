n = int(input())
d = {}
for _ in range(n):
    soz = input().strip()
    d[soz] = d.get(soz, 0) + 1
izlanadigan = input().strip()
print(d.get(izlanadigan, 0))