#################################### Pre-Entrega N°03 ####################################

Autor: Carlos Biénzobas.

                          ### Desarrollo ###

Contexto:
El presente proyecto consiste en una página web de un Centro Dental ficticio en Santiago de Chile. El centro dental se caracteriza por poseer múltiples sucursales en la región metropolitana, múltiples especialidades y dentistas en su equipo de trabajo. Adicionalmente a esto, en caso de que el cliente no encuentre el servicio que busca en la clínica, puede optar a buscar a través de la página web, una opción dentro de la red de especialistas o clínicas externas que tienen convenio con la misma.
Finalmente, esta versión de la entrega tiene como objetivo su uso administrativo interno dentro de la clínica para su evaluación, donde posteriormente como parte del Proyecto Final del presente curso, se espera complementar y ajustar a la versión final de la misma para acceso a todo público.

Ecosistema:
Python-3.9.13
django-4.2
django Admin access==> User = admin / pass: coder2024
Template Bootstrap-Startbootstrap scrolling nav gh pages

Contenido Proyecto:
El proyecto consta de 5 aplicaciones:
A continuación una descripción breve del objetivo de cada una:

- Inicio: Aplicación para el manejo de manera independiente del contenido y aspectos generales de comunicación al cliente a travez de la pagina principal del sitio web. Dado que la entrega actual es para fines internos, actualmente solo hereda la totalidad del contenido default de la pagina base.html.
- Acceso: Aplicación sin uso por el momento. Espacio reservado para entrega Proyecto Final. La expectativa es que para proyecto final incorporar autentificación para usuarios administrativos a formularios.
- Dentistas: Aplicación para la visualización, búsqueda y creación de Dentistas en la base de datos.
- Especialidades: Aplicación para la visualización, búsqueda y creación de Especialidades en la base de datos.
- Sucursales: Aplicación para la visualización, búsqueda y creación de Sucursales en la base de datos.

Racional del código:
Dado el tamaño del presente proyecto y los multiples archivos de programación requeridos asociados para su funcionamiento, es que dentro de las aplicacion DENTISTAS, en sus principales archivos ".py" y ".html" intervenidos se encuentra en # o <---> la lógica detras de cada linea de codigo y su objetivo respectivo. El racional ahi descrito es el mismo fundamento con el que se replica la logica hacia la aplicacion de ESPECIALIDADES y SUCURSALES, cumpliendo los mismos objetivos de formularios, busquedas y visualizacion de tablas.


Casos de Prueba y Funcionalidades: (Basados en Criterios 3era Entrega Clase 21 - Playground Intermedio Parte III , diapositiva 55.)

                        ### Casos de Prueba ###

1. Herencia html:

  1.1 Ingresar a la Carpeta CMDENTAL ==> CMDENTAL ==> templates ==> base.html
  
  1.2 Revisar en archivo base.html y identificar las multiples secciones de bloqueo de contenido en multiples niveles por medio de la sentencia "  {% block XXX %}  {% endblock %} ". Las principales a identificar son:
  {% block title %}  {% endblock %} 
  {% block about %}  {% endblock %}
  {% block content %}  {% endblock %}
  {% block contact %}  {% endblock %}
  Nota: Cada uno de estos bloqueos se apertura a nivel de title y content según necesidad.

  1.3 Ingresar a la Carpeta:
  CMDENTAL ==> dentistas ==> templates ==> dentistas ==> nuestros_dentistas.html y validar utilización de herencias.
  CMDENTAL ==> especialidades ==> templates ==> especialidades ==> especialidades.html y validar utilización de herencias.
  CMDENTAL ==> sucursales ==> templates ==> sucursales ==> sucursales.html y validar utilización de herencias.

  Nota: Estos 3 casos son ejemplos de la utilización efectiva de Herencia, pero esta misma esta aplicada en la totalidad de los templates del proyecto.



