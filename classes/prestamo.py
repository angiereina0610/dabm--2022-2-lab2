# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 13:05:13 2022

@author: Angie Reina
"""

from tabulate import tabulate

class Prestamo:
    file = "database/prestamos.csv"
    
    def __init__(self ,nombre ,carnet , equipo ,fechap , fechae):
        self.nombre = nombre 
        self.carnet = carnet 
        self.equipo = equipo
        self.fechap = fechap
        self.fechae = fechae 
    
    def save(self):
        f = open(self.file,'a')
        linea = ";".join([self.nombre , self.carnet , self.equipo , self.fechap , self.fechae])
        f.write(linea+"\n")
        f.close()
        
def crearPrestamo():
    print("REGISTRAR PRESTAMO")
    nombre = input("Nombre del estudiante:")
    carnet = input("Carnet:")
    equipo = input("Equipo:")
    fechap = input("Fecha de prestamo(yyyy-mm-dd):")
    fechae = input("Fecha de entrega(yyy-mm-dd):")
    p = Prestamo(nombre,carnet,equipo,fechap,fechae)
    return p        
    
def verPrestamos():
    a = open("database/prestamos.csv","r") 
    prestamos = a.readlines()
    header = ["NOMBRE","CARNET","EQUIPO","FECHA DE PRESTAMO","FECHA DE ENTREGA"]
    
    matriz = []
    
    carnet_Est = input("Digite por favor el número del carnet:")
    
    for l in prestamos:
        l = l.replace("\n" , "")
        l = l.split(';')
        matriz.append(l)
        
    #print(tabulate(matriz,header,tablefmt="grid"))

    matriz2 = []
    
    for l in range(0 , len(matriz)):
        if matriz[l][1] == carnet_Est:
            matriz2.append(matriz[l])
    print(tabulate(matriz2,header,tablefmt="grid"))

def registroEntrega():
    datos=get_all_prestamos()
    carnet=input("Ingrese carnet de estudiante: ")
    equipo=input("Ingrese equipo devuelto: ")
    for e in datos:
        if equipo in e:
            if carnet in e:
                datos.remove(e)
            else:
                print("Prestamo no registrado en la base de datos")
    save_all_prestamo(datos)
    
def save_all_prestamo(datos):
    a=open("database/prestamos.csv","w")
    for e in datos:
        a.write(e)
    a.close() 
    
def get_all_prestamos():
    a=open("database/prestamos.csv","r")
    datos=a.readlines()
    return datos    
    
    
        