btn_registrate=document.querySelector('.registro p span')

btn_registrate.addEventListener('click', () =>{
    window.location.href='/registro'
})

let img_mostrar_contrasena = document.getElementById('ver_contrasena');
ver_click(img_mostrar_contrasena, 'contrasena')

function ver_click(boton, id_input) {
  boton.addEventListener("click", () => {
    let input_contrasena = document.getElementById(id_input);
    let tipo_input_contrasena = input_contrasena.getAttribute("type");

    if (tipo_input_contrasena == "password") {
      input_contrasena.setAttribute("type", "text");
      boton.setAttribute("src", "/static/img/Close_eye.png");
    } else {
      input_contrasena.setAttribute("type", "password");
      boton.setAttribute("src", "/static/img/Open_eye.png");
    }
  });
}