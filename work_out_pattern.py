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

for i in range(1,6):
    for k in range(1,i+1):
        print(i*k,end=" ")
    print()