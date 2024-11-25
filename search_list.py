def search_list(user_list, name):
    index = 0
    for i in user_list:
        if(i.lower() == name.lower()):
            return index
        index += 1
    return -1
        
    


values = input("Enter the values :")
user_list = values.split()
name = input("Enter the name to search:")
answer = search_list(user_list, name)
print(answer)