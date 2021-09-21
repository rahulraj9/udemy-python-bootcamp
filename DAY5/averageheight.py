student_heights = input("Input a list of student heights ").split()
total_student = 0
total_height_sum = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  total_height_sum += student_heights[n] 
  total_student += 1
average_of_student_height = round(total_height_sum/total_student)
print(average_of_student_height) 


