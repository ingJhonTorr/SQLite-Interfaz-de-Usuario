# -*- coding: utf-8 -*-
"""
@author: JHON TORRES -> https://www.classgap.com/es/tutor/jhon-torres
Youtube -> Jhon Torres Robotica 
"""

from sqlite1 import *

# Crea la base de datos (ejecutar solo una vez)
crear_base_datos()
# Crea la tabla (ejecutar solo una vez)
crear_tabla()

agregar_usuario('Jhon', 30, 'ingjotajota@gmail.com')
agregar_usuario('Maria', 25, 'maria@example.com')
agregar_usuario('Juan', 31, 'juan@example.com')

usuarios = obtener_usuarios()
print("\nUsuarios:")
for usuario in usuarios:
    print(usuario)
    
actualizar_usuario(2, 'Maria Gonzalez', 25, 'maria@example.com')
actualizar_usuario(3, 'Juan Perez', 32, 'juanperez@example.com')

usuarios = obtener_usuarios()
print("\nUsuarios actualizados:")
for usuario in usuarios:
    print(usuario)
    
eliminar_usuario(3)

usuarios = obtener_usuarios()
print("\nUsuarios después de eliminar:")
for usuario in usuarios:
    print(usuario)