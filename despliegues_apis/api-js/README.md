# API JS (Express)

API sencilla para el laboratorio de despliegue. Expone endpoints de salud y metadatos de la instancia.

## Requisitos

- Node.js 18+ (recomendado)
- Dependencias en package.json

## Instalacion

```bash
npm install
```

## Ejecucion

```bash
npm start
```

Por defecto escucha en el puerto 3000. Puedes cambiarlo con la variable de entorno `PORT`.

## Endpoints

- `GET /check` -> Respuesta de salud: `OK`.
- `GET /info` -> JSON con metadatos de la instancia (instancia, curso, grupo).
