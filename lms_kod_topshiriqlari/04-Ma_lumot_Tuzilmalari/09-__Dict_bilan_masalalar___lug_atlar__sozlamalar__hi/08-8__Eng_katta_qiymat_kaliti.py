n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)
# Eng katta qiymatga ega kalitni topish (qiymatlari bo'yicha max)
max_key = max(d, key=d.get)
print(max_key)