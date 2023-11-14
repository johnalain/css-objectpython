from typing import Self


class Employee :
    def __init__(self,name,age,department,is_manager,rating,salary):
        self.name = name
        self.age = age
        self.department = department
        self.is_manager = is_manager
        self.rating =rating
        self.salary = salary
        
    def is_excellent(self):
        if self.rating >= 4.5:
         return True
        else:
         return False
     
    # def bonus(self):
    #     if self.age == 60:
    #         self.salary += 500
    #     print("salary is "+ str(self.salary))
    def bonus(self):
        if self.age == 60:
            self.salary += 500
            print("salary is "+ str(self.salary))
        else:
         print("no bonus added"+ str(self.salary))
        
        
        
        



   
#    
#      print("sorry u rnot 60 "+ (self.salary) )
        
# class Student:
    # def __init__(self,name,age,major,university_name):
        
    #     self.name = name
    #     self.age = age
    #     self.major = major
    #     self.university_name = university_name
       

