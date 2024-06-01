from flask import Blueprint, request
from db import query_db
import responses
import hashlib

bf_username = Blueprint('bf_username', __name__)


# 登录接口
@bf_username.route('/api/bf/l1/login',methods=['POST'])
@responses.check_post(['username', 'password'])
def Login():
    username = request.form['username']
    password = request.form['password']
    user = query_db("SELECT USERNAME FROM USER WHERE ((USERNAME = %s OR PHONE = %s) AND PASSWORD = %s)", (username, username, hashlib.md5(password.encode("utf-8")).hexdigest()))
    if user:
        return responses.update_callback(responses.callback_public_loginsucc, {'username': user[0]["USERNAME"]})
    else:
        check_name = query_db("SELECT USERNAME FROM USER WHERE (USERNAME = %s OR PHONE = %s)", (username, username))
        if check_name:
            return responses.callback_bf_username_err1
        else:
            return responses.callback_bf_username_err2

    
    