btn_iniciar_sesion = document.querySelector(".regresar p span");

btn_iniciar_sesion.addEventListener("click", () => {
  window.location.href = "/login";
});

function validar_formulario_registro() {
  let input_nombre = document.getElementById("nombre");
  let input_usuario = document.getElementById("usuario");
  let input_correo = document.getElementById("correo");
  let input_contrasena = document.getElementById("contrasena");
  let input_confirmar_contrasena = document.getElementById(
    "confirmar_contrasena"
  );

  console.log(input_nombre.value);
  console.log(input_usuario.value);
  console.log(input_correo.value);
  console.log(input_contrasena.value);
  console.log(input_confirmar_contrasena.value);

  if (!validar_nombre(input_nombre.value)) {
    alert("El campo Nombre no puede estar vacío");
    return false;
  }

  if (!validar_usuario(input_usuario.value)) {
    return false;
  }

  if (!validar_correo(input_correo.value)) {
    alert("Correo no válido");
    return false;
  }

  if (input_contrasena.value != input_confirmar_contrasena.value) {
    alert("Las contraseñas no coinciden");
    return false;
  }

  if (!validar_contrasena(input_contrasena.value)) {
    alert(
      "La contraseña debe contener al menos una mayúscula, una minúscula, un número, un caracter especial y mínimo 8 caracteres en total"
    );
    return false;
  }

  alert("Registro exitoso");
}

function validar_nombre(nombre) {
  return !(nombre.length == 0);
}

function validar_usuario(usuario) {
  if (/^[a-zA-Z\-]+$/.test(usuario)) {
    return true;
  } else if (usuario.length == 0) {
    alert("El campo Usuario no puede estar vacío");
    return false;
  } else {
    alert("El campo usuario no debe contener espacios en blanco");
    return false;
  }
}

function validar_correo(correo) {
  if (
    /^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i.test(correo)
  ) {
    return true;
  } else {
    return false;
  }
}

function validar_contrasena(contrasena) {
  if (
    /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/i.test(
      contrasena
    )
  ) {
    return true;
  } else {
    return false;
  }
}

let img_mostrar_contrasena = document.getElementById('ver_contrasena');
let img_mostrar_confirmar_contrasena = document.getElementById('ver_confirmar_contrasena');

ver_click(img_mostrar_contrasena, 'contrasena')
ver_click(img_mostrar_confirmar_contrasena, 'confirmar_contrasena')

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
