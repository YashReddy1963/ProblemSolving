# Question: Write a Python program to create a BankAccount 
# class with attributes like account_number, balance, 
# account_holder, and methods like deposit(amount) and 
# withdraw(amount). Implement the logic to prevent overdraft.

class BankAccount:
    def __init__(self, acc_num, amount, acc_name):
        self.account_number = acc_num
        self.balance = amount
        self.account_holder = acc_name
        self.services()
    
    def services(self):
        while(1):
            print("1.Deposite money \n2.Withdraw money \n3.Exit")
            ch = int(input("Enter your choice: \n"))
            if ch == 1:
                amount = int(input("Enter the amount to deposite"))
                self.deposite(amount)
            elif ch == 2:
                amount = int(input("Enter the amount to withdraw: \n"))
                self.withdraw(amount)
            elif ch == 3:
                exit()

    def deposite(self, amount):
        self.balance = self.balance + amount
        print(f"The balance currently is: {self.balance} for account holder:{self.account_holder}")

    def withdraw(self, amount):
        if self.balance < amount:
            print("Currently your balance is less then the withdraw amount..")
            return -1
        self.balance = self.balance - amount
        print(f"Currently your balance is: {self.balance} \n")

acc_num=int(input("Enter your account number: \n"))
amount=0
acc_name=input("Enter your name: \n")

obj = BankAccount(acc_num, amount, acc_name)
