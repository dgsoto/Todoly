# Todoly API Automation

<img src="https://todo.ly/images/presentation/fixlarge/intro.png">

Este proyecto es un framework de automatización de pruebas para la API de Todoly, utilizando Python, Behave, y Allure.


> Este proyecto está diseñado para automatizar pruebas en la API de Todoly, una aplicación de gestión de tareas. Todoly proporciona funcionalidades para organizar y realizar un seguimiento de tareas y proyectos de manera efectiva.

- Link de todoly: https://todo.ly/
- Link de la API de todoly: https://todo.ly/ApiWiki/

## Descripción de Todoly

Todoly es una plataforma simple y eficiente para la gestión de tareas y proyectos. Ofrece características que permiten a los usuarios crear listas de tareas, asignar tareas a proyectos, establecer fechas de vencimiento y mucho más. La interfaz intuitiva y la flexibilidad hacen que Todoly sea una elección popular para aquellos que buscan una solución de gestión de tareas sencilla pero potente.

## Automatización de la API

Este proyecto tiene como objetivo automatizar pruebas en la API de Todoly para garantizar su correcto funcionamiento y mantener la integridad de las funcionalidades ofrecidas. Algunos de los aspectos que se automatizarán incluyen:

- **Pruebas CRUD (Create, Read, Update, Delete):** Verificar la capacidad de crear, leer, actualizar y eliminar elementos a través de la API.

- **Pruebas de Escenarios Clave:** Automatizar escenarios clave, como la creación de tareas, la asignación a proyectos y la verificación de la correcta actualización de estados.

- **Pruebas de Comparación de Datos:** Utilizar herramientas como `compare` y `jsondiff` para comparar y verificar las respuestas de la API con los resultados esperados.

## Objetivos de la Automatización

- **Garantizar la Estabilidad:** Asegurarse de que la API de Todoly sea estable y consistente en todas las operaciones.

- **Acelerar el Ciclo de Desarrollo:** La automatización de pruebas permite una rápida retroalimentación durante el desarrollo, acelerando el proceso de entrega.

- **Mejorar la Calidad del Software:** Identificar y corregir rápidamente cualquier problema en la API para mejorar la calidad del software entregado.




## Estructura del Proyecto

El proyecto sigue una estructura organizada para facilitar el mantenimiento y la escalabilidad. Aquí hay una descripción de los directorios principales:

- **features:** Contiene los archivos relacionados con los escenarios de Behave.
  - `api.feature`: Define los escenarios BDD para las pruebas de la API.
  - `steps`: Contiene los archivos de pasos BDD (`api_steps.py`) para la implementación de los pasos definidos en `api.feature`.
  - `environment.py`: Configuración del entorno de Behave.

- **configuration:** Contiene la configuración del proyecto.
  - `config.yml`: Archivo YAML para almacenar la configuración del proyecto.

- **tests:** Contiene pruebas unitarias adicionales que no están basadas en BDD.
  - `test_api.py`: Ejemplos de pruebas unitarias para las funciones de la API.
  - `test_compare.py`: Pruebas unitarias para las funciones de comparación.

- **utils:** Contiene módulos/utilidades compartidos.
  - `api_utils.py`: Funciones de utilidad para realizar solicitudes a la API.
  - `compare_utils.py`: Funciones de utilidad para realizar comparaciones entre respuestas de la API.

- **requirements.txt:** Archivo que lista todas las dependencias del proyecto.

- **README.md:** Documentación del proyecto.

> La estructura del proyecto está organizada para facilitar el mantenimiento y la escalabilidad:

```python
├── features
│ ├── api.feature
│ ├── steps
│ │ └── api_steps.py
│ └── environment.py
├── configuration
│ └── config.yml
├── tests
│ ├── init.py
│ ├── test_api.py
│ └── test_compare.py
├── utils
│ ├── init.py
│ ├── compare_utils.py
│ └── api_utils.py
├── requirements.txt
└── README.md
```

## Requisitos
Primero create un virtual environment con python para tener un ambiente controlado y no mesclar proyectos.
```bash
python -m venv my-env-api-todoly
```
Ahora puedes activar tu environment con este comando
```bash
source my-env-api-todoly/Script/active
```

Ahora si ya puedes instalar los requerimientos dentro tu ambiente y asegúrate de tener Python instalado en tu máquina. Puedes instalar las dependencias del proyecto ejecutando:

```bash
pip install -r requirements.txt
```

## Ejecutar Pruebas

### Ejecutar Pruebas con Behave

Si deseas ejecutar comandos Behave sin Allure, simplemente puedes omitir las opciones relacionadas con Allure. Aquí tienes ejemplos de comandos Behave para ejecutar pruebas CRUD, pruebas de humo (smoke) y ambas, sin usar Allure

#### Ejecutar todas las pruebas
```bash
behave
```

#### Ejecutar las pruebas CRUD
```bash
behave -k @crud
```

#### Ejecutar las pruebas Smoke
```bash
behave -k @smoke
```

#### Ejecutar ambas pruebas CRUD y SMOKE
```bash
behave -k "@crud or @smoke"
```

> La opción -f en Behave se utiliza para especificar el formato de salida de los resultados de las pruebas. Si deseas utilizar un formato específico, puedes agregar -f seguido del formato deseado. Aquí hay ejemplos de comandos Behave con la opción -f para ejecutar pruebas CRUD, pruebas de humo (smoke) y ambas:

#### Ejecutar Pruebas CRUD con Formato de Documentación
```bash
behave -k @crud -f plain
```

#### Ejecutar pruebas de Smoke con formato JUnit
```bash
behave -k @smoke -f junit
```

#### Ejecutar ambas CRUD y Smoke con formato JSON
```bash
behave -k "@crud or @smoke" -f json
```

>**Nota:**
Puedes elegir entre varios formatos como json, plain, pretty, progress, json.pretty, junit, entre otros. Ajusta el formato según tus preferencias o requisitos de integración con herramientas externas. Si no especificas la opción -f, Behave utilizará el formato predeterminado, que es pretty.

### Ejecutar Todas las Pruebas de behave con allure
```bash
behave -f allure_behave.formatter:AllureFormatter -o allure-results
allure serve allure-results
```

### Ejecutar Pruebas con Etiqueta @crud
```bash
behave -f allure_behave.formatter:AllureFormatter -o allure-results -k @crud
```

### Ejecutar Pruebas con Etiqueta @smoke
```bash
behave -f allure_behave.formatter:AllureFormatter -o allure-results -k @smoke
```

## Informes de Allure
Después de ejecutar las pruebas, puedes visualizar los informes de Allure con el siguiente comando:

```bash
allure serve allure-results
```

## Contribuciones
Si encuentras problemas o deseas contribuir al proyecto, por favor abre un issue o envía una pull request.

## Licencia
Este proyecto está bajo la licencia MIT.
```bash
Recuerda personalizar la información, como las instrucciones de ejecución y los comandos, según las características específicas de tu proyecto. También, asegúrate de incluir información importante sobre la configuración, requisitos y cualquier otra cosa que los usuarios o colaboradores puedan necesitar para entender y contribuir al proyecto.
```