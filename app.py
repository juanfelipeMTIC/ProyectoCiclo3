from flask import Flask, render_template, request
import werkzeug.security as ws
from werkzeug.utils import redirect  # libreria para guardar contraseñas
#import db

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta'


@app.route('/')
def inicio():
    return render_template('inicio.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        print(request.form)  # validar
        return render_template('perfil.html')


@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/registro_usuario', methods=['POST'])
def registrarUsuario():
    nombre = request.form['nombre']
    usuario = request.form['usuario']
    correo = request.form['correo']
    contraseña = request.form['contrasena']
    confirmar_contraseña = request.form['confirmar_contrasena']
    return redirect('/login')


@app.route('/busqueda')
def buscar():
    return render_template('busqueda.html')


@app.route('/menu')
def menu():
    return render_template('menu.html')


if __name__ == '__main__':
    app.run(debug=True)