2. Por lo menos 3 Clases en Models:

 2.1 Ingresar a la Carpeta: 
  CMDENTAL ==> dentistas ==> models.py y verifica que este creada la clase "Dentista".
  CMDENTAL ==> especialidades ==> models.py y verifica que este creada la clase "Especialidad".
  CMDENTAL ==> sucursales ==> models.py y verifica que este creada la clase "Sucursal".



3. Formularios para insertar datos a las clases de models:

  3.1 Ejecuta "pipenv shell" y "python manage.py runserver" en la terminal sobre la carpeta "CMDENTAL".
  3.2 Ingresa a link con la IP resultante para ingrega a la pagina web principal "http://127.0.0.1:8000/"
  3.3 Hacer clic en la "navigation bar" en la parte superior de la web y hacer clic en el boton "dentistas".
  3.4 En la nueva pagina resultante, dirigete hacia el final de la pagina, especificamente a la sección "Formulario" y hacer clic en el boton "agregar". 
  3.5 En la nueva pagina resultante, completa la información solicitada y hacer clic en botón "Agregar".Espera recibir el mensaje de "registro agregado exitosamente".
  3.6 En esta pagina, dirigirse hacia el "navigation bar" en la parte superior de la pantalla y hacer clic en la opción de "Especialidades" y "Sucursales" repitiendo los pasos 3.3, 3.4 y 3.5  para ambas opciones respectivamente.

  NOTA: PARA QUE EN DENTISTAS Y ESPECIALIDADES SE VEAN EN LA MISMA PAGINA LOS NUEVOS REGISTROS SE DEBE MARCAR LA CASILLA "PLANTA" EN DENTISTAS Y "DISPONIBLE" EN ESPECIALIDADES, SINO NO APARECERAN.



 4. Formulario(s) para búsqueda en Base de Datos:
  4.1 Ejecuta "pipenv shell" y "python manage.py runserver" en la terminal sobre la carpeta "CMDENTAL".
  4.2 Ingresa a link con la IP resultante para ingrega a la pagina web principal "http://127.0.0.1:8000/"
  4.3 Hacer clic en la "navigation bar" en la parte superior de la web y hacer clic en el boton "dentistas".
  4.4 En la nueva pagina resultante, dirigete hacia la mitad de la pagina, especificamente a la sección que contiene el boton "Buscar" y hacer clic sobre el mismo.
  4.5 En la nueva pagina resultante, completa la información en el cuadro de busqueda, en este caso el nombre, y hacer clic en botón "buscar".Espera recibir en la misma pantalla el resutado de la busqueda.
  4.6 Una vez concluida la busqueda, dirigirse hacia el "navigation bar" en la parte superior de la pantalla y hacer clic en la opción de "Especialidades" y "Sucursales" repitiendo los pasos 3.3, 3.4 y para ambas opciones respectivamente.
  
  NOTA: Datos de ejemplos para encontrar por medio del cuadro de busqueda en cada clase seria: dentistas: Carolina; especialidades: Endodoncia y sucursales: Las Condes





                            ### Funcionalidades ###

1. Base de datos con tablas independientes para Dentistas, Especialidades y Sucursales.
  archivo(s) relacionado(s) y ubicación: 
  CMDENTAL ==> CMDENTAL ==> db.sqlite.3

2. Visualización en front web de registros en base de datos para Dentistas, Especialidades y Sucursales.
  archivo(s) relacionado(s) y ubicación: 
  
  Tablas Dentistas:
  FRONT: CMDENTAL ==> CMDENTAL ==> dentistas ==> nuestros_dentistas.html
  VISTA: CMDENTAL ==> CMDENTAL ==> dentistas ==> views.py ==> nuestros_dentistas
  MODELO: CMDENTAL ==> CMDENTAL ==> dentistas ==> models.py ==> Dentista

  Tablas Especialidades:
  FRONT: CMDENTAL ==> CMDENTAL ==> especialidades ==> especialidades.html
  VISTA: CMDENTAL ==> CMDENTAL ==> especialidades ==> view.py ==> especialidades
  MODELO: CMDENTAL ==> CMDENTAL ==> especialidades ==> models.py ==> Especialidad
  
  Tablas Sucursales:
  FRONT: CMDENTAL ==> CMDENTAL ==> sucursales ==> sucursales.html
  VISTA: CMDENTAL ==> CMDENTAL ==> sucursales ==> view.py ==> sucursales
  MODELO: CMDENTAL ==> CMDENTAL ==> sucursales ==> models.py ==> Sucursal

