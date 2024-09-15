from typing import List
from ninja import Router
from ninja import Schema
from django.shortcuts import get_object_or_404
from usuarios.models import Usuario

router = Router()


class UsuarioSchema(Schema):
    id: int
    nombre: str
    apellido_paterno: str
    apellido_materno: str
    edad: int
    nombre_cuenta: str


class UsuarioCreateSchema(Schema):
    nombre: str
    apellido_paterno: str
    apellido_materno: str
    edad: int
    nombre_cuenta: str
    contrasena: str


@router.get("/", response=List[UsuarioSchema])
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return usuarios


@router.post("/", response=UsuarioSchema)
def crear_usuario(request, payload: UsuarioCreateSchema):
    usuario = Usuario.objects.create(**payload.dict())
    return usuario


@router.put("/{usuario_id}", response=UsuarioSchema)
def actualizar_usuario(request, usuario_id: int, payload: UsuarioCreateSchema):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    for attr, value in payload.dict().items():
        setattr(usuario, attr, value)
    usuario.save()
    return usuario


@router.delete("/{usuario_id}")
def eliminar_usuario(request, usuario_id: int):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    usuario.delete()
    return {"success": True}
