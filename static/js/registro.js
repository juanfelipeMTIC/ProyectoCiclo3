btn_iniciar_sesion=document.querySelector('.regresar p span')

btn_iniciar_sesion.addEventListener('click', () =>{
    window.location.href='/login'
})

function validar_formulario_registro(){
    input_usuario = document.getElementById('usuario')
    input_correo = document.getElementById('correo')
    input_contrasena = document.getElementById('contrasena')
    input_confirmar_contrasena = document.getElementById('confirmar_contasena')

    if (!validar_contrasena(input_usuario.value)){
        alert('El campo usuario no debe contener espacios en blanco')
        return flase
    }
    if (!validar_correo(input_correo.value)){
        alert('Correo no válido')
        return flase
    }
    if (!validar_contrasena(input_contrasena.value)){
        alert('La contraseña debe contener al menos una mayúscula, una minúscula, un número, un caracter especial y mínimo 8 caracteres en total')
        return flase
    }
    if (input_contrasena.value != input_confirmar_contrasena.value){
        alert('Las contraseñas no coinciden')
        return false
    }
}

function validar_usuario(usuario){
    if (/^\S*$/i.test(usuario)){
        return true
    } else {
        return flase
    }
}

function validar_correo(correo) {
    if (/^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/i.test(correo)) {
        return true
    } else {
        return false
    }
}

function validar_contrasena(contrasena){
    if(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/i.test(contrasena)){
        return true
    } else {
        return false
    }
}