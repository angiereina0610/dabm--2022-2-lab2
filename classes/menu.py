# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 13:04:49 2022

@author: Angie Reina
"""

from datetime import datetime , timedelta
class Menu:
    def __init__(self, laboratorio):
        self.laboratorio=laboratorio
    
    def ver(self):
        print("BIENVENIDO AL SISTEMA".center(50,"*"))
        print("Laboratorio:"+self. laboratorio)
        print("1.Tecnicos")
        print("2.Estudiantes")
        print("3.Salir")      
        op=input(">>>")
        
        return op 
    
class MenuTecnicos:
    def ver(self):
        print("MENU TECNICOS DE LABORATORIO".center(50,"*"))
        print("1.Registrar equipos")
        print("2.Registrar prestamo")
        print("3.Registrar mantenimiento")
        print("4.Registrar entrega")
        print("5.Ver todos los prestamos")
        op=input(">>>")

        return op
   

'''if __name__=='__main__' :
    menu= Menu("Escuela de Ingnieros")
    op=menu.ver()
    if op=="1":
        menu2=MenuTecnicos()
        op2=menu2.ver()'''
        
        
class MenuEstudiantes:
    def ver(self):
        print("MENU ESTUDIANTES".center(50 , "*"))
        print("1.Consultar equipos en prestamo")
        print("2.Disponibilidad de los equipos")
        op=input(">>>")
        
        return op
if __name__=='__main__' :
            menu= Menu("Escuela de ingenieros")
            op=menu.ver()
            if op=="1":
                menu2=MenuTecnicos()
                op2=menu2.ver()
            if op =="2":
                menu2=MenuEstudiantes()
                op2=menu2.ver()

        

   