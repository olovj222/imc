import csv
import os
import msvcrt

#Tuplas -clases
clases = [
    ("Pesas", "LUN-MIE 8:00-10:00 a.m",10),
    ("Zumba","MAR-JUE 3:30-5:40 p.m",20),
    ("Nutrición", "VIE 6:00-7:30 a.m",2),
    ("Crossfit", "SAB 11:30-12:55 p.m",10)
]

#Diccionario - usuarios
usuarios = {}
# Lista - Reservas
reservas = []
# contador para id usuario
numero_us = 100

while True:
    print("<<Press key>>")
    msvcrt.getch()
    os.system("cls")
    print("""
    SISTEMA FITLIFE
    --------------------------------------------
    1) Registrar nuevo usuario
    2) Reservar una clase y generar reporte CSV
    3) Consultar clases disponibles
    4) Consultar reservas de un usuario
    5) Consultar usuarios
    0) SALIR
    --------------------------------------------""")
    opc = input("Seleccione: ")
    #función para crear títulos
    def titulo(texto : str):
        print(f"{texto.upper()}")
    def error(texto : str):
        print(f"❌{texto.upper()}❌")
    def exito( texto : str):
        print(f"💨{texto}💨")
    if opc =="0":
        titulo("Adiós")
        break
    elif opc =="1":
        titulo("Registrar nuevo usuario")
        nombre = input("Ingrese nombre de usuario: ").title()
        #validar que nombre de usuario no se repita, "values" permite comparar respecto a valores y no llave
        if nombre not in usuarios.values():
            usuarios[numero_us] = nombre
            exito(f"Usuario {numero_us} registrado")
            numero_us +=100
        else:
            error("Usuario ya registrado")

    elif opc =="2":
        titulo("Reservar una clase y generar reporte CSV")
        codigo = int(input("Ingrese código: "))
        if codigo in usuarios:
            curso = input("Ingrese curso para inscribir: ").capitalize()
            centinelacurso = False
            centinelacupos = False
            for c in clases:
                if c[0].capitalize() == curso:
                    centinelacurso: True
                    if c[2] >0: #verificamos si hay cupos
                        centinelacupos = True
                        #REalizar reserva
                        reservas.append([codigo, usuarios[codigo], c[0],c[1]])
                        exito("Reserva realizada")
                        #descontar cupo
                        actualizacionCupo = (c[0],c[1],c[2] -1)
                        clases.remove(c)
                        clases.append(actualizacionCupo)
                        #reg en csv
                        with open('reporte_reservas.csv','w', newline='', encoding='utf-8') as a:
                            escribir = csv.writer(a, delimiter=",")
                            escribir.writerows(reservas)
                        break
            if centinelacupos == False:
                error("No hay cupos")
            if centinelacurso == False:
                error("Curso no existe")
        else:
            error("Código no existe")
    elif opc =="3":
        titulo("Consultar clases disponibles")
        for c in clases:
            print(f"{c[0]} Horario {c[1]} Cupos: {c[2]}")
    elif opc =="4":
        titulo("Consultar reservas de un usuario")
        if len(reservas)>0:
            codigo = int(input("Ingrese codigo usuario"))
            centinela = False
            for r in reservas:
                if r[0]==codigo:
                    print(f"{r[0]}{r[1]} Curso: {r[2]} Horario: {r[3]}")
                    centinela = True
            if centinela == False:
                error("el codigo no tiene reservas asociadas")
        else:
            error("No hay reservas")
    elif opc =="5":
        titulo("Listado usuarios")
        if len(usuarios)>0:
            for u in usuarios:
                print(f"{u}: {usuarios[u]}")
        else:
            error("No hay usuarios")
    else:
        error("Opción no válida")