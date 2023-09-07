# -*- coding: utf-8 -*-
"""
@author: JHON TORRES -> https://www.classgap.com/es/tutor/jhon-torres
Youtube -> Jhon Torres Robotica 
"""
import sqlite3 as sql

def crear_base_datos():
    con = sql.connect("UserDB.db")
    con.commit()
    con.close()
    
def crear_tabla():
    con = sql.connect("UserDB.db")
    cursor = con.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            edad INTEGER NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    con.commit()
    con.close()

def agregar_usuario(nombre, edad, email):
    con = sql.connect("UserDB.db")
    cursor = con.cursor()
    cursor.execute('''
        INSERT INTO usuarios (nombre, edad, email) VALUES (?, ?, ?)
    ''', (nombre, edad, email))
    con.commit()
    con.close()
    
def obtener_usuarios():
    con = sql.connect("UserDB.db")
    cursor = con.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    con.close()
    return usuarios

def actualizar_usuario(id_usuario, nombre, edad, email):
    con = sql.connect("UserDB.db")
    cursor = con.cursor()
    cursor.execute('''
        UPDATE usuarios
        SET nombre=?, edad=?, email=?
        WHERE id=?
    ''', (nombre, edad, email, id_usuario))
    con.commit()
    con.close()

def eliminar_usuario(id_usuario):
    con = sql.connect("UserDB.db")
    cursor = con.cursor()
    cursor.execute('DELETE FROM usuarios WHERE id=?', (id_usuario,))
    con.commit()
    con.close()