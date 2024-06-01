from flask import Blueprint, request, make_response
from db import query_db, modify_db
import responses
import hashlib
import base64

csrf = Blueprint('csrf', __name__)


# 登录接口
@csrf.route('/api/csrf/l1/login',methods=['POST'])
@responses.check_post(['username', 'password'])
def Login():
    username = request.form['username']
    password = request.form['password']
    user = query_db("SELECT USERNAME FROM USER WHERE (USERNAME = %s AND PASSWORD = %s)", (username, hashlib.md5(password.encode("utf-8")).hexdigest()))
    if user:
        return responses.update_callback(responses.callback_public_loginsucc, {'username': user[0]["USERNAME"], 'token': create_token(user[0]["USERNAME"])})
    else:
        return responses.callback_public_loginerr1

# 获取权限信息
@csrf.route('/api/csrf/l1/getUserinfo',methods=['GET'])
@responses.check_header(['Cookie'])
def getUserinfo():
    token = request.cookies.get('token', None)
    try:
        username = base64.b64decode(add_base64_padding(token.split('.')[1])).decode().split('"account":"')[1].split('"')[0]
        if verify_token(token,username):
            res = query_db("SELECT USERNAME,PHONE,QQ,PID FROM USER WHERE USERNAME = %s", (username))
            return responses.update_callback(responses.callback_public_getinfo, {"msg": res})
        else:
            return responses.update_callback(responses.callback_public_tokenerr, {'username': username})
    except:
        return responses.callback_public_tokenerr

# 垂直越权
@csrf.route('/api/csrf/l1/modifyUserInfo',methods=['GET'])
@responses.check_header(['Cookie'])
@responses.check_get(['phone', 'qq'])
def modifyUserInfo():
    phone = request.args['phone']
    qq = request.args['qq']
    token = request.cookies.get('token', None)
    try:
        account = base64.b64decode(add_base64_padding(token.split('.')[1])).decode().split('"account":"')[1].split('"')[0]
        if verify_token(token,account):
            modify_db("UPDATE USER SET PHONE = %s,QQ = %s WHERE USERNAME = %s", (phone, qq, account))
            return responses.callback_public_modifysuccess
        else:
            return responses.update_callback(responses.callback_public_tokenerr, {'username': account})
    except:
        return responses.responses.callback_public_tokenerr


# token模块
import datetime
import time
import jwt

SECRET_KEY = "PILOT/csrf_t0ken"

def time_str_int(date_str):
    '''将时间字符串转为时间戳'''
    ##将时间字符串转为时间数组
    timeArray = time.strptime(date_str, "%Y-%m-%d")
    ##将时间数组转为时间戳
    timeStamp = int(time.mktime(timeArray))
    return timeStamp

def create_token(account):
    '''生成本地token'''
    ##获取一天后的时间戳，token过期时间为一天后
    overdue_time=(datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    overdue_timeStamp = time_str_int(overdue_time)
    ###生成token
    own_token = jwt.encode({"account": account,"overdue_time":overdue_timeStamp}, SECRET_KEY, algorithm="HS256")
    return own_token

def verify_token(own_token,account):
    '''检验token'''
    try:
        ##解密token
        decode_token=jwt.decode(own_token, SECRET_KEY, algorithms=["HS256"])
        ##获取token中的account
        token_account=decode_token['account']
        ##获取token中的过期时间
        token_overdue_time=decode_token['overdue_time']
        ##获取当前时间的时间
        now_time=datetime.datetime.now().strftime("%Y-%m-%d")
        ##转为时间戳
        now_timeStamp = time_str_int(now_time)
        ###进行判断token,如果账号对的上以及当前访问时间没有超过token过期时间则返回True
        if token_account == account and now_timeStamp < token_overdue_time:
            return True
        else:
            return False
    except:
        return False

def add_base64_padding(data):
    # 计算缺少的填充字符数
    pad_len = 4 - (len(data) % 4)
    # 添加填充字符 '='
    return data + '=' * pad_len