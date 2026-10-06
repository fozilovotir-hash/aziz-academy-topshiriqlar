group_a = set(input().split())
group_b = set(input().split())
common = sorted(group_a.intersection(group_b))
print(len(common))
for name in common:
    print(name)