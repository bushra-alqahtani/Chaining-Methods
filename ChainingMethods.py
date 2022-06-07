class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposite(self,amount):
        self.account_balance+=amount
        return self
   
    def make_withdrawal(self, amount):
        self.account_balance-=amount
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self
    def transfer_money(self, other_user, amount):
        other_user.account_balance+=amount
        self.account_balance-=amount
        return self


yahya=User("Yahya","Yahya@gmail.com")
bushra=User("Bushra","bushra@gmail.com")
talal=User("Talal","talal@gmail.com")

yahya.make_deposite(1000).make_deposite(2000).make_deposite(4000).make_withdrawal(1000).transfer_money(talal,3000).display_user_balance()


bushra.make_deposite(2000).make_deposite(2500).make_withdrawal(600).make_withdrawal(150).display_user_balance()


talal.make_deposite(5000).make_withdrawal(200).make_withdrawal(300).make_withdrawal(1000).display_user_balance()



