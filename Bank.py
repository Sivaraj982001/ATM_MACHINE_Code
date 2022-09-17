from datetime import date
import time
from BankDatabase import Fetch, updateData

class Bank:
    def __init__(self,BankName, cardno, pin):
        self.bn = BankName
        self.cno = cardno
        self.pin = "'%s'"%(pin)
        self.acno = int(Fetch("ACCOUNT_NO",self.cno))
        self.name = Fetch("NAME",self.cno)
        self.ba = int(Fetch("BALANCE",self.cno))
        self.fee = 10
        self.tt = ""
        self.amount = 0
        self.__opin = Fetch("PIN",self.cno)
        self.minBalance = 100

    def dateTimeGenerator(self):
        now = time.localtime()
        Current_time = time.strftime("%H:%M:%S", now)
        Current_date = date.today()
        return str(Current_date),str(Current_time)

    def PinCheck(self):
        if self.pin == self.__opin:
            return True
        else :
           return False

    def Banknamecheck(self):
        if self.bn=="indian bank":
            pass
        else:
            self.fee+=30
    
    def withdrawl(self):
        print("/--------------------------------------Account type-------------------------------/")
        print("\n1. Savings Account")
        print("2. Current Account\n")
        at = int(input("Enter the Type : \n"))

        if at==1:
            amount = int(input("Enter the Amount of Withdrawl : "))
            
            if self.PinCheck():  
                if(amount<=(self.ba-self.minBalance)):
                    print("wait for Counting.....")
                    print("Collect your Money")
                    self.ba -= amount
                    self.amount = amount
                    self.ba -= self.fee
                    updateData("BALANCE",self.ba,self.cno)
                    self.tt = "Withdrawl"
                else:
                    print("\nInsufficiant Balance")
                    self.fee=0
            else:
                print("\nIncorrect Pin")
                self.fee = 0
        
        if at==2:
            self.fee+=200
            amount = int(input("Enter the Amount of Withdrawl : "))
            if self.PinCheck():  
                if(amount<=(self.ba-self.minBalance)):
                    print("wait for Counting.....")
                    print("Collect your Money")
                    self.ba -= amount
                    self.amount = amount
                    self.ba -= self.fee
                    updateData("BALANCE",self.ba,self.cno)
                    self.tt = "Withdrawl"
                else:
                    print("Insufficiant Balance")
                    self.fee = 0
            else:
                print("Incorrect Pin")
                self.fee = 0
            
    def deposit(self):
        amount = int(input("Enter the Amount of Deposit : "))

        if self.PinCheck():  
                    print("Put your Money on the holder")
                    print("wait for Counting.....")
                    self.ba += amount
                    self.ba -= self.fee
                    self.amount=amount
                    updateData("BALANCE",self.ba,self.cno)
        else:
                print("Incorrect Pin")
            
    def Transfer(self):
        amount = int(input("Enter the Amount of Tranfer : "))
        no = int(input("Enter the cartno of the Tranfer Account Holder : "))
        if self.PinCheck():  
                    print("Put your Money on the holder")
                    print("wait for Counting.....")
                    ba = int(Fetch("BALANCE",no))
                    ba+=amount
                    updateData("BALANCE",ba,no)
                    self.ba-=amount
                    self.ba-=self.fee
                    self.amount=amount
                    updateData("BALANCE",ba,self.cno)
        else:
                print("Incorrect Pin")
    
    def Balance(self):
        print("Your Balnce is %d Rs"%(self.ba))

    def Reciept(self):
        d,t = self.dateTimeGenerator()
        print("------------------------------------------%s--------------------------------------"%(self.bn))
        print("-----------------------------------------------------------------------------------")
        print("Date = ",d)
        print("Time = ",t)
        print("------------------------------------------------------------------------------------")
        print("\n")
        print("CardNo: XXXXX XXXX XXXX %d"%(self.cno))
        print("Transaction: %s"%(self.tt))
        print("Amount: %d Rs"%(self.amount))
        print("Account No: %d"%(self.acno))
        print("Available Balance: %d Rs"%(self.ba))
        print("ATM Opertor fee: %d"%(self.fee))
        print("\n-----------------------------------------------------------------------------------")
    
    def DomainCheck(self,Domain):
        if(Domain==1):
            pass
        elif(Domain==2):
            self.fee+=100
            

            
            





        



