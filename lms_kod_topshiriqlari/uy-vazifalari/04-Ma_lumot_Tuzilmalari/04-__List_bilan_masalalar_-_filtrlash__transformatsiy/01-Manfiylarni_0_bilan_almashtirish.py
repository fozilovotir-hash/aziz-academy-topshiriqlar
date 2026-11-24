nums = input().split()
res = ""
for x in nums:
    v = int(x)
    if v < 0 :
        v = 0
    if res == "":
        res = str(v)
    else:
        res = res + " " + str(v)
print(res)