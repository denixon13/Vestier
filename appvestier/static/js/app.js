document.addEventListener('DOMContentLoaded', function(){

    eventListeners();
    actualizarStock();
    incrementar();
    decrementar();

});

function eventListeners(){
    const menuOpciones = document.querySelector(".menu-opciones");
    const btnSingup = document.getElementById("btn-sign-up");
    const header = document.querySelector("header");
    const controlesUsuario = document.querySelector(".controles-usuario");
    const contenedor = document.querySelector(".navegacion2")
    const btnMenu = document.getElementById("btn-menu");
    const trigger = document.querySelector('.usuario-trigger');
    const dropdown = document.querySelector('.usuario-dropdown');

    //Barra de busqueda 
    const iconoBusqueda = document.querySelector('ion-icon[name="search"]');
    const barraBusqueda = document.getElementById('barra-busqueda');
    const cerrarBusqueda = document.getElementById('cerrar-busqueda');
    const nav1 = document.querySelector('.navegacion1');
    const nav2 = document.querySelector('.navegacion2');

    if (iconoBusqueda && barraBusqueda && cerrarBusqueda) {
        iconoBusqueda.addEventListener('click', function () {
            barraBusqueda.classList.add('visible');
            nav1.classList.add('oculto');
            nav2.classList.add('oculto');
        });

        cerrarBusqueda.addEventListener('click', function () {
            barraBusqueda.classList.remove('visible');
            nav1.classList.remove('oculto');
            nav2.classList.remove('oculto');
        });
    }

    btnMenu.addEventListener("click", ()=>{
        menuOpciones.classList.toggle("mostrar"); // Alterna la clase "mostrar" en el menú de opciones
        responsiveY(); // Llama a la función responsiveY para ajustar el menú de opciones
    })

    const responsiveY = ()=>{
        if(window.innerHeight<=362){
            if(menuOpciones.classList.contains("mostrar")){
                menuOpciones.classList.add("min"); // Añade la clase "min" al menú de opciones si la altura de la ventana es menor o igual a 362px
            }
            else{
                menuOpciones.classList.remove("min"); // Elimina la clase "min" del menú de opciones si la altura de la ventana es mayor a 362px
            }
        }
        else{
            menuOpciones.classList.remove("min");
        }
    }

    const responsive = ()=>{
        if (btnSingup){
            if(window.innerWidth <=865){
                menuOpciones.children[0].appendChild(btnSingup); // Mueve el botón de "iniciar sesion" al final del menú de opciones
                header.appendChild(menuOpciones); // Mueve el menú de opciones al header
            }
            else{
                controlesUsuario.appendChild(btnSingup); // Vuelve a mover el botón de "iniciar sesion" a los controles de usuario
                contenedor.appendChild(menuOpciones); // Vuelve a mover el menú de opciones a la barra de navegación
            }
        }
        

        responsiveY();
    }
    responsive();

    window.addEventListener("resize", responsive); // Reaplica el responsive al cambiar el tamaño de la ventana

    //menu-usuario
    if (trigger && dropdown) {
        trigger.addEventListener('click', function (e) {
            e.stopPropagation();
            dropdown.classList.toggle('activo');
        });

        document.addEventListener('click', function (e) {
            if (!trigger.contains(e.target) && !dropdown.contains(e.target)) {
                dropdown.classList.remove('activo');
            }
        });
    }


};

let stockDisponible = 0;

function  actualizarStock(radio){
    stockDisponible = parseInt(radio.dataset.stock);
    document.getElementById('cantidad').value = 1;
    document.getElementById('cantidad').max = stockDisponible;
    document.getElementById('stock-info').innerText = `Stock disponible: ${stockDisponible}`;
}

function incrementar(){
    const input = document.getElementById('cantidad');
    let actual = parseInt(input.value);
    if(actual < stockDisponible){
        input.value = actual + 1;
    }
}

function decrementar(){
    const input = document.getElementById('cantidad');
    let actual = parseInt(input.value);
    if(actual > 1){
        input.value = actual - 1;
    }
}