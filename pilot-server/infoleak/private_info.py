from flask import Blueprint, request
from db import query_db
import responses

private_info = Blueprint('private_info', __name__)


@private_info.route('/api/il/l2/getUserinfo',methods=['GET'])
def getUserinfo():
    res = query_db("SELECT * FROM VIRTUAL_USERINFO")
    return responses.update_callback(responses.callback_public_getinfo, {"msg": res})

    
