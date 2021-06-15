
# Asignatura: usuario
# Objetivos:
# Practica crear una clase y crear instancias a partir de ella
# Practica el acceso a los métodos y atributos de diferentes instancias.
# Si has estado siguiendo, utilizará la clase de usuario que hemos estado discutiendo para esta tarea.

# Para esta tarea, agregaremos algunas funcionalidades a la clase Usuario:

# make_withdrawal (self, amount) #: haz que este método disminuya el saldo del usuario en la cantidad especificada
# display_user_balance (self) #: haz que este método imprima el nombre del usuario y el saldo de la cuenta en el terminal
# p.ej. "Usuario: Guido van Rossum, Saldo: $ 150
# BONIFICACIÓN: transfer_money (self, other_user, amount) : haz que este método disminuya el saldo del usuario en la cantidad y agrega esa cantidad al saldo de otro other_user

class User:	
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        # print(f"El {self.name} {self.account_balance}")
        # print (self.account_balance)

    def make_withdrawal(self, amount):        
        self.account_balance -=amount

    def display_user_balance(self):
        print(f"Usuario: {self.name}, Saldo: ${self.account_balance}")

    def transfer_money (self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        # print (other_user.display_user_balance())
        # print (self.display_user_balance())
        print(f"{self.name} hiso un deposito de ${amount} a {other_user.name}")
        print (f"El balance final de {monty.name} es {monty.account_balance}")
        print (f"El balance final de {guido.name} es {guido.account_balance}")

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
monty.make_withdrawal(50)
print(guido.account_balance)	# salida: 300
print(monty.account_balance)	# salida: 50
guido.display_user_balance()
monty.transfer_money(guido,50)




#-----------------------------------------------------------------------------------------------------------------------------------

# Qué son los objetos? ¿Qué es una clase?
# ¿Qué son las propiedades / métodos?
# ¿Qué es el self?
# ¿Por qué es importante la POO?
# Claudia Quintana to Everyone (8:55 PM)
# 1. ¿Qué son los objetos? ¿Qué es una clase?
# Una clase es como un plan que asegura la creación consistente de instancias.
# Me to Everyone (8:58 PM)
# Una clase es una plantilla para la creación de objetos de datos según un modelo predefinido. Las clases se utilizan para representar entidades o conceptos. ... Cada objeto creado a partir de la clase se denomina instancia de la clase. Las clases son un pilar fundamental de la programación orientada a objetos.
# Claudia Quintana to Everyone (8:59 PM)
# objetos o instancias: Cada vez que declaramos una variable, estamos creando una instancia de una clase, y este objeto o instancia sigue el patr[on definido por su clase
# Gonzalo Ibarra to Everyone (9:00 PM)
# ¿Qué es el self?, se trata de una referencia al objeto cuyo método es llamado
# Claudia Quintana to Everyone (9:01 PM)
# ¿Qué son las propiedades / métodos? Atributos: características compartidas por todas las instancias del tipo de clase.
# Métodos: acciones que puede realizar un objeto. Un usuario, por ejemplo, debería poder hacer un depósito o un retiro, o tal vez enviar dinero a otro usuario.
# Me to Everyone (9:01 PM)
# Una propiedad es un identificador con un determinado tipo de dato que accede normalmente a un campo en forma directa o a través de un método.
# Me to Everyone (9:02 PM)
# Los métodos representan acciones que puede realizar un objeto. Por ejemplo, un objeto “Automóvil” puede tener definidos los métodos “MotorArranque,” “Tracción” y “Parada”. Los métodos se definen al agregar procedimientos (subrutinas o funciones) a la clase.
# Me to Everyone (9:03 PM)
# La POO es muy potente porque nos permite modelar de manera sencilla datos y comportamientos complejos del mundo real. Al poder manejar los datos y los comportamientos de cada objeto de manera independiente nos evita tener que mantener datos globales y coordinar todo eso.