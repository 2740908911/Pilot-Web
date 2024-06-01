from flask import Blueprint, request
from db import query_db
import responses
import hashlib

vc_bypass_c = Blueprint('vc_bypass_c', __name__)


# 登录接口
@vc_bypass_c.route('/api/vc/l1/login',methods=['POST'])
@responses.check_post(['username', 'password', 'verify'])
def Login():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    if verify != "true":
        return responses.callback_public_vcerror
    user = query_db("SELECT USERNAME FROM USER WHERE (USERNAME = %s AND PASSWORD = %s)", (username, hashlib.md5(password.encode("utf-8")).hexdigest()))
    if user:
        return responses.update_callback(responses.callback_public_loginsucc, {'username': user[0]["USERNAME"]})
    else:
        return responses.callback_public_loginerr1