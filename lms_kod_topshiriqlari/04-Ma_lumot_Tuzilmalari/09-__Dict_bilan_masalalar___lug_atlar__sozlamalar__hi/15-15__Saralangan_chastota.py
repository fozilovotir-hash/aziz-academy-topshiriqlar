s = input().strip()
d = {}
for ch in s:
    d[ch] = d.get(ch, 0) + 1
for ch in sorted (d):
    print(f"{ch}={d[ch]}")