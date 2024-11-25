num=int(input("Enter a number:"))
sum = 0
originalNum = num
for i in range(0,4):
    sum += num # sum=9
    num = (num * 10) + originalNum # 90 + 9

print("The computed value is: ", sum)
