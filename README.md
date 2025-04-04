# 📝 TaskManager - Gestor de Tareas en Django  

TaskManager es una aplicación web para gestionar tareas, creada con Django. Permite a los usuarios registrarse, iniciar sesión, agregar, editar y eliminar tareas.  

## 🚀 Características  
- Registro e inicio de sesión de usuarios.  
- Creación, edición y eliminación de tareas.  
- Interfaz mejorada con Bootstrap.  
- Panel de administración de Django.  

## 📦 Instalación y Configuración  

### 1️⃣ Clonar el repositorio  
```bash
git clone https://github.com/tu_usuario/taskmanager.git
cd taskmanager


2️⃣ Crear un entorno virtual
🔹 En Windows (CMD/PowerShell)
python -m venv venv
venv\Scripts\activate


🔹 En macOS/Linux (Terminal) python3 -m venv venv
source venv/bin/actívate


3️⃣ Instalar dependencias
bash
pip install -r requirements.txt


4️⃣ Configurar la base de datos
python manage.py migrate

5️⃣ Crear un superusuario (opcional)
Si deseas acceder al panel de administración:
python manage.py createsuperuser

6️⃣ Ejecutar el servidor
python manage.py runserver
Luego, abre el navegador y ve a:
🔗 http://127.0.0.1:8000/

⚙️ Variables de Entorno
Para configurar la base de datos y otros ajustes, puedes crear un archivo .env y agregar:
SECRET_KEY='tu_clave_secreta'
DEBUG=True





📄 Estructura del Proyecto

taskmanager/
│── taskmanager/         # Configuración principal de Django  
│── tasks/               # Aplicación principal  
│── templates/           # Archivos HTML  
│── static/              # Archivos CSS y JS  
│── db.sqlite3           # Base de datos SQLite  
│── manage.py            # Comando principal de Django  
│── requirements.txt     # Dependencias del proyecto  
│── README.md            # Documentación del proyecto  


📌 Tecnologías Usadas
•	Django
•	SQLite
•	Bootstrap
•	HTML, CSS


📜 Licencia
Este proyecto está bajo la licencia MIT. ¡Siéntete libre de mejorarlo y contribuir! 🚀

