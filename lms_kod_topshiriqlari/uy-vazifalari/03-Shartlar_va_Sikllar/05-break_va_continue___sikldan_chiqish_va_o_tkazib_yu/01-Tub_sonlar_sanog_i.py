count = 0
while True:
    n = int(input())
    if n == 0:
        break
    if n < 2:
        continue
    tub = True
    for i in range(2, n):
        if n % i == 0:
            tub = False
            break
    if tub:
        count += 1
print(count)