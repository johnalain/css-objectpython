
# my_num = input("enter ur number")
# my_num1 = input("enter another number")
# result = int(my_num) + int(my_num1)
#if you enter decimal number u should use float instead of int
# result = float(my_num) + float(my_num1)
# print(result)
# lists
# friends = [1,"codezilla",True,False,[1,"michel"]]
#friends =[index0,index1,index2,index3,index4]
#list can have more then one item variable has only one
#u can put a list inside another list
# print (friends)
# print(friends[0])
# friends = ["example","codezilla","python","programming"]
#index[-1] print last item of list
# print(friends[-1])
# print(friends[-2])
# print(friends[-4])
# # print(friends[-5])//out of list range
# print(friends[1:3])
# #print from index 1 to index 3 "index3"not included
# print(friends[0:3])
# print(friends[1:])
# #print(friends[1:])from index 1 till end of list
# #['codezilla', 'python', 'programming']
# friends[0] = "michel"
# #to change item in list ['michel', 'codezilla', 'python', 'programming
# print(friends)
# codezilla = ["programming", "python", "tutorials", "html","css"]
# tutorial =["extend","list1","codezilla"]
# print(codezilla,tutorial)
#['programming', 'python', 'tutorials', 'html', 'css'] ['extend', 'list1', 'codezilla'] print 2 lists
# codezilla.extend(tutorial)
# print(codezilla)
# ['programming', 'python', 'tutorials', 'html', 'css', 'extend', 'list1', 'codezilla']
# codezilla += tutorial 
# same as codezilla = codezilla + tutorial to do concatnation
# codezilla.append("rita")
#['programming', 'python', 'tutorials', 'html', 'css', 'extend', 'list1', 'codezilla', 'extend', 'list1', 'codezilla', 'rita'] append(rita,1)to add item
# codezilla.insert(0,"josephine")
#insert(index where to insert item,"item")
# codezilla.remove("python")
#remove item from list
# codezilla.remove("jjj")
#"jjj" not in the list give error
# codezilla.clear()
# erase all items frm list
# codezilla.pop()
#eliminate last item

# print(codezilla)

# ex:4 calculator
# first_num = int(input("enter first num : "))
# operation = input("enter operation: ")
# second_num = int(input("enter second num : "))

# if operation == '+':
#     print(first_num + second_num)
# elif operation == '-':
#     print(first_num - second_num)
# elif operation == '/':
#     print(first_num / second_num)
# else :
#     print(first_num * second_num)
 #python function   
# -def add_number(a, b):
#     -return a + b
# -result = add_number(3,5)
# -print(result)
# javascript function
# -function sayHello() {
#   -console.log("hello michel");
# =}
# -sayHello();
    
# def slat_mik():
#     return "hello"

# print(slat_mik())
# def greet(name):
#     return "hello,"+ name
# dataFromFunction = greet("rita")
    
# print (dataFromFunction)

# def greet(name):
#     return "hello, dear " + name
# # dataFromFunction = greet ("josephine")
# print(greet("amal"))
    
# def say_hi(name,age):
#     return "my name is:  +name+ my age is: +str (age)"
#     datafromfunction = greet(rita,27)
#     print(datafromfunction)
 
# x = int(input("input first number: "))
# y = int(input("input second number"))
# def add(x,y):
#   return x+y
# print (add(x,y))
# for x in range(1,12):
#     print(x)
# for x in reversed(range(1,12)):
#      print(x)
    
# print("happy  new year")

# for x in reversed(range(1,12,2)):
#      print(x)
    
# print("happy  new year")

# for x in range(1,12,2):
#      print(x)
    
# print("happy  new year")
# credit_card = "1234-4567-7890-2345"
# for x in credit_card:
#     print (x)
# https://www.youtube.com/watch?v=KWgYha0clzw
# for x in range(1, 21):
#     if x == 3:
#         breakpoint
# else:
#     print(x)
#https://www.youtube.com/watch?v=cqopVpEWvCc video#28
# from Employee import Employee
# from Employee import Student
# employee1 = Employee("michel",50,"facebook",True)
# employee2 = Employee("rita",27,"hos",False)
# print(employee1.name) 
# print(employee2.name) 
# print(employee1.age)
# print(employee2.is_manager)
# print(employee1.is_manager)
# #create file emmplee.py hold a class Employee
# print(employee1.name,employee2.name)
# print(employee1.age,employee2.age,employee1.department,employee2.is_manager)

# student1 = Student("josephine",17,"computer science","aub")
# print(student1.name)
# print(student1.name,student1.age,student1.major,student1.university_name)

#https://www.youtube.com/watch?v=ZaQgQN2HTGY&t=1s
from Employee import Employee
# from Employee import Student
from FamilyDoctor import FamilyDoctor



employee1 = Employee("michel",50,"codezilla",True,5,1500)
employee2 = Employee("rita",60,"facebook",False,4,500)
# employee1 = Employee("michel",1500)
# employee2 = Employee("rita",500)
# print(employee1.name,employee1.age,employee1.department,employee1.rating)
# print(employee1.is_excellent())
# print(employee2.is_excellent())
# print(employee1.name,employee1.salary)
# print(employee2.name,employee2.age,employee2.salary)
print(employee1.salary)
print(employee1.bonus())
print(employee2.salary)
print(employee2.bonus())



doctor2=FamilyDoctor ()


doctor2.studied_years()
doctor2.works_where()
doctor2.paid_by_who()


