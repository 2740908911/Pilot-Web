from flask import Blueprint, request
from db import query_pgsql
import responses
import hashlib
import base64

pgsqli = Blueprint('pgsqli', __name__)


# 登录接口
@pgsqli.route('/api/sqli/l3/login',methods=['POST'])
@responses.check_post(['username', 'password'])
def Login():
    username = request.form['username']
    password = request.form['password']
    sql = 'SELECT "USERNAME" FROM pilot."USER" WHERE ("USERNAME" = \'' + username + '\' AND "PASSWORD" = \'' + hashlib.md5(password.encode("utf-8")).hexdigest() + '\')'
    try:
        user = query_pgsql(sql)
        if user:
            return responses.update_callback(responses.callback_public_loginsucc, {'username': user[0][0], 'token': create_token(user[0][0])})
        else:
            return responses.callback_public_loginerr1
    except Exception as e:
        return responses.update_callback(responses.callback_public_sqlerror, {'msg': str(e).split("CODE:")[0].strip()})

# 获取权限信息
@pgsqli.route('/api/sqli/l3/getAuthinfo',methods=['GET'])
@responses.check_header(['Authorization'])
@responses.check_get(['n'])
def getUserinfo():
    token = request.headers['Authorization']
    username = request.args['n']
    account = base64.b64decode(add_base64_padding(token.split('.')[1])).decode().split('"account":"')[1].split('"')[0]
    if verify_token(token,account):
        sql = 'SELECT "UID" FROM pilot."USER" WHERE "USERNAME" = \'' + username + '\''
        try:
            if query_pgsql(sql)[0][0] == 1:
                res = query_pgsql('SELECT "USERNAME","PHONE","QQ","PID","UID" FROM pilot."USER"')
                return responses.update_callback(responses.callback_public_getinfo, {"msg": transform_data(res)}) 
            else:
                return responses.callback_public_autherr
        except Exception as e:
            return responses.update_callback(responses.callback_public_sqlerror, {'msg': str(e).split("CODE:")[0].strip()})
    else:
        return responses.update_callback(responses.callback_public_tokenerr, {'username': username})

# token模块
import datetime
import time
import jwt

SECRET_KEY = "PILOT/pgsqli"

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

def transform_data(input_data):
    output_data = []
    for item in input_data:
        output_item = {
            'USERNAME': item[0],
            'PHONE': item[1],
            'QQ': item[2],
            'PID': item[3],
            'UID': item[4]
        }
        output_data.append(output_item)
    return output_data