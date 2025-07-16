"""def fun():
    print("hola!")
fun()"""


"""def fun(name):
    print("hello",name)
fun("hi")
fun("haaaa")"""

"""def fun(name):
    pass

fun("hi")"""

"""def fact(num):
    f=count=1
    while count<=num:
        f=f* count
        count+=1
    print(f)
fact(5)"""


"""def is_even(num):
    if num%2==0:
        print(num," is even")
    else:
        print(num," is odd")
num=int(input("enter a number:"))
is_even(num)"""

def is_positive(num):
    if num>=0:
        return True
    else:
        return False
num=int(input("enter a number:"))
print(is_positive(num))




