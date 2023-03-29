# docker_services

En este tuto se explica cómo construir una arquitectura de cuatro servicios utilizando Flask, Python y Postgres como base de datos.

Para lograr que los servicios se comuniquen entre sí, se utilizará Docker para unificarlos dentro de contenedores. La idea es "Dockerizar" toda la aplicación para que cada servicio corra dentro de un contenedor y así ser más facil asegurarse de que cada uno de ellos funcione correctamente.

Al final, se creará un archivo de Docker Compose que incluirá un Dockerfile para cada servicio, lo que permitirá construir cada uno de ellos de forma independiente.

(un archivo de Docker Compose, es un archivo de configuración de Docker que permite definir, configurar y ejecutar múltiples contenedores de Docker al mismo tiempo. El archivo de Docker Compose incluirá un Dockerfile para cada servicio, lo que permitirá construir cada servicio de forma aislada, lo que puede facilitar el mantenimiento y la actualización de cada uno de ellos por separado.)

La idea es que al final del proyecto, solo necesitemos ejecutar el comando "docker-compose up" para que Docker se encargue de instalar todo y que nuestros servicios estén funcionando en nuestro equipo.

Con esto, el proyecto podrá ejecutarse en cualquier máquina que tenga Docker instalado.

## El proyecto

El proyecto consiste en cuatro servicios, y para cada servicio se debe crear un directorio que incluya el código fuente y el archivo Dockerfile correspondiente.

Para empezar, se programará la funcionalidad de cada servicio sin Docker, para que corra en la máquina local.
Una vez que se tenga la implementación de cada servicio y se haya verificado su correcto funcionamiento, se procederá a implementar el contenedor correspondiente utilizando el Dockerfile.

Una vez creado el Dockerfile correspondiente para cada servicio, el siguiente nivel es Docker Compose, que utiliza los Dockerfiles para construir y ejecutar los servicios en contenedores. Un nivel más alto es Kubernetes, que permite la gestión de los contenedores de manera más avanzada, pero este tema no se aborda en este tutorial.

## Objetivo

Cuando un usuario accede al servicio web, los datos que se graficarán serán consultados al servicio "api" y este a su vez consultará al servicio "facker", que se encargará de generar los datos falsos y de insertarlos en la base de datos.

Los resultados de las consultas se mostrarán en bloques de cinco registros y se incluirán botones para continuar y para acceder al panel de administración de la base de datos.

    Crearemos 4 servicios funcionales:
  
* Uno llamado "web", será construido con Python y Flash y su front-end estará hecho con Bootstrap, HTML y CSS.
Esta aplicación será un generador de datos falsos con ciertas características y al final se graficarán en una tabla de Bootstrap utilizando Data Table.
El servicio permitirá realizar consultas de datos desde el navegador.

* Otro servicio llamado "api" que será el intermediario entre el servicio web y api.

* Otro llamado "facker", encargado de generar los datos falsos que se mostrarán en el servicio web.

* Y por último el servicio “database” para la base de datos.

 Estos serían los pasos a grandes rasgos:

* Crear un servicio web.
* Crear un servicio API.
* Implementar la funcionalidad del servicio web para permitir consultas de datos.
* Implementar la funcionalidad del servicio API para procesar y entregar los datos solicitados.
* Mostrar los resultados en bloques de cinco registros.
* Agregar un botón para continuar.
* Agregar un botón para ir al panel de administración de la base de datos.

    Entonces, tendremos un servicio web que funciona como una interfaz para el usuario.
    Este servicio está construido en Python y Flash, y utiliza Bootstrap, HTML y CSS para el frontend.

    La aplicación en sí es un generador de datos falsos con características específicas que se muestran en una tabla de Bootstrap utilizando un data table.

    Para que los datos lleguen a su destino, primero se consultan en el servicio de API.
    El servicio API consulta el servicio Faker, que es responsable de buscar datos falsos en la base de datos y de generar nuevos datos para insertarlos en la misma.

Al iniciar la aplicación por primera vez, se ofrecerá la opción de crear datos falsos en el servicio web, mediante un botón. Al hacer clic en esta opción, se enviará una solicitud a la API, que a su vez solicitará los datos falsos a Facker.
Facker creará los datos y los guardará en una tabla de Postgres en la base de datos.

Cuando se ingresa a la página principal del servicio web, se realiza una solicitud para mostrar los datos. Esta solicitud es enviada a través de la API, que a su vez solicita la información a Facker. Facker busca en la base de datos Postgres todos los registros guardados y los retorna en formato JSON a través de la API. La API envía la respuesta en formato JSON al servicio web, que finalmente grafíca los datos en una tabla de Bootstrap en el front-end.

