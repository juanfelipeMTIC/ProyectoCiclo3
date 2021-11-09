import sqlite3
from sqlite3 import Error
from sqlite3.dbapi2 import Cursor

def obtener_conexion():
    try:
        conexion = sqlite3.connect('db/DrinkApp.db')
        return conexion
    except Error:
        print(Error)


def obtener_registros(tabla, condicion=None):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    if condicion:
        strsql = 'SELECT * FROM {} WHERE {}'.format(tabla, condicion)
    else:
        strsql = 'SELECT * FROM {}'.format(tabla)

    cursor.execute(strsql)
    datos = cursor.fetchall()
    conexion.close()

    return datos

def obtener_registro(tabla, condicion):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    strsql= 'SELECT precio FROM {} WHERE {}'.format(tabla, condicion)

    cursor.execute(strsql)
    datos = cursor.fetchall()
    conexion.close()

    return datos


def obtener_productos(tabla):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    strsql= 'SELECT * FROM {}'.format(tabla)

    cursor.execute(strsql)
    datos = cursor.fetchall()
    conexion.close()

    return datos

def insert_usuario(nombre, usuario, correo, contraseña):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    strsql = "INSERT INTO Usuarios (nombre, usuario, correo, contrasena) VALUES ('{}','{}','{}','{}')".format(nombre, usuario, correo, contraseña)

    cursor.execute(strsql)
    conexion.commit()
    conexion.close()


def insert_pedido(producto, cantidad, precioUnitario, precioTotal):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    strsql = "INSERT INTO Pedidos (producto, cantidad. precioUnitario, precioTotal) VALUES ('{}','{}','{}','{}')".format(producto, cantidad, precioUnitario, precioTotal)

    cursor.execute(strsql)
    conexion.commit()
    conexion.close()