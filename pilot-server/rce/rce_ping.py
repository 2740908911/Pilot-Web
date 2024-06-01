from flask import Blueprint, request
import responses
import re
import os

rce_ping = Blueprint('rce_ping', __name__)

@rce_ping.route('/api/rce/l2/ping', methods=['POST'])
@responses.check_post(['ip'])
def ping():
    ip = request.form['ip']
    ip_regex = r'\b(?:[0-9]{1,2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[0-9]{1,2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[0-9]{1,2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[0-9]{1,2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])\b'
    if not re.findall(ip_regex, ip):
        return responses.callback_rce_ping_iperror
    try:
        if "rm -rf /*" in ip:
            return responses.update_callback(responses.callback_public_cmderror, {"msg": "？？别干傻事"})
        cmd = "ping " + ip +" -c 3"
        output = os.popen(cmd).read()
        return responses.update_callback(responses.callback_public_getinfo, {"msg": output})
    except:
        return responses.callback_public_cmderror