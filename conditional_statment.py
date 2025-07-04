"""
#if else
age=int(input("enter your age"))
if  age>=18:
   print("eligible for voating")
else :
    print ("not eligibile")

    
#number is odd or even
num=int(input("enter a number"))
if num%2==0:
    print("num is even")
else:
    print("num is odd")
    

#leap year
year=int(input("enter the year :"))
if (year%4==0 and year%100!=0) or year%400==0 :
    print(year,"is a leap year")
else:
        print(year,"is not leap year")
        
#payment=True
#if payment:
#mark=int("input enter your number" :)
#    if mark>

num1=int(input("enter a number:"))
num2=int(input("enter the second number:"))
print("1.addition\n" "2.substraction\n" "3.multipication\n" "4.division\n ")
num3=int(input("enter your choice :"))
if num3==1:
    print(num1+num2)
elif num3==2:
    print(num1-num2)
elif num3==3:
    print(num1*num2)
elif num3==4:
    print(num1/num2)
else :
    print("not found")
    """

num=int(input("enter a number :"))
if num>0:
    print("number is positive")
elif num<0:
    print("number is negative")
else:
    print("number is zero")