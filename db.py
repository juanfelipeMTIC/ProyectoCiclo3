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
        strsql = 'SELECT * FROM {} WHERE{}'.format(tabla, condicion)
    else:
        strsql = 'SELECT * FROM {}'.format(tabla)

    Cursor.execute(strsql)
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