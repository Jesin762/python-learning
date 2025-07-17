"""for i in range(1,6):
    for k in range(65,65+i):     #q no:3
        print(chr(k),end=" ")
    print()"""

"""for i in range(1,6):
    print(" "*int(5-i),"* "*i) 
for i in range(5,0,-1):            # q no:2
    print(" "*int(5-i),"* "*i)"""

"""for i in range(5,0,-1):       # q no: 2
    print(" "*int(5-i),"* "*i) """

for row in range(1,5):
    for col in range(1,5):
        if (col==1 or col==4) or (row==1 or row==4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()        

        