3. Formulación web para creación de nuevos registros en tablas de Dentistas, Especialidades y Sucursales.

  Formulario Dentistas:
  FRONT: CMDENTAL ==> CMDENTAL ==> dentistas ==> agregar_dentista.html
  VISTA: CMDENTAL ==> CMDENTAL ==> dentistas ==> view.py ==> add_dentista
  MODELO: CMDENTAL ==> CMDENTAL ==> dentistas ==> models.py ==> Dentista
  FORM: CMDENTAL ==> CMDENTAL ==> dentistas ==> forms.py ==> NuevoDentista

  Formulario Especialidades:
  FRONT: CMDENTAL ==> CMDENTAL ==> especialidades ==> agregar_especialidades.html
  VISTA: CMDENTAL ==> CMDENTAL ==> especialidades ==> view.py ==> agregar_especialidades
  MODELO: CMDENTAL ==> CMDENTAL ==> especialidades ==> models.py ==> Especialidad
  FORM: CMDENTAL ==> CMDENTAL ==> especialidades ==> forms.py ==> NuevaEspecialidad
  
  Formulario Sucursales:
  FRONT: CMDENTAL ==> CMDENTAL ==> sucursales ==> agregar_sucursales.html
  VISTA: CMDENTAL ==> CMDENTAL ==> sucursales ==> view.py ==> agregar_sucursales
  MODELO: CMDENTAL ==> CMDENTAL ==> sucursales ==> models.py ==> Sucursal
  FORM: CMDENTAL ==> CMDENTAL ==> sucursales ==> forms.py ==> NuevaSucursal

4. Barra de busqueda en tablas de Dentistas, Especialidades y Sucursales.

  Barra busqueda Dentistas:
  FRONT: CMDENTAL ==> CMDENTAL ==> dentistas ==> buscar_dentista.html
  VISTA: CMDENTAL ==> CMDENTAL ==> dentistas ==> view.py ==> search_dentista
  MODELO: CMDENTAL ==> CMDENTAL ==> dentistas ==> models.py ==> Dentista
  FORM: CMDENTAL ==> CMDENTAL ==> dentistas ==> forms.py ==> BuscaDentista

  Barra busqueda Especialidades:
  FRONT: CMDENTAL ==> CMDENTAL ==> especialidades ==> buscar_especialidades.html
  VISTA: CMDENTAL ==> CMDENTAL ==> especialidades ==> view.py ==> agregar_especialidades
  MODELO: CMDENTAL ==> CMDENTAL ==> especialidades ==> models.py ==> Especialidad
  FORM: CMDENTAL ==> CMDENTAL ==> especialidades ==> forms.py ==> BuscaEspecialidad

  Barra busqueda Sucursales:
  FRONT: CMDENTAL ==> CMDENTAL ==> sucursales ==> buscar_sucursales.html
  VISTA: CMDENTAL ==> CMDENTAL ==> sucursales ==> view.py ==> agregar_sucursales
  MODELO: CMDENTAL ==> CMDENTAL ==> sucursales ==> models.py ==> Sucursal
  FORM: CMDENTAL ==> CMDENTAL ==> sucursales ==> forms.py ==> BuscarSucursal

5. Modificación (update and delete) de registros en base de datos por medio de Admin DJANGO.

CMDENTAL ==> CMDENTAL ==> urls.py ==> path('admin/', admin.site.urls)
CMDENTAL ==> templates ==> base.html ==> Navigation ==> button "Acceso Administrativo" href="/admin/"
