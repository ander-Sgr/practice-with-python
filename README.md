<div align="center">
<h1>LAB - 02 -PYTHON</h1>
</div>

## 💡  Acerca de la práctica

> _El objetivo de este lab es familiarizarse con python, y de esta forma entender como funcionan las estrcuturas basicas, manejar listas y diccionarios, ficheros y realizar debug a traves del uso de logging._
 
 
Con este lab pondremos en práctica la implementación de registros con la bibliotica `logging` de python, con el uso de esta biblioteca podremos hacer trazas en nuestro código, de esta forma podremos ver posibles errores o simplemnete ve el flujo de ejecución de nuestro programa. Realizaremos llamadas a una API para tratar esos datos y procesarlos con listas y diccionarios. Así como el manejo del sistema de ficheros y la persistencia de los mismos.


## 🛠 Implementación

### Logging

Por defecto el logogin de la aplicación ha de estar a nivel de `WARNING` este registro indica que el sistema funciona correctamente o se predicr un problema futuro.

Ya que nuestro programa recibe argumentos, si pasamos como argumento verbosity `(-v)` el nivel de logging baja hasta `DEBUG`

Para poder realizar esta funcionalidad verificamos si el argumento verbosity está activo o no y dependiendo del pase de argumentos el nivel de logging cambia 

```python
 log_level = logging.WARNING
    if verbosity:
        log_level = logging.DEBUG
    logging.basicConfig(level=log_level, format='%(levelname )s - %(message)s')
```
A la hora de realizar los registros se mostrarán las trazas `urllib3` estas trazas nos muestran mensajes de error sobre una opreación HTTP, detalles de solicitud como los headers y para evitar que aparezcan tenemos que  obtener ese registro en concreto y filtrarlo solo a nivel de `WARNING` de esta forma solo mostrará eventos de registros y errores.

```python
    filter_urllib3 = logging.getLogger('urllib3')
    filter_urllib3.setLevel(logging.WARNING)
```

### Datos de usuarios

Para hacer llamadas HTTP usaremos la libreria `requests`. Usaremos el endopint siguiente

```py
 endpoint = f"https://random-data-api.com/api/v2/users?size={count_users}"
```

Tendremos que recuperar X cantidad de usuarios y procesarlos. 

Para procesar esos datos lo que hemos hecho es guarddarlos en una List de obejetos Persona. Esta lista solo contendrá Nombre, Apellido, Estado, País

```py
    persons = []
    for user in json_data:
        person = Person(
            user['last_name'],
            user['first_name'],
            user['address']['country'],
            user['address']['state']
        )
        persons.append(person)
```

### Manejo de ficheros


