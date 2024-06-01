from flask import Blueprint, request
from db import query_db
import responses

system_info = Blueprint('system_info', __name__)


@system_info.route('/api/il/l1/getNext1',methods=['GET'])
@responses.check_get(['param'])
def getNext1():
    param = request.args["param"]
    query = "SELECT " + param + " FROM USER"
    try:
        a = query_db(query)
        return responses.callback_system_info_l1
    except Exception as e:
        if "1064" in str(e):
            return responses.update_callback(responses.callback_public_sqlerror, {'msg': str(e)})
        else:
            return responses.callback_system_info_l1

@system_info.route('/api/il/l1/getNext2',methods=['GET'])
def getNext2():
    return responses.callback_system_info_l2
    
    