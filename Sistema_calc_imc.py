import os
import csv
import msvcrt
#colección imcs
listaimc = []
#F para programa

#1Calcular IMC
def calcularimc(peso,altura):
    res = peso/(altura**2)
    return res
#2 Verificar estado del imc
def estadoimc(resultado):
    if resultado < 18.5:
        return "bajo peso"
    elif resultado >= 18.5 and resultado <= 24.9:
        return "adecuado"
    elif resultado >= 25 and resultado <= 29.9:
        return "sobrepeso"
    elif resultado >= 30 and resultado <= 34.9:
        return "obesidad grado 1"
    elif resultado >= 35 and resultado <= 39.9:
        return "obesidad grado 2"
    else:
        return "obesidad grado 3"
    
#3 Imprimer IMC en lista
def imprimirReporte(archivo, lista):
    with open(archivo, 'w', newline='', encoding='utf-8') as a:
        escribir = csv.writer(a, delimiter=",")
        escribir.writerows(lista)
    
while True:
    print("<<press key>>")
    msvcrt.getch()
    os.system("cls")
    nombre = input("Ingrese nombre: ")
    peso = float(input("Ingrese su peso: "))
    altura = float(input("Ingrese su altura: "))
    imc = calcularimc(peso,altura)
    print(f"su imc es: {imc}")
    estado = estadoimc(imc)
    print(estado)

    listaimc.append([nombre, imc, estado])
    imprimirReporte('reporte_imc.csv',listaimc)

    resp = input("Desea salir? s/n: ").lower()
    if resp =="s":
        break