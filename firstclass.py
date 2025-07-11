#Print name and age.
# fname="Aareejan"
# age= 19
# print(f"My name is {fname} and age is {age} ")

#Add Two numbers.
# a=12
# b=10
# print(a+b)

#Input age by user and check if minor or adult.
# age= int(input("Enter your age:"))
# if age<18:
#     print('You are minor')
# else:
#     print("You are adult")

#Print Hi 5 times
# for i in range(5):
#     print("Hi")


#Program that greets person usiing name.

# def greet():
#     name=input("Enter name:")
#     print(f"Hello, {name}")
# greet()

# #Constructor
# class student:
#     def __init__(self,name):
#         self.name=name
#     def greet(self):
#         print("Hello,", self.name)
# p1= student("Aareejan")
# p1.greet()

#Set Examples
# s={1,2,3,4,2}
# print(s)
# d=set()
# d.add(5)
# print(d)
# s1={1,2,3}
# s2={3,4,5}
# print(s1.union(s2))
# print(s1.intersection(s2))

#Frozenset-Example
# fs=frozenset([1,2,3,2])
# print(fs)
# s={frozenset([1,2]),frozenset([3,4])}
# print(s)

#defaultdict - Example
# from collections import defaultdict
# d=defaultdict(int)
# d['a']+=1
# print(d)
# d2=defaultdict(list)
# d2['x'].append(10)
# print(d2)

#  #try-except EXample
# try:
#     num=int(input('Enter a number:'))
#     result=10/num
#     print('Result is:', result)
# except ZeroDivisionError:
#         print('Cant divide by Zero')

# except ValueError:
#         print("Invalid input,please enter a number")


#WAP to draw square using python graphics.
# import turtle
# t=turtle.Turtle()
# for i in range(4):
#     t.forward(100)
#     t.right(90)
# turtle.done()

#WAP to draw heart using python graphics.
# import turtle

# t = turtle.Turtle()
# t.color("red")
# t.begin_fill()

# t.left(140)
# t.forward(113)
# t.circle(-57, 200)
# t.left(120)
# t.circle(-57, 200)
# t.forward(113)

# t.end_fill()
# turtle.done()

#WAP to draw heart and text inside
import turtle
t = turtle.Turtle()
t.color("red")
t.begin_fill()

t.left(140)
t.forward(113)
t.circle(-57, 200)
t.left(120)
t.circle(-57, 200)
t.forward(113)

t.end_fill()


t.hideturtle()
t.penup()
t.goto(0, -20) 
t.color("black")
t.write("I LOVE YOU", align="center", font=("Arial", 30, "bold"))

turtle.done()





