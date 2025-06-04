# Trabajo Final Integrador  
## *El Olivo y la Cochinilla*  

### Cátedra: Simulación  
**Docentes:**  
- Ing. Teri Maria Eugenia  
- Ing. Paredi Mario  

**Comisión:** 4K2  

### Integrantes y legajos:
- Dibi, Pablo — *Legajo: 42.171*  
- Jaluf, Rocio — *Legajo: 52.447*  
- Montilla, Tomas — *Legajo: 53.331*  
- Sachetti, Milagros — *Legajo: 53.867*  

---

## Descripción del proyecto

Este repositorio contiene el **backend** de la aplicación desarrollada para el Trabajo Final Integrador de la materia **Simulación**.  
El proyecto está enfocado en la simulación del impacto de tratamientos fitosanitarios sobre una plaga que afecta al cultivo del olivo, conocida como **la cochinilla del olivio** o **parlatoria oleae**.

El backend fue desarrollado utilizando **Python** y el framework **FastAPI**.

---

## Tecnologías utilizadas

- Python 3.11+
- FastAPI
- Docker
- Pydantic

---

## Endpoints de la API

### GET /tratamientos-sanitarios
Obtiene todos los tratamientos fitosanitarios disponibles.

**Respuesta:**  
Lista de objetos con el siguiente esquema:

```
{
  "id": 1,
  "producto": "Nombre del producto",
  "disminucion_grado_ataque": 40,
  "media_inmunidad": 20,
  "desviacion_inmunidad": 5,
  "periodo_carencia": 30,
  "tiempo_entre_aplicaciones": 7
}
```

---

### POST /simular
Realiza una simulación del tratamiento sobre las hectáreas ingresadas, entre la fecha de inicio y floración.

**Body:**
```
{
  "id_tratamiento": 1,
  "hectareas": 10,
  "fecha_inicio": "2025-08-15",
  "fecha_floracion": "2025-10-15"
}
```

**Respuesta:**  
Lista de objetos `DiaSchema`:
```
[
  {
    "fecha": "2025-08-01T00:00:00",
    "grado_ataque": 2.5,
    "arboles_observados": 50,
    "dia_humedo": false,
    "dia_calido": true,
    "aplicacion_tratamiento_fitosanitario": false
  },
  ...
]
```

---

## Ejecución con Docker

### Requisitos previos

- Tener instalado Docker

### Instrucciones

1. Clonar este repositorio:
   ```
   git clone https://github.com/usuario/proyecto-simulacion.git
   cd proyecto-simulacion
   ```

2. Construir la imagen de Docker:
    ```
   docker build -t simulador-olivo .
    ```

3. Ejecutar el contenedor:
    ```
   docker run -d -p 8000:8000 simulador-olivo
    ```

4. Acceder a la documentación interactiva de la API:
   ```
   http://localhost:8000/docs
   ```

---

## Estructura de esquemas principales

### TratamientoFitosanitarioSchema
class TratamientoFitosanitarioSchema(BaseModel):
    id: int
    producto: str
    disminucion_grado_ataque: int
    media_inmunidad: int
    desviacion_inmunidad: int
    periodo_carencia: int
    tiempo_entre_aplicaciones: int

### SimuladorInputSchema
class SimuladorInputSchema(BaseModel):
    id_tratamiento: int
    hectareas: int
    fecha_inicio: date
    fecha_floracion: date