from flask import Blueprint
from .controller import check_status, get_info

# Blueprint que agrupa los endpoints de la API.
api_routes = Blueprint('api_routes', __name__)


@api_routes.route('/check', methods=['GET'])
def check():
    """GET /check -> devuelve un estado OK."""
    return check_status()


@api_routes.route('/info', methods=['GET'])
def info():
    """GET /info -> devuelve metadatos de la instancia en JSON."""
    return get_info()
