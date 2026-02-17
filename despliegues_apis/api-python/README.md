# API Python (Flask)

API sencilla para el laboratorio de despliegue. Expone endpoints de salud y metadatos de la instancia.

## Requisitos

- Python 3.x
- Dependencias en requirements.txt

## Instalacion

```bash
pip install -r requirements.txt
```

## Ejecucion

```bash
python run.py
```

Por defecto escucha en el puerto 3000. Puedes cambiarlo con la variable de entorno `PORT`.

## Endpoints

- `GET /check` -> Respuesta de salud: `OK`.
- `GET /info` -> JSON con metadatos de la instancia (instancia, curso, grupo).
