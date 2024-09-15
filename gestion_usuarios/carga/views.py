import csv
from django.shortcuts import render
from django.contrib import messages
from .forms import CargaMasivaForm
from usuarios.models import Usuario
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Bienvenido a la página de gestión de usuarios de Diego Lerma. Reto 1 completado</h1>")


def cargar_csv(request):
    if request.method == "POST":
        form = CargaMasivaForm(request.POST, request.FILES)
        if form.is_valid():
            archivo_csv = request.FILES["archivo_csv"]
            decoded_file = archivo_csv.read().decode("utf-8").splitlines()
            reader = csv.DictReader(decoded_file)
            for row in reader:
                Usuario.objects.create(
                    nombre=row["nombre"],
                    apellido_paterno=row["apellido_paterno"],
                    apellido_materno=row["apellido_materno"],
                    edad=int(row["edad"]),
                    nombre_cuenta=row["nombre_cuenta"],
                    contrasena=row["contrasena"],
                )
            messages.success(request, "Usuarios cargados exitosamente.")
    else:
        form = CargaMasivaForm()

    return render(request, "carga/cargar_csv.html", {"form": form})
