n = int(input())
eng = int(input())
pos = 1 
for i in range(2, n + 1):
    x = int(input())
    if x > eng:
        eng = x
        pos = i
print(pos)