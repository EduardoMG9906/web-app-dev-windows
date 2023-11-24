import functools
from flask import Blueprint, request, jsonify
from flask_cors import CORS
from model.medicamentos import (
    get_medicamentos,
    get_medicamento,
    create_medicamento,
    update_medicamento,
    delete_medicamento,
)

bp = Blueprint('medicamentos', __name__, url_prefix='/medicamentos')
CORS(bp)

@bp.route('/', methods=['GET'])
def list():
    retorno = get_medicamentos()
    return jsonify(retorno)

@bp.route('/<int:medicamento_id>', methods=['GET'])
def get(medicamento_id):
    return jsonify(get_medicamento(medicamento_id))

@bp.route('/', methods=['POST'])
def create():
    data = request.get_json()
    dosis = data['dosis']
    via = data['via']
    nombre = data['nombre']
    frecuencia_dia = data['frecuencia_dia']
    duracion_dias = data['duracion_dias']
    observaciones = data['observaciones']
    return jsonify(create_medicamento(dosis, via, nombre, frecuencia_dia, duracion_dias, observaciones))

@bp.route('/<int:medicamento_id>', methods=['PUT'])
def update(medicamento_id):
    data = request.get_json()
    dosis = data['dosis']
    via = data['via']
    nombre = data['nombre']
    frecuencia_dia = data['frecuencia_dia']
    duracion_dias = data['duracion_dias']
    observaciones = data['observaciones']
    return jsonify(update_medicamento(dosis, via, nombre, frecuencia_dia, duracion_dias, observaciones, medicamento_id))

@bp.route('/<int:medicamento_id>', methods=['DELETE'])
def delete(medicamento_id):
    return jsonify(delete_medicamento(medicamento_id))