## Como empezar

Una forma de empezar sería crear la estructura de carpetas para cada uno de los servicios que necesitamos, como el servicio de API, el servicio de Facker, la carpeta para la base de datos de Postgres y el servicio de Web. 
De esta manera, podríamos tener una organización más clara y separada para cada uno de los servicios que vamos a desarrollar. En Visual Studio Code, podríamos crear estas carpetas y empezar a trabajar en cada uno de los servicios por separado.

1. Para empezar con el servicio de Faker, lo primero que debemos hacer es, en su directorio “faker” crear un archivo llamado "facker-service.py".

2. Después, debemos crear un entorno virtual para nuestro proyecto, lo cual podemos hacer con el comando **python3 -m venv venv** en la terminal. Una vez creado, podemos activar el entorno virtual con el comando **source venv/bin/activate** en Ubuntu y el comando **. venv\scripts\activate** en windows. Una vez que hemos activado nuestro entorno virtual:

3. necesitamos instalar Flask, el framework (espacio de trabajo) de Python, que utilizaremos para desarrollar nuestra aplicación. Podemos hacer esto ejecutando el comando **pip install flask**. Si verificamos las librerías instaladas en nuestro entorno virtual con el comando **pip freeze**, deberíamos ver que Flask está entre ellas.

4. Para generar los datos falsos que utilizaremos en nuestro servicio, utilizaremos la librería Faker de Python. Esta librería cuenta con una amplia variedad de datos falsos y métodos para generar diferentes tipos de datos. Para instalarla, basta con ejecutar el comando **pip install faker**.

    hablar sobre HACER PIP FREEZE > requirements.TXT

Una vez que hemos instalado ambas librerías, podemos comenzar a importarlas en nuestro código para empezar a trabajar con ellas

## Archivo faker-service.py

Abrimos el archivo: faker-service.py.

* Vamos a importar las librerías necesarias en nuestro archivo faker-service.py.
Para utilizar Flask, importaremos la clase Flask del módulo flask.
Para generar datos aleatorios, importaremos la clase Faker del módulo faker. Para ello, podemos usar las siguientes líneas de código:

    'from flask import Flask
    from faker import Faker'

Con esto, tendremos las herramientas necesarias para desarrollar nuestro servicio de facker.

* Lo siguiente será definir una instancia de Flask:
'''
    app = Flask(__name__)
'''

* Luego, crearemos una ruta para nuestro servicio de facker con el decorador “@app.route('/facker').”
* Dentro de esta función, crearemos una instancia de Faker:, añadiendo esta linea abajo:

    faker = Faker()

    (Esto nos permitirá generar datos falsos en nuestra API.)

* Ahora, define la ruta con el decorador "@app.route('/facker')" y la función "get_fake_data":

    @app.route('/faker_data')
    def get_fake_data():
        try:
            return "Hola mundo, hola desde get_fake_data"
        except:
            return "Error en el endpoint de get_fake_data"

* Agrega el siguiente código al final de tu archivo Python:

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=3000, debug=True)

    Esto iniciará el servidor web de Flask con el host 0.0.0.0 para que pueda ser accedido desde cualquier dirección IP en localhost y el puerto 3000. El parámetro debug=True activará el modo de depuración, lo que significa que Flask mostrará los errores en la página web en caso de que los haya. Recuerda que no es recomendable activar el modo de depuración en un entorno de producción debido a posibles problemas de seguridad.

## Repaso

Con estos pasos, tendrás un endpoint en Flask que responde en la URL "/faker_data" y devuelve un mensaje al front-end.

Si hay algún error, se capturará y se mostrará el mensaje "Error en el endpoint de get_fake_data".

_codigo completo, confirma tu codigo con este:_

    from flask import Flask
    from faker import Faker

    app = Flask(__name__)
    faker = Faker()

    @app.route('/faker_data')
    def get_fake_data():
        try:
            return "Hola mundo, hola desde get_fake_data"
        except:
            return "Error en el endpoint de get_fake_data"

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=3000, debug=True)

Finalmente, si queremos **probar nuestro servicio**, podemos ejecutar el siguiente comando en la terminal:
**python faker-service.py**

y podrás acceder desde el navegador desde la web:
    <http://localhost:3000/facker_data>

Por defecto se ejecutará nuestro servicio en el puerto 5000.  es decir si dejamos  nuestra linea asi: “app.run()” con los paréntesis vacíos. Podríamos  acceder a él servicio en la dirección:<http://localhost:5000/facker_data>



# Parte 2

- creamos rama develop
- intalamos reque desde requirements.txt
