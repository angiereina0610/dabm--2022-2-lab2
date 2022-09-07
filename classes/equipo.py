# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 13:04:27 2022

@author: Angie Reina
"""

from tabulate import tabulate
class Equipo:
    file = "database/equipos.csv"
    def __init__(self, nombre, proveedor, cantidad, referencia, ciclo, fum=""):
        self.nombre = nombre
        self.proveedor = proveedor
        self.cantidad = cantidad
        self.referencia = referencia
        self.ciclo = ciclo
        self.fum = fum   #Fecha ultima de mantenimiento 


    def verDatos(self):
        header = ["NOMBRE", "REFERENCIA", "CANTIDAD", "PROVEEDOR", "CICLO", "FUM"]
        datos=[[self.nombre, self.referencia,self.cantidad , self.proveedor, self.ciclo, self.fum]]
        print(tabulate(datos, header, tablefmt="grid"))
        
        
    def save(self):
        f = open(self.file , 'a')
        linea = ";".join([self.nombre,self.referencia,self.cantidad,self.proveedor,self.ciclo,self.fum])
        f.write(linea+"\n")
        f.close()
        
    def consulta(self , nombre):
        pass



def CrearEquipo():
    print("REGISTRAR NUEVO EQUIPO")
    nombre_equipo = input("Nombre de equipo:")
    proveedor = input("Proveedor:")
    referencia = input("Referencia:")
    ciclo = input("Ciclo de mantenimiento (dias):")
    cantidad = input("Cantidad:")
    fum=input("Fecha  de último mantenimiento(yyyy-mm-dd):")

    e = Equipo(nombre_equipo, proveedor, referencia, ciclo,cantidad , fum)
    
    return e

def consultarEquipo():
    print("CONSULTA DE EQUIPOS".center(50,"*"))
    nom_equip = input("Ingrese por favor el nombre del equipo:")
    datos1 = get_all_equipos()
    cont=0
    
    datos2=",".join(datos1)
    
    if nom_equip in datos2:
        for l in datos1:
            if nom_equip in l:
                datos1 =l.split(";")
                cont = int(datos1[4])
                if cont > 0:
                    print("El equipo existe en la base de datos y hay " + str (cont) + "  equipos")
                else:
                    print("El equipo no esta en la base de datos")
                return cont
    
def registroMantenimiento():
    
    listaEquipos = getAllEquipos()
    #print(listaEquipos)
    equipo = input("Equipo:")
    fum = input("Fecha último mantenimiento:")
    
    pos = 0
    for e in listaEquipos:
        #print(e)
        if equipo in e :
            datosEquipo = e.split(";")
            #print(datosEquipo)
            datosEquipo[5] = fum + "\n"
            listaEquipos[pos] = ";".join(datosEquipo)
        pos+=1
        
    saveAllEquipos(listaEquipos)
    
    
def saveAllEquipos(equipos):
    a = open('database/equipos.csv','w')
    for e in equipos:
        a.write(e)
    a.close()
    
def getAllEquipos():
    a = open('database/equipos.csv','r')  #lectura de archivos
    datos = a.readlines()
    return datos

def registroEntrega():
    pass
def ver_todos_los_prestamos():
    a = open("database/prestamos.csv","r") 
    prestamos = a.readlines()
    header = ["NOMBRE","CARNET","EQUIPO","FECHA DE PRESTAMO","FECHA DE ENTREGA"]
    
    matriz = []

    for l in prestamos:
        l = l.replace("\n" , "")
        l = l.split(';')
        matriz.append(l)
        
    print(tabulate(matriz,header,tablefmt="grid"))
def get_all_equipos():
    a=open("database/equipos.csv","r")
    datos=a.readlines()
    return datos