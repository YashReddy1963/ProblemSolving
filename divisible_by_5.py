n = input("Enter the Binary nubersnumbers separated by commas: ").split(",")
for i in n:
    if int(i) % 5 == 0:  
        print(i)