n = int(input().strip())
courses = []
for _ in range(n):
    parts = input().split()
    name = parts[0]
    k = int(parts[1])
    students = parts[2:2+k]
    courses.append({'name': name, 'students': students})

student = input().strip()
soni = 0
for c in courses:
    if student in c['students']:
        soni += 1
print(soni)