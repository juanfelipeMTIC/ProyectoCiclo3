alert('Sesion correcta');
let btn_cerrar_sesion = document.querySelector('#cerrar_sesion');
btn_cerrar_sesion.addEventListener('click', () => {
    location.href = '/cerrar_sesion';
})