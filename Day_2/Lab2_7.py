print("Enter 'q' to stop.\n")
str_list = []

while True:
    #here implement a code that does the specified function
    char = input("Enter the ASCII for the characters: ")
    
    if (char == 'q'):
        break
        
    else:
        char = chr(int(char))
        str_list.append(char)
        
_str = "".join(str_list)        
print(f"\nThe result string is: {_str}")