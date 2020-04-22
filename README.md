# Image to text.
## Extráe el texto de una imagen usando _tesseract_.

### Descripción.
Proyecto básico hecho en _Python(Django)_ y _Vanilla Javascript_ que muestra el resultado de la utilización de la  librería _tesseract_

### Utilización.
El uso es simple, se sube una imagen, hecho esto se pulsa el botón *convertir* que realizará la extracción del texto (esto puede tardar un tiempo, en función de la cantidad de texto a extraer).

Finalizada la extracción se muestra el texto en pantalla y se tiene la opción de exportar el texto usando el botón *exportar*

### Dependencias del sistema.
Para hacer la instalación se requiere tener instalado *tesseract*, si no lo tiene instalado puede descargarlo [aquí](https://github.com/tesseract-ocr/tesseract/wiki).

Adicionalmente se pueden agregar _traineddata_ en varios idiomas desde [aquí](https://github.com/tesseract-ocr/tesseract/blob/master/doc/tesseract.1.asc#languages)

Para este proyecto será necesario tener instalados los idiomas eng y spa.
Puede comprobar los idiomas instalados en:
- Windows: C:\Program Files\Tesseract-OCR\tessdata\
- Linux, Mac: /usr/share/tesseract-ocr/4.00/tessdata/ *(la carpeta 4.00 es la versión, si tiene una versión diferente tiene que entrar en la carpeta correspondiente a su versión)*

### Instalación.
Para realizar la instalación hay que seguir los siguientes pasos.

1. Descargar el código fuente
2. Crear un entorno virtual con virtualenv o similares (este paso es opcional, pero muy recomendado) `virtualenv _carpeta_ -p python3` (_carpeta_ es el nombre que se le quiere dar a la carpeta donde se guardaran los datos del entorno virtual. En el caso de windows hay que agregar la ruta entera hacia el lanzador de python).
3. Si se ha creado el entorno virrual, activadlo (donde _carpeta_ es el nombre que se le ha dado al usar virtualenv). 
    
    Windows: `_carpeta_\scripts\activate.bat`
    Linux, Mac: `source _carpeta_/bin/activate`
4. instalar los requerimientos `pip install -r requirements.txt`, tambien puede instalar los requerimientos de forma manual usando pip. Necesitará instalar *django*, *pillow* y *pytesseract*
5. Editar el archivo image_to_text/settings.py. Ir al final del archivo. cambiar el contenido de la variable _MAIN_URL_ por la dirección web donde se ejecutará la aplicación.
6. Aplicamos las migraciones. `python manage.py migrate`
7. Recolectamos los archivos estáticos. `python manage.py collectstatics`
8. Para usarlo con el servidor de pruebas de *django* usad. `python manage.py runserver` y acceder con el navegador a [localhost:8000](http://localhost:8000)

### Extras.
Las imágenes se subirán a la carpeta *tmp/* dentro de la carpeta media. Si no se hacen cambios dicha carpeta se ubicará en la carpeta padre de donde tengamos la aplicación. *../static/media/tmp/*

Una vez subida la imagen se crea un registro en la base de datos con la imagen y un UUID.

La base de datos usada por defecto es sqlite3, si se desea cambiar por otra solo hay que seguir la configuración recomendada para cada tipo de base de datos. [LEER](https://docs.djangoproject.com/en/3.0/ref/databases/).

Se ha creado un endpoint (tipo GET) para eliminar datos tanto de la base de datos como de la carpeta temp (también se puede utilizar como una tarea automatizada).

Para usarla solo hay que acceder a ella ya sea desde el navegador, desde un programa tipo postman o curl indicando la dirección del servidor y el endpoint */clear/*.

Ejemplo, si está trabajando con el servidor de *django* sería. [http://localhost:8000/clear/](http://localhost:8000/clear/)

Por defecto eliminará todos los datos desde 1 hora anterior al momento de ejecutar el endpoint. O, lo que es lo mismo, solo dejará los datos de la última hora.

Se puede cambiar este comportamiento enviando por parámetro la cantidad de horas que tiene que dejar.

[http://localhost:8000/clear/?hours=10](http://localhost:8000/clear/?hours=10) 

Esto hará que borre todos los datos excepto los de las últimas 10 horas. Si se quiere eliminar todo solo hay que enviar como parámetro *hours=0*.

El parámetro solo admite números enteros positivos, cualquier otra cosa (negativos, decimales, texto) hará su función por defecto que es *hours=1*

### Ejemplo.

![Ejemplo de funcionamiento](./Image_to_tex.gif)

### Por hacer.

- Utilizar las diversas opciones de reconocimiento de texto.

- Utilizar y mostrar el reconocimiento de cuadros que componen el texto de la imágen.

- Seleccionar idiomas.

- Crear API para utilizar desde el exterior o integrar otros Front-ends.


### Créditos.

Autor: != Alfonso merino

Email: alfonsoma75@gmail.com