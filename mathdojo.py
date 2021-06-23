# Asignatura: MathDojo
# Objetivos:
# Practica creando una clase y creando nuevas instancias
# Practica los métodos de encadenamiento
# Practica escribir funciones flexibles que pueden tomar un número variable de argumentos.
# Crea una clase de Python llamada MathDojo que tenga un atributo, resultado y 2 métodos: sumar y restar . Los 2 métodos deben tomar al menos 1 parámetro, pero podrían tomar muchos más.

class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result=self.result+num
        for num in nums:
            self.result=self.result+num
        return self
    def subtract(self, num, *nums):
        self.result=self.result-num
        for num in nums:
            self.result=self.result-num
        return self     
# crear una instruccion:
md = MathDojo()

# x=md.add(2).add(5).add(7).result
# x=md.add(2).add(5).add(7).result
# x=md.subtract(2).subtract(5).subtract(7)

x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# debe imprimir 5

# corre cada uno de los metodos algunos mas veces y valida el resultado!

#  Crear una clase de MathDojo
#  Escriba el método add y pruébelo llamándolo 3 veces, con diferentes números de argumentos cada vez
#  Escriba el método de subtract y pruébelo llamándolo 3 veces, con diferentes números de argumentos cada vez
#  Asegúrese de poder encadenar los métodos como se demostró anteriormente
#  BONUS: Calcule la desviación estandar (existe alguna diferencia)