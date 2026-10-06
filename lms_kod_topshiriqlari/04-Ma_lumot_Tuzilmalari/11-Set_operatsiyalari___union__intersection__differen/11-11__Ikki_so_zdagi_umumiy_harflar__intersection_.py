s1 = set(input())
s2 = set(input())
res = s1.intersection(s2)
if not res:
    print("BO'SH")
else:
    print("".join(sorted(res)))
      
