n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
total_score = sum(student['score'] for student in students)
print(total_score / n)