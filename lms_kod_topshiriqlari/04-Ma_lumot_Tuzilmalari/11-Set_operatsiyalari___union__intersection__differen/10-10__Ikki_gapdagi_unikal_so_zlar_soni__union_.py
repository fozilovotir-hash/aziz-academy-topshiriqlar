s1 = input().strip().lower().split()
s2 = input().strip().lower().split()
res = len(set(s1).union(set(s2)))
print(res)