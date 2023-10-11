###########################################
### Desarrollo de una Aplicación Python ###
###########################################

Descripción: En este proyecto, tenéis la libertad de elegir un tema de interés y desarrollar una aplicación Python.

La aplicación debe cumplir con los siguientes requisitos mínimos:

Descarga de Datos: La aplicación debe ser capaz de descargar datos JSON desde al menos una fuente en línea, como una API web o un archivo JSON remoto.

Procesamiento de Datos: Los datos JSON descargados deben ser procesados y almacenados en estructuras de datos adecuadas, como listas, diccionarios u objetos personalizados según la naturaleza de los datos.

Manipulación de Datos: Los usuarios deben poder realizar alguna forma de manipulación de datos, como búsqueda, filtrado, ordenamiento o cálculos sobre los datos descargados.

Interfaz de Usuario (Opcional): Como apartado opcional, se propone crear una interfaz de usuario simple para interactuar con la aplicación. Esto podría ser una interfaz de línea de comandos o una GUI básica.

Documentación: Debéis proporcionar documentación clara y concisa que explique cómo funciona su aplicación, cómo se ejecuta y cómo se pueden utilizar sus características. Si la aplicación tiene dependencias parafuncionar, debes explicar claramente cómo se instalan.

Control de Versiones: Se debe utilizar un sistema de control de versiones, como Git, para realizar un seguimiento de las actualizaciones del código y colaborar en el desarrollo si se trabaja en grupo.

Entorno en container (Opcional). En este apartado opcional te propongo la creación de un container con docker en el que esté todo configurado y listo para funcionar.

Presentación: Al final del proyecto, el alumnado debe presentar su aplicación y su funcionamiento ante el grupo y el profesor, destacando las características implementadas y los problemas superados. Además, deberá crear un vídeo de menos de 2 minutos con los highlights de la app.

################
### Temática ###
################

La temática de este proyecto es un rastrador de peliculas y series tv. Su funcionalidad es para que los usuarios puedan buscar información sobre las peliculas y series tv que le interese.
Para ello se va utilizar para la recogidad de la informacion de peliculas y series tv una Api. 
Cuya Api es: https://www.omdbapi.com/ (Para esta Api se necesita solicitar a la página una clave para poder tener acceso)

##############################
### Instalación Requeridad ###
##############################

Para poder usar esta aplicación dentras que tener instalado lo necesario que se indica en el fichero requirements.txt

##############################################
### Desarrollo del Código Fuente Principal ###
##############################################

Para poder desarrollar esta aplicacion se ha tenido que utilizar varias funciones para que se pueda desarrollar en condiciones el código fuente. 

A la hora de ejecutarse nuestra aplicación la primera funcion que se pondra en funcionamiento es la de main que es la función que da la llamada a las otras funciones para que pueda realizar de desarrollo. Dentro de esta función lo que tenemos es una primera variable que la declaramos para guardar nuestra clave de nuestra API que vamos a utilizar, despues de esta declaracion realizaremos un bucle while para que nos muestre un menu para que el usuario pueda realizar una de las opcion que se muestra que son las siguientes:
    Primero:  muestra un mensaje de menu de opciones.
    Segundo: muestra la primera opcion que nos muestra uan descripcion que se va a realizar cuando se introduzca ese valor.
    Tercero:  muestra la segunda opcion que nos muestra uan descripcion que se va a realizar cuando se introduzca ese valor.
    Cuarto: muestra la tercera opcion que nos muestra uan descripcion que se va a realizar cuando se introduzca ese valor.
    Quinto: se declara una variable con la que se le va asignar segun lo que introduzca el usuario.
    Sexto: despues de la declaracion de la variable anterior comprobaremos que si en la variable cumple unas condiciones que indicara en las condiciones del if.
    Septimo: dentro del if si se cumple la primera condicion se hara la llamada a la funcion de buscarPeliculaPorTitulo() sino tendra que volver a comprobar si se cumple la siguiente condicion que si la segunda condicion si la cumple hara la llamada a la funcion de buscarSeriePorTitulo() sino la cumple tampoco nos mostrara un mensaje de hasta luego y se acabara el programa. Si en la variable no se ha introducido un valor permitido nos mostrara un mensaje que solo puede introducir ciertos valores.

La funcion main() es llamada a traves de un if que nos mostrara un mensaje de bienvenida y hara la llamada a la funcion para que realize todo lo anterior que se ha explicado.

#########################################################################
### Desarrollo de la funciones de buscar pelicula o series por titulo ###
#########################################################################

