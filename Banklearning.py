class Account:
    def __init__ (self, balance , accountno):
      self.balance = balance
      self.accountno = accountno

    def debit(self, amount):
       self.balance -= amount
       print("Debited = " , amount)
       print("Total Balance = " , self.get_balance())

    def credit(self, amount):
       self.balance += amount
       print("Debited = " , amount)                                          
       print("Total Balance = " , self.get_balance())
    
    def get_balance(self):
       return self.balance

A1 = Account(35000, 104330028)
A1.debit(500)
A1.credit(700)


