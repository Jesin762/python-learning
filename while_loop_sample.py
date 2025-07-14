"""
count=1
while count<=10:
    print(count)
    count+=10
    
num=int(input("enter a number:"))
count=1
while count<=10:
    print(f" {num} * {count} = {num * count}")
    count=count+1
    """
while True:
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
 else:
    print("not found")
 hello=str(input("if you wamt to continue : yes or no :"))
 if hello.lower()!="yes":
    break
    
    
    