s = input().strip()
d = {}
for char in s:
    d[char] = d.get(char, 0) + 1
res = []
for k, v in d.items():
    res.append(f"{k}:{v}")
print(" ".join(res))
         