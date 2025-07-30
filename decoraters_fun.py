"""def change(fun):
 
  def wrapper():
    print("how are you")
    fun()
    print("okayyy")
  return wrapper
@change
def greeting():
   print("i am fine")
greeting()
"""
#
"""def change(fun):
    def wrapper(a, b):       
        return fun(b, a)     
    return wrapper

@change
def subtract(a, b):
    print(a - b)

subtract(45, 50)  """
#
"""def subtract(a,b):
    a,b=b,a
    print(a-b)
subtract(10,20)"""
#
"""
def subtract(a,b):
    c=a
    a=b
    b=c
    print(a-b)
subtract(10,20)"""


