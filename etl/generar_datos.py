# PROYECTO AGENDA MEDICCA
# ESTE ARCHIVO CREADA DATOS FICTICIOS PARA EL PRYECTO 

import pandas as pd
import numpy as np
import random
from pathlib import Path

# SE FIJARA PARA QUE SIEMPRE GENERE LOS MISMO DATOS CADA VEZ QUE SE EJECUTE EL PROGRAMA
random.seed(42)
np.random.seed(42)

BASE_DIR = Path(__file__).resolve().parent
RUTA_RAW = BASE_DIR / "data" / "raw"
RUTA_RAW.mkdir(parents=True, exist_ok=True)

# 1 CREACION DE ESPECIALIDADES
especialidades = pd.DataFrame([
    {"especialidad_id": 1, "nombre": "Medicina General"},
    {"especialidad_id": 2, "nombre": "Pediatria"},
    {"especialidad_id": 3, "nombre": "Cardiologia"},
    {"especialidad_id": 4, "nombre": "Ginecologia"},
    {"especialidad_id": 5, "nombre": "Ortopedia"},
    {"especialidad_id": 6, "nombre": "Dermatologia"}
])

# 2 CREACION DE MEDICOS
nombres_medicos = [
     "Carlos", "Laura", "Andres", "Mariana", "Felipe",
    "Camila", "Daniel", "Valentina", "Santiago", "Natalia"
]
apellidos = [
    "Gomez", "Rodriguez", "Martinez", "Lopez", "Garcia",
    "Ramirez", "Torres", "Hernandez", "Castro", "Morales"
]

medicos = []

for i in range(1, 16):
    # CADA MEDICO QUEDA ASOCIADO A UNA ESPECIALIDAD
    medicos.append({
        "medico_id": i,
        "nombre": f"Dr. {random.choice(nombres_medicos)} " f"{random.choice(apellidos)}",
        "especialidad_id": random.randint(1,6)
    })

medicos = pd.DataFrame(medicos)

# 3 CREACION DE PACIENTES
nombres_pacientes = [
    "Juan", "Maria", "Pedro", "Ana", "Luis",
    "Sofia", "Jorge", "Paula", "Miguel", "Diana",
    "Andres", "Laura", "Camilo", "Valentina"
]
pacientes = []

for i in range(1, 501):

    pacientes.append({
        "paciente_id": i,
        "nombre": f"{random.choice(nombres_pacientes)} "
                  f"{random.choice(apellidos)}",
        "edad": random.randint(1, 90),
        "genero": random.choice(["F", "M"])
    })

pacientes = pd.DataFrame(pacientes)


# ==============================================
# 4. CREAR CITAS MeDICAS
# ==============================================

estados = ["Atendida", "Cancelada", "No asistio"]

# Probabilidades de cada estado:
# 75% atendidas, 15% canceladas y 10% no asistio.
probabilidades = [0.75, 0.15, 0.10]

citas = []

for i in range(1, 1001):

    # Seleccionamos un medico y un paciente existentes.
    medico_id = random.randint(1, 15)
    paciente_id = random.randint(1, 500)

    # Generamos una fecha aleatoria durante el a?o 2026.
    fecha = pd.Timestamp("2026-01-01") + pd.Timedelta(
        days=random.randint(0, 364)
    )

    # Generamos una hora entre las 7:00 y las 17:00.
    hora = f"{random.randint(7, 17):02d}:{random.choice([0, 30]):02d}"

    # Elegimos el estado segun las probabilidades definidas.
    estado = random.choices(
        estados,
        weights=probabilidades,
        k=1
    )[0]

    # Las citas no atendidas no tendran tiempo de espera.
    tiempo_espera = (
        random.randint(5, 120)
        if estado == "Atendida"
        else 0
    )

    citas.append({
        "cita_id": i,
        "paciente_id": paciente_id,
        "medico_id": medico_id,
        "fecha": fecha,
        "hora": hora,
        "estado": estado,
        "tiempo_espera_minutos": tiempo_espera
    })

citas = pd.DataFrame(citas)


# ==============================================
# 5. GUARDAR LOS ARCHIVOS CSV
# ==============================================

especialidades.to_csv(
    RUTA_RAW / "especialidades.csv",
    index=False,
    encoding="utf-8-sig"
)

medicos.to_csv(
    RUTA_RAW / "medicos.csv",
    index=False,
    encoding="utf-8-sig"
)

pacientes.to_csv(
    RUTA_RAW / "pacientes.csv",
    index=False,
    encoding="utf-8-sig"
)

citas.to_csv(
    RUTA_RAW / "citas.csv",
    index=False,
    encoding="utf-8-sig"
)

# ==============================================
# 6. MOSTRAR RESULTADOS
# ==============================================

print("\nGENERACION DE DATOS FINALIZADA")
print("--------------------------------")

print(f"Especialidades: {len(especialidades)}")
print(f"Medicos: {len(medicos)}")
print(f"Pacientes: {len(pacientes)}")
print(f"Citas: {len(citas)}")

print("\nArchivos guardados en:", RUTA_RAW)