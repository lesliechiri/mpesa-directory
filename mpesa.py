class MpesaAccount:
    def __init__(self,name,number,balance):
        self.name = name
        self.number = number
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.loan = 0
        

    def withdrawal_amount(self,x):
        withdrawal_amount = x
        if x>self.balance:
            print("cant withdraw")
        else:   
            self.balance = self.balance - x
            self.withdrawals.append(x)
            data = "Dear {} withdrawal of kes {} was successful current balance is{}".format(self.name,x,self.balance)
            print(data)
    def deposit(self,y):
        deposit = y
        self.balance = self.balance + y
        self.deposits.append(y)
        
        depo = "Dear {} deposit of kes {} was successful current balance is {}".format(self.name,y,self.balance)
        print(depo)
    def check_balance(self):


        check_balance = self.balance    
        bee = "Dear {} your current balance is {}".format(self.name,self.balance)

        print(bee)
    def my_deposits(self):
        
        for x in self.deposits:
            print(x)

    def my_withdrawals(self):

        for y in self.withdrawals:
            print(y)
    def give_loan(self,g):
        loan = g 
        
        

        if len(self.deposits)>=5 and g<=(1/3*sum(self.deposits)) and self.loan==0:
            self.loan = self.loan + g
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
            
        elif self.loan==0:
            print("Dear customer your loan of {} has been cleared".format(self.loan))
       
           
        

        
        
        
    
