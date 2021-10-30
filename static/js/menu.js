btn_deseo=document.querySelector('.producto article p span')

btn_deseo.addEventListener('click', () =>{
    window.location.href='/registro'
})

function agregar_deseo(){
    input_usuario = document.getElementById('usuario')
    input_correo = document.getElementById('correo')
    input_contrasena = document.getElementById('contrasena')
    input_confirmar_contrasena = document.getElementById('confirmar_contasena')