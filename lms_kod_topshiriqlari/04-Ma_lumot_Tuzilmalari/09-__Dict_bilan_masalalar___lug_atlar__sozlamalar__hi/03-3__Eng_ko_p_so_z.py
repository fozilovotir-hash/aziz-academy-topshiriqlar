n = int(input())
d = {}
for _ in range(n):
    word = input().strip()
    d[word] = d.get(word, 0) + 1
# Eng ko'p uchragan so'zni topish (lug'atga birinchi kiritilgan tartibda eng kattasini oladi)
most_common = max(d, key=d.get)
print(most_common)