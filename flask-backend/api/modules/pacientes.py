import functools
from flask import Blueprint, request, jsonify
from flask_cors import CORS
from model.paciente import (
    get_pacientes,
    get_paciente,
    create_paciente,
    # get_company_by_name,
    update_paciente,
    delete_paciente,
)

bp = Blueprint('pacientes', __name__, url_prefix='/pacientes')
CORS(bp)

@bp.route('/', methods=['GET'])
def list():
    retorno = get_pacientes()
    return jsonify(retorno)

@bp.route('/<int:paciente_id>', methods=['GET'])
def get(paciente_id):
    return jsonify(get_paciente(paciente_id))


@bp.route('/', methods=['POST'])
def create():
    data = request.get_json()
    tipo_id = data['tipo_id']
    nombre = data['nombre']
    email = data['email']
    grupo_sanguineo = data['grupo_sanguineo']
    genero = data['genero']
    edad = data['edad']
    fecha_nacimiento = data['fecha_nacimiento']
    direccion = data['direccion']
    celular = data['celular']
    eps = data['eps']
    serial_hc = data['serial_hc']

    return jsonify(create_paciente(tipo_id, nombre, email, grupo_sanguineo, genero, edad, fecha_nacimiento, direccion, celular, eps, serial_hc))

@bp.route('/<int:paciente_id>', methods=['PUT'])
def update(paciente_id):
    data = request.get_json()
    tipo_id = data['tipo_id']
    nombre = data['nombre']
    email = data['email']
    grupo_sanguineo = data['grupo_sanguineo']
    genero = data['genero']
    edad = data['edad']
    fecha_nacimiento = data['fecha_nacimiento']
    direccion = data['direccion']
    celular = data['celular']
    eps = data['eps']
    serial_hc = data['serial_hc']
    return jsonify(update_paciente(tipo_id, nombre, email, grupo_sanguineo, genero, edad, fecha_nacimiento, direccion, celular, eps, serial_hc, paciente_id))

@bp.route('/<int:paciente_id>', methods=['DELETE'])
def delete(paciente_id):
    return jsonify(delete_paciente(paciente_id))
