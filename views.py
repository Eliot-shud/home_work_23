from flask import request, jsonify, Blueprint
from marshmallow import ValidationError

from convert_query import build_query
from models import BatchRequestSchema

main_bp = Blueprint('main', __name__, url_prefix='/perform_query')


@main_bp.route('/', methods=['POST'])
def post():
    req = request.json
    try:
        val_data = BatchRequestSchema().load(req)
    except ValidationError as error:
        return jsonify(error.messages), 400

    result = None
    for query in val_data['queries']:
        result = build_query(
            cmd=query['cmd'],
            value=query['value'],
            file_name=val_data['file_name'],
            data=result
        )
    return jsonify(result)