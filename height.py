# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
i = 0
# count the length of list
for a in student_heights:
    i += a
print(i)
j = 0
for b in student_heights:
    j += 1
print(j)

average_height = i / j
print(round(average_height))