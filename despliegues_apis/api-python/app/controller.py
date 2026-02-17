from flask import jsonify


def check_status():
    """Endpoint de salud para validar que la API esta activa."""
    return "OK", 200


def get_info():
    """Devuelve metadatos de la instancia usados en el laboratorio."""
    return jsonify({
        "Instancia": "Instancia-2 - API Python",
        "Curso": "Seminario de Sistemas 1 A",
        "Grupo": "Grupo #8"
    })
