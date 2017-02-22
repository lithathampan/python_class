def triangle():
    base=int(input("Enter number:"))
    for i in range(1,base+1):
        for j in range(0,i):
            print("*",end="")
        print("")
    for i in range(base-1,0,-1):
        for j in range(0,i):
            print("*",end="")
        print("")
        
triangle()
