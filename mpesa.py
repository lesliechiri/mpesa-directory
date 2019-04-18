class MpesaAccount:
	def __init__(self,name,number,balance):
		self.name = name
		self.number = number
		self.balance = balance
	def withdrawal_amount(self,x):
		withdrawal_amount = x
		x<self.balance
		self.balance = self.balance - x
		
		data = "Dear {} withdrawal of kes {} was successful current balance is{}".format(self.name,x,self.balance)
		print(data)
	def deposit(self,y):
		deposit = y
		self.balance = self.balance + y
		
		depo = "Dear {} deposit of kes {} was successful current balance is {}".format(self.name,y,self.balance)
		print(depo)
	def check_balance(self):


		check_balance = self.balance	
		bee = "Dear {} your current balance is {}".format(self.name,self.balance)
		print(bee)
		
		
		
	
