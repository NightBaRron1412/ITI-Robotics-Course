def swap_case(s):
    
    s_list = []
    
    for char in s:
        if (char.isupper()):
            s_list.append(char.lower())
            
        elif (char.islower()):
            s_list.append(char.upper())
            
        else:
            s_list.append(char)
            
    s = "".join(s_list) 

    return s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)