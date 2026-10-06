a = set(map(int, input().split()))
b = set(map(int, input().split()))
intersection_size = len(a.intersection(b))
union_size = len(a.union(b))
jaccard = intersection_size / union_size
print(f"{jaccard:.3f}")