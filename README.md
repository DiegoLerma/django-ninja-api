# Django Ninja API - Reto 1

![Logo Lite Thinking](https://lms.litethinking.com/assets/LMSLOGO-b18547ba.svg)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.x-darkgreen.svg)](https://www.djangoproject.com/)
[![Django-Ninja](https://img.shields.io/badge/Django--Ninja-blueviolet.svg)](https://django-ninja.rest-framework.com/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Este repositorio contiene el proyecto para el **Reto 1: Microservicios con Django y API REST usando Django-Ninja** del **Master en Desarrollo de Microservicios con Python 🐍** en [LiteThinking](https://www.litethinking.com/es/home). La aplicación permite la gestión de usuarios a través de un CRUD y carga masiva mediante un archivo CSV.

## 📄 **Descripción**

El proyecto está dividido en dos principales funcionalidades:

1. **API REST** para gestionar las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) de usuarios.
2. **Interfaz web** para cargar usuarios de manera masiva desde un archivo CSV.

### 🛠 **Estructura del Proyecto**

- **`usuarios/`**: CRUD de usuarios y API REST utilizando Django-Ninja.
- **`carga/`**: Interfaz web para la carga masiva de usuarios mediante CSV.

## 🚀 **Tecnologías utilizadas**

- **Django**: Framework web de alto nivel para aplicaciones escalables.
- **Django-Ninja**: Framework ligero y rápido para APIs RESTful.

---

## ⚙️ **Instalación**

### **Prerrequisitos**

- [Python 3.8+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)
- Uso de un entorno virtual es recomendado.

### **Pasos de instalación**

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/DiegoLerma/django-ninja-api.git
   cd django-ninja-api
   ```

2. **Crear y activar un entorno virtual (opcional):**

   - **Linux/MacOS**:

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

   - **Windows**:

     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Instalar dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Realizar migraciones:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Iniciar el servidor de desarrollo:**

   ```bash
   python manage.py runserver
   ```

6. **Acceder a la aplicación:**

   - **API CRUD de usuarios**: `http://127.0.0.1:8000/api/`
   - **Carga masiva de usuarios**: `http://127.0.0.1:8000/cargar/`

---

## 🗂 **Ejemplo de archivo CSV**

El archivo CSV debe seguir este formato para la carga masiva:

```csv
nombre,apellido_paterno,apellido_materno,edad,nombre_cuenta,contrasena
Juan,Pérez,González,30,juanp,secret123
María,López,Ramírez,25,mlopez,pass456
```

---

## 📚 **Descripción de Django-Ninja**

**Django-Ninja** es un framework moderno para construir APIs en Django, basado en anotaciones de tipo de Python. Sus principales características incluyen:

- **Tipado automático**: Genera esquemas de validación y documentación API automáticamente.
- **Alto rendimiento**: Usa Starlette como backend para solicitudes asíncronas.
- **Documentación automática**: Swagger se genera automáticamente.

## 💡 **Mejores prácticas aplicadas**

1. **Estructuración clara del proyecto**: Separación modular del código en dos aplicaciones (`usuarios` y `carga`).
2. **Uso de Django-Ninja**: Simplicidad y eficiencia para construir APIs RESTful.
3. **Validación automática de datos**: Uso de anotaciones de tipo en Python para validar datos entrantes.
4. **Carga masiva de usuarios**: Implementación eficiente de manejo de grandes volúmenes de datos.
5. **Seguridad**: Manejo seguro de contraseñas con los mecanismos estándar de Django.

---

## 🛡️ **Contribuciones**

¡Todas las contribuciones son bienvenidas! Sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama para tus cambios:

   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```

3. Realiza los cambios y haz commit:

   ```bash
   git commit -m "Añadir nueva funcionalidad"
   ```

4. Sube tus cambios:

   ```bash
   git push origin feature/nueva-funcionalidad
   ```

5. Abre un pull request en el repositorio original.

---

## 🌐 **Contacto y Soporte**

Cualquier duda o sugerencia, no dudes en abrir un issue en el [repositorio](https://github.com/DiegoLerma/django-ninja-api).
