# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
print(student_heights)
s=0 
c=0
for n in range(len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
  c+=1
  s+=student_heights[n]
print(round(s/c))



