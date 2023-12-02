# these files sre in github repository objectpython 
#elzero web schoo python video 21
myList = ["one","two","one",1,100, 5.7,True ]
print(myList[0])
print(myList[-1])#True
print(myList[2])
print(myList[1:4])#['two', 'one', 1]
print(myList[:4])#['one', 'two', 'one', 1]
print(myList[1:]) #['two', 'one', 1, 100, 5.7, True]
print(type(myList[0]))#<class 'str'>

print(myList[::1])#['one', 'two', 'one', 1, 100, 5.7, True]
print(myList[::2])#['one', 'one', 100, True]
# print(myList[150])#IndexError: list index out of range

myList[1] = 1
print(myList)#['one', 1, 'one', 1, 100, 5.7, True]
myList[-1] = False
print(myList)#['one', 1, 'one', 1, 100, 5.7, False]
myList[0:3] = ["A", "B", "C"]
print(myList)#['A', 'B', 'C', 1, 100, 5.7, False]
myList[0:3] = ["A"]
print(myList)#['A', 1, 100, 5.7, False]




