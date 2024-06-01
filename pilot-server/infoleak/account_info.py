from flask import Blueprint, request
from db import query_db
import responses
import hashlib

account_info = Blueprint('account_info', __name__)


# 登录接口
@account_info.route('/api/il/l3/login',methods=['POST'])
@responses.check_post(['username', 'password'])
def Login():
    username = request.form['username']
    password = request.form['password']
    if username == "pilottest123" and password == "fanqie@123":
        return responses.update_callback(responses.callback_public_loginsucc, {'username': '测试管理员1'})
    else:
        return responses.callback_public_loginerr1