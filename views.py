from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from convert_query import build_query, get_resault
from models import RequestSchema

main_bp = Blueprint('main', __name__)

FILE_NAME = 'data/apache_logs.txt'


@main_bp.route('/perform_query', methods=['POST'])
def perform_query():

    data = request.json
    try:
        check_data = RequestSchema().load(data)
    except ValidationError as error:
        return jsonify(error.messages), 400

    cmd = check_data.get('cmd1')
    value = check_data.get('value1')
    file_name = check_data.get('file_name')
    data = get_resault(cmd, value, file_name, None)

    cmd = check_data.get('cmd2')
    value = check_data.get('value2')
    file_name = check_data.get('file_name')
    result = get_resault(cmd, value, file_name, data)

    return jsonify(result)
