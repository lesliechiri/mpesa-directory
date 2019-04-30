from datetime import datetime

class MpesaAccount:
    def __init__(self,name,number,balance):
        self.name = name
        self.number = number
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.loan = 0
        self.loans = []

        

    def withdrawal_amount(self,x):
        withdrawal_amount = x
        if x>self.balance:
            print("cant withdraw")
        else:   
            self.balance = self.balance - x
            
            now = datetime.now()
            object = {"time":now,"x":x}
            self.withdrawals.append(object)
            data = "Dear {} withdrawal of kes {} was successful current balance is{}".format(self.name,x,self.balance)
            print(data)
    def deposit(self,y):
        deposit = y
        self.balance = self.balance + y
        
        now = datetime.now()
        object = {"time":now,"y":y}
        self.deposits.append(object)
        
        depo = "Dear {} deposit of kes {} was successful current balance is {}".format(self.name,y,self.balance)
        print(depo)
    def check_balance(self):


        check_balance = self.balance    
        bee = "Dear {} your current balance is {}".format(self.name,self.balance)

        print(bee)
    def my_deposits(self):
        
        for x in self.deposits:
            time = x["time"].strftime("%A,%d,%B,%Y")
            y = x["y"]
            print("on {} you deposited  {}".format(time,y))

    def my_withdrawals(self):

        for a in self.withdrawals:

            
            time = a["time"].strftime("%A,%d,%B,%Y")
            x = a["x"]
            print("on {}  you withdrew {}".format(time,x))
           
    def give_loan(self,g):
        loan = g 
        total = 0
        for x in self.deposits:
                y = x["y"]
                total+=y
        

        if len(self.deposits)>=5 and g<=total/3 and self.loan==0:
            self.loan = self.loan + g
            
            

            now = datetime.now()
            object = {"time":now,"g":g}
            self.loans.append(object)
            print("Dear customer your loan of {} has been approved".format(g))
        else:
            print("loan not approved") 


            
            
            
        

        

        

        
    def loan_repayment(self,a):


        cash = a
        
        if a<self.loan:
            self.loan = self.loan-a
            print("Dear customer your remaining loan balance is {}".format(self.loan))
        elif a>self.loan:
            excess_cash = a - self.loan
            self.loan = a - excess_cash - self.loan
           
            self.balance = excess_cash+self.balance
        elif a == self.loan:
            self.loan = self.loan-a
            print("Dear customer your loan is now fully paid")


    def my_loans(self):


     
        for b in self.loans:

            
            time = b["time"].strftime("%A,%d,%B,%Y")
            b = a["g"]
            print("on {}  you recieved a loan of {}".format(time,g))

    def statements(self):
       

        for x in self.deposits:
            time = x["time"].strftime("%A,%d,%B,%Y")
            y = x["y"]
            print("on {} you deposited  {}".format(time,y))


        for a in self.withdrawals:

            
            time = a["time"].strftime("%A,%d,%B,%Y")
            x = a["x"]
            print("on {}  you withdrew {}".format(time,x))


        for b in self.loans:

            
            time = b["time"].strftime("%A,%d,%B,%Y")
            g = b["g"]
            print("on {}  you recieved a loan of {}".format(time,g))        

        

        
        
        
    
