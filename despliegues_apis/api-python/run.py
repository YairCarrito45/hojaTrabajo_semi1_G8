from app import create_app
import os

# Instancia de Flask creada por el factory.
app = create_app()

if __name__ == '__main__':
    # Usa PORT del entorno cuando esta disponible (por ejemplo, despliegue).
    port = int(os.environ.get("PORT", 3500))
    app.run(host='0.0.0.0', port=port)
