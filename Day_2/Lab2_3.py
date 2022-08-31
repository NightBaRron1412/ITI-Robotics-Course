print("Enter 'q' to exit.\n")
user_input = None

while True:
    user_input = input("Enter Any number: ")
    
    if (user_input.lower() == "q"):
        break
        
    else:
        user_input = int(user_input)
        
        if (user_input % 2 == 0):
            print(f"{user_input} is an even number.\n")
            
        else:
            print(f"{user_input} is a odd number.\n")