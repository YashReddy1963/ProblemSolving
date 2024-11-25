str="Hello World! 123"
count=0
digit=0
for i in str:
    if(i.isalpha()):
        count=count+1
    elif(i.isnumeric()):
        digit=digit+1

print("LETTERS=",count)
print("DIGITS=",digit)