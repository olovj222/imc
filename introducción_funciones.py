"""Las funciones son fragmentos de codigos que podemos reutilizar cda vez que necesitemos.
Permiten fragmentación o modular el desarrollo de una apliación
para utilizar funcion llamamos por su nombre

Existen 2 tipos:
sin retorno: que solo hacen algo y hasta ahí se pueden utilizar
con retorno: que nos entregan un valor para seguir trabajando sobre él
"""

#función para sumar 2 numeros sin retorno
def sum1(num1, num2):
    suma = num1+num2
    print(f"El resultado de la suma es {suma}")
# funcion para sumar 2 numeros con retorno
def sum2(num1, num2):
    suma= num1+num2
    return suma

sum1(20,50)
sum1(1,15)
sum1(1000,-999)
print(sum2 (40,60)*2)

def login(user: str, contrasena : str):
    if user == "Duoc" and contrasena == "Duocadmin":
        return True
    else:
        return False

user = input("Ingrese usuario: ")
contrasena = input("Ingrese contraseña: ")
if login(user, contrasena):
    print("Usuario correcto")
else:
    print("Usuario incorrecto")


#Funcion para calcular el IMC
def imc (peso, altura):
    res = peso/(altura**2)
    return res

peso = float(input("Ingrese peso: "))
altura = float(input("Ingrese altura: "))
print(imc(peso,altura) *10000)