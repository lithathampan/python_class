def string_formation(base):
    string=""
    while base>0:
        string = string + "*"
        base -=1
    print(string)
    
def triangle():
    base_num=int(input("Enter the number of stars on base of the triangle"))
    num=1
    while num <= base_num:
        string_formation(num)
        num +=1
    while base_num >0:
        num=base_num - 1
        string_formation(num)
        base_num -=1
        
        
triangle()
