from flask import Flask


def create_app():
    """Crea y configura la aplicacion Flask."""
    app = Flask(__name__)

    # Registra las rutas de la API en la raiz.
    from .routes import api_routes
    app.register_blueprint(api_routes)

    return app
