# Asociación entre clases
# Objetivos:
# Comprender cómo las diferentes clases pueden relacionarse entre sí
# Practica escribir clases con atributos de un tipo personalizado
# Ahora que tenemos una clase de usuario y una clase de BankAccount, pensemos en la relación entre ellos: un usuario tiene una cuenta bancaria o, en términos de OOP, hay una asociación entre estas dos clases. Lo que esto significa es que, en lugar de realizar un seguimiento de un saldo directamente en la clase Usuario, resumiremos toda la información de la cuenta bancaria y asociaremos a un usuario con una instancia específica de una Cuenta bancaria.

# Para simplificar las cosas, comencemos asumiendo que cada usuario tiene una sola cuenta que comienza con un saldo de $ 0 y una tasa de interés del 2%. Esto significa que la clase Usuario, en lugar de tener directamente un atributo de saldo, ahora tendrá un atributo de tipo BankAccount. Para establecer esta relación, podemos actualizar el método __init__ de nuestro Usuario a algo como esto, eliminando el atributoaccount_balance y agregando un atributoaccount:

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)	# agregó esta línea
    
    def make_deposit(self,amount):
        self.account.deposit(amount)

    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
    
    def make_transer(self,amount):
        self.account.transfer_money(amount)
        
    def new_account(self):
        self.account.create()
    
    # def view_accoun_info():
    #     self.account.

# Nota: La clase BankAccount debe estar en el mismo archivo que la clase Usuario, por lo que se reconoce la referencia a la misma. Eche un vistazo a la modularización si siente la necesidad de tener las 2 clases en archivos separados.

# Interactuamos con este nuevo atributo tal como lo hacemos con los atributos anteriores: ¡la única diferencia es que hemos definido personalmente la funcionalidad de esta clase! Conocemos los atributos y métodos disponibles para el atributo account mirando nuestra clase BankAccount.

# class User:
#     def example_method(self):
#         self.account.deposit(100)		# podemos llamar los métodos de la instancia BankAccount 
#     	print(self.account.balance)		# o acceder a sus atributos

class BankAccount:
    def __init__(self, int_rate=0, balance=0,accounts):
        self.int_rate = int_rate
        self.balance = balance
        self.accounts={}
        self.interes=0        
    # def __str__():
        return f"No ha ingresado todos los datos necesarios"
        
    def deposit(self, amount):
        self.balance += amount
        # print(f"El {self.name} {self.account_balance}")
        # print (self.account_balance)
        return self

    def withdraw(self, amount):
        if amount>self.balance:
            print(f"No puede hacer un retiro de {amount}, su saldo es de {self.balance}")
            return self
        else:
            self.balance -=amount
            return self
        
    def display_account_info(self):
        print(f"La taza de interes es del: {self.int_rate} y los intereses acumulados son: ${self.interes}, el saldo final es: ${self.balance}")
        return self

    def transfer_money (self, other_user, amount):    
        if amount>self.balance:
            print(f"No puede hacer una transferencia de ${amount}, su saldo es de ${self.balance}")
            return self        
        else:
            self.withdrawal(amount)
            other_user.deposit(amount)
            print(f"{self.name} hiso una transferencia de ${amount} a {other_user.name}")
            return self
    # def create(self):
    #     account=

Benjamin = User("Benjamin Livingstone","benjaminlivingstone@gmail.com")
# Benjamin.account=BankAccount(0.07,200)
# Benjamin.account2=BankAccount(0.05,500)

# Benjamin.account.deposit(100)		# podemos llamar los métodos de la instancia BankAccount 
# Benjamin.account.yield_interest()
# Benjamin.account.display_account_info()
# print(Benjamin.account.balance)		# o acceder a sus atributos

# Benjamin.account2.deposit(200)
# #self.account.deposit(100)	
# Benjamin.account2.yield_interest()
# Benjamin.account2.display_account_info()

Benjamin.make_deposit(100)

print(Benjamin.account.balance)
