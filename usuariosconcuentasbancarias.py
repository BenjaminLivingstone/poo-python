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
# Nota: La clase BankAccount debe estar en el mismo archivo que la clase Usuario, por lo que se reconoce la referencia a la misma. Eche un vistazo a la modularización si siente la necesidad de tener las 2 clases en archivos separados.

# Interactuamos con este nuevo atributo tal como lo hacemos con los atributos anteriores: ¡la única diferencia es que hemos definido personalmente la funcionalidad de esta clase! Conocemos los atributos y métodos disponibles para el atributo account mirando nuestra clase BankAccount.

# class User:
#     def example_method(self):
#         self.account.deposit(100)		# podemos llamar los métodos de la instancia BankAccount 
#     	print(self.account.balance)		# o acceder a sus atributos

class BankAccount:
    def __init__(self, int_rate=0, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        self.interes=0
    # def __str__():
        
    def deposit(self, amount):
        self.balance += amount
        return self
        
    def withdraw(self, amount):
        self.balance -=amount
        return self
        
    def display_account_info(self):
        print(f"La taza de interes es del: {self.int_rate}% y los intereses acumulados son: ${self.interes}, el saldo final es: ${self.balance}")
        return self

    def yield_interest(self):
        if (self.balance>0):
            self.interes=self.balance*self.int_rate
            return self
        else:
            print(f"A trabajar")
            return self

Benjamin = User("Benjamin Livingstone","benjaminlivingstone@gmail.com")
cuenta1=BankAccount(0.07,200)
cuenta2=BankAccount(0.05,500)

Benjamin.account.deposit(100)		# podemos llamar los métodos de la instancia BankAccount 
Benjamin.account.display_account_info()
