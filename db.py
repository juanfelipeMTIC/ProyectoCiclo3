import sqlite3
from sqlite3 import Error

def obtener_conexion():
    try:
        conexion = sqlite3.connect('db/DrinkApp.db')
        return conexion
    except Error:
        print(Error)