
student_scores = input("Input a list of student scores ").split()
highest_score = int(student_scores[0])
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
  if student_scores[n] > highest_score :
      highest_score = student_scores[n]

print(highest_score)