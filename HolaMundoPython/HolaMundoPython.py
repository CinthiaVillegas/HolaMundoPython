print("Hola Mundo")

print("==============================================")
print("=== Funciones de entrada y salida de datos ===")
print("==============================================")

nombre = input("Introduce tu nombre: ")
print(f"Mucho gusto, {nombre}")

print("==============================================")
print("=== Variables con diferentes datos(tipado dinamico) ===")
print("==============================================")
 
#Variable, el nombre de las variables tienen que iniciar con una letra
#y se puede separar con una letra mayuscula en la segunda palabra o con un guion
#bajo _. Por ejemplo: HeladoLimon, heladoLimon, helado_limon
name = "Cinthia"
age = 22
pi = 3.1416

#Impresion en pantalla de las variables declaradas
print("Nombre: ",name," Edad: ", age, " PI= ", pi)
#Impresion del tipo de dato de cada variable
print("Nombre= ",type(name)," Edad= ", type(age)," PI = ", type(pi))

#Casteo de una variable con valor entero  a una varible con valor flotante (decimal)
age = float(age)
print("Edad: ",age)
print("Edad= ",type(age))

print("==============================================")
print("==== Operaciones básicas y condiciones =======")
print("==============================================")

#Existen 3 tipos de operaciones básicas
#~Aritméticas: Suma(a+b), Resta(a-b), Multiplicación(a*b), División(a/b), Cociente de la división(a//b),
# Resto de la división(a%b), Potencia a^b (a **b) 
#~Comparación: Mayor que(>), Menor que(<), Mayor igual(>=), Menor igual(<=), igualdad(==), diferencia(!=)
#~Lógicas: and, or, not
#Los condicionales los utilizaremos para validar si se cumple una o más condiciones para ejecutar cierto bloque de código

a = float(input("Valor de A = "))
b = float(input("Valor de B = "))

print("** Variables ** A= ",a,"   B= ",b)

print("== Operaciones aritmeticas ==")

print("Suma = ", a + b)
print("Resta = ", a - b)
print("Multiplicación = ", a * b)
print("División = ", a / b)
print("Cociente = ", a // b)
print("Resto = ", a % b)
print("Potencia = ", a ** b)

print("== Operaciones de comparación ==")
if (a>b or a>=b):
 print("A es mayor igual que B")
elif (a<b or a<=b):
 print("A es menor igual que B")
elif (a==b):
 print("A tiene el mismo valor que B")


