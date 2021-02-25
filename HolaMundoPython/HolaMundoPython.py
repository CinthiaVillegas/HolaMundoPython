print("Hola Mundo")

print("==============================================")
print("=== Funciones de entrada y salida de datos ===")
print("==============================================")

nombre = input("Introduce tu nombre: ")
print(f"Mucho gusto, {nombre}")

print("==============================================")
print("=== Variables con diferentes datos(tipado dinamico) ===")
print("==============================================")
 
#Variable
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


