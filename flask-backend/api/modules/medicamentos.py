import functools
from flask import Blueprint, request, jsonify
from flask_cors import CORS
from model.medicamentos import (
    get_medicamentos,
    # get_user,
    # create_user,
    # update_user,
    # delete_user,
)

bp = Blueprint('medicamentos', __name__, url_prefix='/medicamentos')
CORS(bp)

@bp.route('/', methods=['GET'])
def list():
    retorno = get_medicamentos()
    return jsonify(retorno)

# @bp.route('/<int:user_id>', methods=['GET'])
# def get(user_id):
#     return jsonify(get_user(user_id))

# @bp.route('/', methods=['POST'])
# def create():
#     data = request.get_json()
#     name = data['name']
#     lastname = data['lastname']
#     return jsonify(create_user(name, lastname))

# @bp.route('/<int:user_id>', methods=['PUT'])
# def update(user_id):
#     data = request.get_json()
#     name = data['name']
#     lastname = data['lastname']
#     return jsonify(update_user(name, lastname, user_id))

# @bp.route('/<int:user_id>', methods=['DELETE'])
# def delete(user_id):
#     return jsonify(delete_user(user_id))
