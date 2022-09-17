from Bank import Bank
from BankDatabase import Fetch 

print("-------------------------------------------Welcome To the Indian Bank----------------------------------------")

bank = input("Enter the Bank : ").strip().upper()
card_no = int(input("Enter your card no : "))
print("/...Fetching Data.../")

#FetchData
Name = Fetch("NAME",card_no)
print("/................Welcome %s......../"%(Name))

P = input("\nEnter Your Pin : ").strip()

obj = Bank(BankName=bank,cardno=card_no,pin=P)
obj.Banknamecheck()

print("----------------------------------Domain Menu---------------------------\n")
print("1. Domestic")
print("2. International")
Domain = int(input("Enter your Domain : "))
obj.DomainCheck(Domain)

print("-------------------------------------Transaction Menu----------------------------------\n")
print("\n1. WithDrawl")
print("2. Deposit")
print("3. Transfer")
print("4. Balance\n")
option = int(input("Choose Your option : \n"))

if(option == 1):
    obj.withdrawl()
elif(option == 2):
    obj.deposit()
elif(option== 3):
    obj.Transfer()
elif(option == 4):
    obj.Balance()

if (obj.PinCheck() and option!=4):
    print("--------------------------------------Collect your Reciept---------------------------------------------------")
    obj.Reciept()

print("----------------------------------------------Thank you for using %s---------------------------------"%(obj.bn))


