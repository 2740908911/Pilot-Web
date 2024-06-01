from flask import Blueprint, request
import responses
import base64
import os

rce = Blueprint('rce', __name__)

# RCE
@rce.route('/api/rce/l1/getprocess', methods=['POST'])
@responses.check_post(['command'])
def getprocess():
    command = request.form['command']
    try:
        cmd = base64.b64decode(command).decode()
        if cmd == "rm -rf /*":
            return responses.update_callback(responses.callback_public_cmderror, {"msg": "？？别干傻事"})
        output = os.popen(cmd).read()
        return responses.update_callback(responses.callback_public_getinfo, {"msg": output})
    except:
        return responses.callback_public_cmderror