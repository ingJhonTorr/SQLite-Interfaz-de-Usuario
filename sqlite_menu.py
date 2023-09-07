# -*- coding: utf-8 -*-
"""
@author: JHON TORRES -> https://www.classgap.com/es/tutor/jhon-torres
Youtube -> Jhon Torres Robotica 
"""

from sqlite1 import *

def mostrar_menu():
    print("\n------------------------------\n----- MENU BASE DE DATOS -----\n")
    print("1. Crear base de datos")
    print("2. Crear tabla de usuarios")
    print("3. Agregar registro")
    print("4. Ver todos los registros")
    print("5. Actualizar registro")
    print("6. Eliminar registro")
    print("7. Salir\n")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción entre 1 y 7:\n")

        if opcion == "1":
            try:
                crear_base_datos()
                print("Base de datos creada exitosamente.")
            except:
                print("La Base de datos ya ha sido creada!")

        elif opcion == "2":
            try:
                crear_tabla()
                print("Tabla de usuarios creada exitosamente.")
            except:
                print("Tabla de usuarios ya ha sido creada!")                    

        elif opcion == "3":
            nombre = input("Ingrese el nombre del usuario:\n")
            edad = int(input("Ingrese la edad del usuario:\n"))
            email = input("Ingrese el email del usuario:\n")
            try:
                agregar_usuario(nombre, edad, email)
                print("Usuario agregado correctamente.")
            except:
                print("Error agregando un nuevo usuario!")

        elif opcion == "4":
            try:
                usuarios = obtener_usuarios()
                for usuario in usuarios:
                    print(usuario)
            except:
                print("Error al ver los registros de la tabla!")

        elif opcion == "5":
            id_usuario = int(input("Ingrese el ID del usuario a actualizar:\n"))
            nombre = input("Ingrese el nuevo nombre del usuario:\n")
            edad = int(input("Ingrese la nueva edad del usuario:\n"))
            email = input("Ingrese el nuevo email del usuario:\n")
            try:
                actualizar_usuario(id_usuario, nombre, edad, email)
                print("Usuario actualizado correctamente.")
            except:
                print("Error actualizando un usuario!")

        elif opcion == "6":
            id_usuario = int(input("Ingrese el ID del usuario a eliminar:\n"))
            try:
                eliminar_usuario(id_usuario)
                print("Usuario eliminado correctamente.")
            except:
                print("Error eliminando un usuario!")

        elif opcion == "7":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, elija una opción válida (1-7).")

if __name__ == "__main__":
    main()