#输入班级1的学生数量，存储至num1
#Enter the number of students in class 1 and store it in num1
num1 = int(input("输入班级1的学生数量:"))

class1 = set()
'''
初始化集合class1
Initialize the collection class1
'''
#通过循环，输入班级1学生的姓名
#Enter the name of student 1 in class 1 through the loop
for i in range(0, num1):
    name = input("输入学生%d姓名:"%(i + 1))
    class1.add(name)
'''
添加至集合class1
Add it to the collection class1
'''

#输入班级2的学生数量，存储至num2
#Enter the number of students in class 2 and store it in num2
num2 = int(input("输入班级2的学生数量:"))

class2 = set()
'''
初始化集合class2
Initialize the collection class2
'''
#通过循环，输入班级2学生的姓名
#Enter the names of students in Class 2 through the loop
for i in range(0, num2):
    name = input("输入学生%d姓名:"%(i + 1))
    class2.add(name)
'''
添加至集合class2
Added to the collection class2
'''
#求出class1与class2的交集，存储至same
#Find the intersection of class1 and class2, and store it in same
same = class1 & class2

print("重名的学生:")
for name in same:
    print(name)
'''
将重名的同学打印
Print the classmates with the same name
'''
    
    
