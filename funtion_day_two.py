# ---- *args and **kwargs ----
 #tuple

"""def total(*n):
    print(sum(n))  
total(56,77,88)"""

#dictinoray

"""def greetings(**student):    
    print(f"hello {student["name"]} you are {student["age"]} years old")
greetings(age=19,name="jesin")"""
#

"""def a(a,b,):
    return a,b
c,b=a(7,3)
print(c,b)"""
  #global keyword

"""c=0
def sample():
    global c
    c=c+2         
sample()
print(c)"""

#recursion

"""def fact(num):
    if num==1:
        return num
    else:
        return num*fact(num-1)
print(fact(5))    """

#reverse recurssion

"""def rev(s):
    if len(s)==0:
        return s
    else:
        return rev(s[1:])+s[0]
print(rev("lechu"))    
"""

#list comprehenssion----

"""evens=[k for k in range(1,20) if k%2==0 ]
print(evens)

odd=[k for k in range(1,20) if k%3==1 ]
print(odd)"""

#lambda------

"""v=lambda a,b:a+b
print(v(45,6))"""

"""even=lambda num:True if num%2==0 else False
print(even(24))"""


"""num=int(input("enter a  number:"))
is_even=lambda num:f"{num} is even" if num%2==0 else f"{num} is odd"
print(is_even(num ))"""

#map---
"""def squares(num):
    return num**2
number=[1,3,6,8]   
print(list(map(squares,number)))"""

#map with lambda

"""number=[1,3,6,8]   
print(list(map(lambda x:x**2,number)))"""

"""numbers=[12,3,7,14,10,5]
print(list(map(lambda x:True if x%2==0 else False,numbers)))"""

#filter

"""number=[12,3,7,14,10,5]
print(list(filter(lambda x:True if x%2==0 else False,number)))"""

"""my_list=[1,33,66,7]
print(my_list.enumerate())"""

#zip ---used to covert 2 list in to one 
"""
for k,v in zip(["name","age","place"],["jesin",20,"kochi"]):
    print(k,v)
"""

#exception handling-- instead of error they tell us what is the error

"""a,b=10,0
try:
    c= a/b
    print(c)
except Exception:
    print("please enter a vaild number")"""

#using as e

"""a,b=10,0
try:
    c= a/b
    print(c)
except Exception as e:
    print(e)
    print("please enter a vaild number")"""

#diiferent types of error

"""a,b=10,0
try:
    c=a/b
    print(c)
except ZeroDivisonErro:
 print("please enter a vaild number greater than")
except NameError:
    print("value not defined dor operants")"""




#program to enter 2 numbers using splits
"""
a,b=map(int, input("enter two number:").split())
print(a,b)"""

#finally
 
"""a,b=map(int, input("enter two number:").split())
try:
    c=a/b
    print(c)
except Exception as e:
    print("enter a valid number")
finally:
    print("program executed")"""

while True:
 try: 
   a ,b=map(int, input("enter two number:").split())
   try:
     c=a/b
     print(c)
   except Exception:
    print("enter a divisiblr number")
 except NameError:
      print("not found")
 except Exception as e:
   print(e)
   


   






