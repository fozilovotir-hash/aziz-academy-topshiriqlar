numbers = list(map(int, input().split()))
sorted_unique = sorted(set(numbers))
print(*sorted_unique)