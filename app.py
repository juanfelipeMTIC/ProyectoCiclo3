from ast import Str
from flask import Flask, render_template, request, session, redirect
import werkzeug.security as ws
from werkzeug.utils import redirect  # libreria para guardar contraseñas
import db

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta'





@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/perfil')
@app.route('/perfil/<usuario>')
def perfil(usuario = None):
    if usuario:
        print('inicio valido')
        registro_usuario = db.obtener_registros('Usuarios', "usuario = '{}'".format(usuario))

        if registro_usuario:
            id_usuario = registro_usuario[0][0]
            
            agregar = False            
            if usuario == session['usuario']:
                agregar = True

            return render_template('perfil.html', usuario = registro_usuario)
            #return usuario
        else:
            usuario = session['usuario']

            return redirect('/perfil/{}'.format(usuario))
            #return usuario
    else:
        print('failed user')
        return render_template('perfil.html')


@app.route('/cerrar_sesion')
def cerrarSesion():
    if 'usuario' in session:
        session.pop('usuario')
    return redirect('/login')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/iniciar_sesion', methods=['POST'])
def iniciarSesion():    
    usuario = request.form['usuario']
    contraseña = request.form['contrasena']    

    registro_usuario = db.obtener_registros('Usuarios', "usuario = '{}'".format(usuario))
    if(registro_usuario):
        contraseñaDb = registro_usuario[0][4] #registro_usuario es un vector, [0] es la fila del usuario
        #4 es la posición necesaria
        inicio_exitoso = ws.check_password_hash(contraseñaDb,contraseña)
        
        if(inicio_exitoso):
            session['usuario'] = usuario
            return redirect('/perfil/{}'.format(usuario))
        else:
            return 'la contraseña o el nombre de Usuario son incorrectos'
    else:
        return 'El usuario no existe'


@app.before_request
def peticion_previa():
    if('usuario' not in session and request.endpoint in ['perfil', 'deseos']):
        print("usuario fuera de sesion")
        return redirect('/login')
    elif 'usuario' in session and request.endpoint in ['login', 'registro']:        
        print("usuario en sesion")
        print(session['usuario'])
        return redirect('/perfil/{}'.format(session['usuario']))
        

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

    db.insert_usuario(nombre, usuario, correo, ws.generate_password_hash(contraseña))
    session['usuario'] = usuario            
    return redirect('/perfil/{}'.format(usuario))


@app.route('/busqueda')
def buscar():
    return render_template('busqueda.html')


@app.route('/menu')
def menu():
    lista = db.obtener_productos('Productos')
    longitud = len(lista)
    return render_template('menu.html', listaProductos = lista, leng = longitud)    

@app.route('/deseos')
def deseos():
    return render_template('deseos.html')

@app.route('/pedido')
def pedido():
    return render_template('pedido.html')

@app.route('/pedir', methods=['POST'])
def pedir():
    producto = request.form['nombre']
    cantidad = request.form['cantidad']
    precioUnitario=db.obtener_registro('Productos', 'nombre="{}"'.format(producto))
    respuesta=0
    for i in precioUnitario:
        respuesta= respuesta + int(i)
    precioTotal=respuesta* int(cantidad)
    #return(str(precio))

    db.insert_pedido(producto, cantidad, precioUnitario, precioTotal)
    return ('Pedido realizado con Éxito')

if __name__ == '__main__':
    app.run(debug=True)

