# python_project_lvilla

El programa contiene una app inicio por el cual pasan todas las url del programa en su archivo urls.py. 

La app inicio cuenta con 3 vistas en el archivo views.py que cada una lleva a un template distinto
    La primer vista solo renderiza el template asociado al home del programa.
    las siguientes 2 vistas de registro e iniciar sesion estan asociadas c/u a su respectivo template. Estas vistas/funciones funcionan de manera similar

    Registrarse: al ingresar a esta funcion mediante GET crea un formulario y lo renderiza en su template, si se ingresa a esta funcion mediante POST guardara
    los datos del nuevo usuario en la BBDD, en el espacio de user's .

    Iniciar sesion: Para poder iniciar sesion es necesario registrarse previamente y lo que validará el inicii de sesion es si se encuentra el mail que se ingresa en el form de inicio de sesion en la BBDD. 

Para crear los formularios que renderizan los templates de registro e inicio de sesion se utilizaron clases contenidas en el archivo forms.py que luego se importaron en el archivo de vistas views.py para su uso.
Para crear datos en la BBDD se crearon clases en el archivo models.py . La clase article servira para crear el contenido (que van a ser tipo textos/noticias) de la web.

el static.html es el html padre 