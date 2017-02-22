import random
def guess_number():
    num=random.randint(1,9)
    user_input=int(input("Enter number between 1 1nd 9:"))
    while num !=user_input:
        user_input=int(input("Enter number between 1 1nd 9:"))
    print("Well Guessed!")
guess_number()
        
        
    
