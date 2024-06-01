from flask import Blueprint, request
import responses
import base64
import pickle
import os

serialize = Blueprint('serialize', __name__)

@serialize.route('/api/unserialize/l1/pickle', methods=['POST'])
@responses.check_post(['command'])
def unserialize():
    command = request.form['command']
    try:
        cmd = pickle.loads(base64.b64decode(command))
        if cmd == "rm -rf /*":
            return responses.update_callback(responses.callback_public_cmderror, {"msg": "？？别干傻事"})
        output = os.popen(cmd).read()
        return responses.update_callback(responses.callback_public_getinfo, {"msg": output})
    except:
        return responses.callback_public_cmderror
    
