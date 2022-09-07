# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 13:05:46 2022

@author: Angie Reina
"""

from classes.menu import *
from classes.equipo import *
from classes.prestamo import *

    
def main():
    menu = Menu("Escuela de Ingeniería")
    op=menu.ver()
    if op == "1":
        menu2 = MenuTecnicos()
        op2 = menu2.ver()
        if op2 == "1":
            e = CrearEquipo()
            e.save()
        elif op2 =="2":
            p = crearPrestamo()
            p.save()
        elif op2 =="3":
            registroMantenimiento()
        elif op2 =="4":
            registroEntrega()
        elif op2 =="5":
            ver_todos_los_prestamos()
        else:
            print("Opción inválida")
            main()
            
    elif op =="2":
        menu2=MenuEstudiantes()
        op2=menu2.ver()
        if op2=="1":
            verPrestamos()
            
        elif op2=="2":
            consultarEquipo()

           
    elif op=="3":
        exit()
        
    main()
 
    
    
if __name__=='__main__':
    main()
    
    
    
    #ultima fecha de mantenimiento + ciclo = cuando hay que hacer el mantenimiento 