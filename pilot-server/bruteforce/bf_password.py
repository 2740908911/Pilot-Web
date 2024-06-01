from flask import Blueprint, request
from db import query_db
import responses
import hashlib

bf_password = Blueprint('bf_password', __name__)


# 登录接口
@bf_password.route('/api/bf/l2/login',methods=['POST'])
@responses.check_post(['username', 'password'])
def Login():
    username = request.form['username']
    password = request.form['password']
    user = query_db("SELECT USERNAME FROM USER WHERE (USERNAME = %s AND PASSWORD = %s)", (username, hashlib.md5(password.encode("utf-8")).hexdigest()))
    if user:
        return responses.update_callback(responses.callback_public_loginsucc, {'username': user[0]["USERNAME"]})
    else:
        return responses.callback_public_loginerr1
    
    