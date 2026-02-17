# Despliegues APIs

Repositorio con dos APIs para el laboratorio de despliegue: una en Node.js (Express) y otra en Python (Flask).

## Estructura

- `api-js/` -> API en Express.
- `api-python/` -> API en Flask.

## Requisitos

- Node.js 18+ (recomendado) para la API JS.
- Python 3.x para la API Python.

## Ejecucion rapida

### API JS (Express)

```bash
cd api-js
npm install
npm start
```

### API Python (Flask)

```bash
cd api-python
pip install -r requirements.txt
python run.py
```

Por defecto ambas APIs escuchan en el puerto 3000. Puedes cambiarlo con la variable de entorno `PORT`.

## Endpoints comunes

- `GET /check` -> Respuesta de salud: `OK`.
- `GET /info` -> JSON con metadatos de la instancia (instancia, curso, grupo).