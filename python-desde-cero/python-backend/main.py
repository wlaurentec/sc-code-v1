from typing import Optional
import uuid
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Define la configuración de la aplicación
app = FastAPI()

# Define los modelos de datos
class Curso(BaseModel):
    id: Optional[str] = None
    nombre: str
    descripcion: Optional[str] = None 
    nivel: str
    duracion: int

# Simularemos una base de datos

cursos_db = []

# CRUD: Read
@app.get("/cursos", response_model=list[Curso])
def obtener_cursos():
    return cursos_db

# CRUD: Create
@app.post("/cursos", response_model=Curso)
def crear_curso(curso: Curso):
    curso.id = str(uuid.uuid4()) # Generar un ID único
    cursos_db.append(curso)
    return curso

# CRUD: Obtener un curso por su ID

@app.get("/cursos/{curso_id}", response_model=Curso)
def obtener_curso(curso_id: str):
    curso = next((curso for curso in cursos_db if curso.id == curso_id), None)
    if curso is None:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    return curso

# CRUD: Actualizar un curso por su ID
@app.put("/cursos/{curso_id}", response_model=Curso)
def actualizar_curso(curso_id: str, curso: Curso):  
    curso_actualizado = next((curso for curso in cursos_db if curso.id == curso_id), None)
    if curso_actualizado is None:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    curso_actualizado.nombre = curso.nombre
    curso_actualizado.descripcion = curso.descripcion
    curso_actualizado.nivel = curso.nivel
    curso_actualizado.duracion = curso.duracion
    return curso_actualizado

# CRUD: Eliminar un curso por su ID
@app.delete("/cursos/{curso_id}", response_model=Curso)
def eliminar_curso(curso_id: str):  
    curso_eliminado = next((curso for curso in cursos_db if curso.id == curso_id), None)
    if curso_eliminado is None:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    cursos_db.remove(curso_eliminado)
    return curso_eliminado