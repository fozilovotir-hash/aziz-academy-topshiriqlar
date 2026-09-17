n = int(input())
d = {}
for i in range(n):
    val = int(input())
    d[f"k{i}"] = val
print(sum(d.values()))