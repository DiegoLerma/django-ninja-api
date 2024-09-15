from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from usuarios.api import router as usuarios_router  # Importar las rutas de la API
from carga import views as carga_views  # Importar las vistas de carga

api = NinjaAPI()
api.add_router("/usuarios/", usuarios_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),  # Ruta para la API
    path('cargar/', carga_views.cargar_csv, name="cargar_csv"),  # Ruta para la carga de usuarios
    path('', carga_views.home, name='home'),  # Página principal
]
