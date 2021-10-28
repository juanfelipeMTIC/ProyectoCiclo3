from flask import Flask, render_template, request 
import werkzeug.security as ws #libreria para guardar contraseñas
#import db

app=Flask(__name__)
app.secret_key = 'mi_clave_secreta'

@app.route('/')
def inicio():
    return render_template('base.html')

@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    else:
        print(request.form) #validar
        return render_template('perfil.html')
    

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method=='GET':
        return render_template('registro.html')
    else:
        print(request.form) #validar
        nombre = request.form('nombre')
        usuario = request.form('usuario')
        correo = request.form('correo')
        contrasena = request.form('contrasena')
        confirmar_contrasena = request.form('confirmar_contrasena')
        
        #db.insertar_usuario(nombre, usuario, correo, ws,ws.generate_password_hash(contrasena)) #se debe validar la contraseña al igual que se hizo en registro.html
        
        return 'Registro éxitoso'

@app.route('/busqueda')
def buscar():
    return render_template('busqueda.html')
