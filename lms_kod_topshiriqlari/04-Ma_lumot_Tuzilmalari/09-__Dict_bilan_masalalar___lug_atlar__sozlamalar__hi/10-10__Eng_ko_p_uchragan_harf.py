s = input().strip()
d ={}
for char in s:
    d[char] = d.get(char, 0) + 1
most_common_char = max(d, key=d.get)
print(most_common_char)