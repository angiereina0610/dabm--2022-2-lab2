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
    nombre = input("Nombre:")
    proveedor = input("Proveedor:")
    referencia = input("Referencia:")
    ciclo = input("Ciclo de mantenimiento (dias):")
    cantidad = input("Cantidad:")
    fum=input("Fecha última de mantenimiento(yyyy-mm-dd):")

    e = Equipo(nombre, proveedor, referencia, ciclo,cantidad , fum)
    
    return e

def consultarEquipo():
    print("CONSULTA DE EQUIPOS")
    nombre = input("Nombre de equipo:")
    
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

