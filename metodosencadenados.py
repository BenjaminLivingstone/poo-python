
class User:	
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        # print(f"El {self.name} {self.account_balance}")
        # print (self.account_balance)
        return self

    def make_withdrawal(self, amount):
        if amount>self.account_balance:
            print(f"No puede hacer un retiro de {amount}, su saldo es de {self.account_balance}")
            return self
        else:
            self.account_balance -=amount
            return self

    def display_user_balance(self):
        print(f"Usuario: {self.name}, Saldo: ${self.account_balance}")
        return self

    def transfer_money (self, other_user, amount):    
        if amount>self.account_balance:
            print(f"No puede hacer una transferencia de ${amount}, su saldo es de ${self.account_balance}")
            return self        
        else:
            self.make_withdrawal(amount)
            other_user.make_deposit(amount)
            print(f"{self.name} hiso una transferencia de ${amount} a {other_user.name}")
            return self
        # print (other_user.display_user_balance())
        # print (self.display_user_balance())
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")

guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(200)
monty.make_deposit(50)
monty.make_withdrawal(50)

# guido.display_user_balance()
# monty.display_user_balance()
# monty.transfer_money(guido,50)
# guido.display_user_balance()
# monty.display_user_balance()

monty.transfer_money(guido,500)

monty.make_withdrawal(50).transfer_money(guido,50)

guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(1100).display_user_balance()
