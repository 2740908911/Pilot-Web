import json

# 公共响应包
callback_public_noparam = json.dumps({
    "status": "400",
    "msg": "缺少参数喔！"
    }, ensure_ascii=False), 200

callback_public_loginerr1 = json.dumps({
    "status": "401",
    "msg": "用户名或密码错误"
    }, ensure_ascii=False), 200

callback_public_vcerror = json.dumps({
    "status": "402",
    "msg": "验证码校验失败"
    }, ensure_ascii=False), 200

callback_public_noauth = json.dumps({
    "status": "403",
    "msg": "请求缺少权限认证，请重新登录！"
    }, ensure_ascii=False), 200

callback_public_loginsucc = json.dumps({
    "status": "200",
    "msg": "登陆成功",
    "username": "",
    "token": "leave out ..."
    }, ensure_ascii=False), 200

callback_public_getinfo = json.dumps({
    "status": "200",
    "msg": []
    }, ensure_ascii=False), 200

callback_public_tokenerr = json.dumps({
    "status": "403",
    "username": "",
    "msg": "Token过期或错误，请重新登录"
    }, ensure_ascii=False), 200

callback_public_autherr = json.dumps({
    "status": "400",
    "msg": "账号权限不足，请使用对应权限账号登录"
    }, ensure_ascii=False), 200

callback_public_modifysuccess = json.dumps({
    "status": "200",
    "msg": "修改成功"
    }, ensure_ascii=False), 200

callback_public_modifyerr1 = json.dumps({
    "status": "405",
    "msg": "默认管理员账号权限不可修改"
    }, ensure_ascii=False), 200

callback_public_urlerr1 = json.dumps({
    "status": "406",
    "msg": "访问失败，请检查URL是否正确"
    }, ensure_ascii=False), 200

callback_public_fileerr1 = json.dumps({
    "status": "407",
    "msg": "文件不存在"
    }, ensure_ascii=False), 200

callback_public_uploadsucc = json.dumps({
    "status": "200",
    "msg": "上传成功",
    "file": "",
    "filename": "",
    "time": ""
    }, ensure_ascii=False), 200

callback_public_filedelerr = json.dumps({
    "status": "408",
    "msg": "文件不可删除或文件不存在"
    }, ensure_ascii=False), 200

callback_public_filedelsucc = json.dumps({
    "status": "200",
    "msg": "删除成功"
    }, ensure_ascii=False), 200

callback_public_uploaderr = json.dumps({
    "status": "409",
    "msg": "该类型文件禁止上传！"
    }, ensure_ascii=False), 200

callback_public_sqlerror = json.dumps({
    "status": "500",
    "msg": ""
    }, ensure_ascii=False), 200

callback_public_cmderror = json.dumps({
    "status": "410",
    "msg": "参数有误，执行错误"
    }, ensure_ascii=False), 200

# 私有响应包
callback_bf_username_err1 = json.dumps({
    "status": "401",
    "msg": "密码错误"
    }, ensure_ascii=False), 200

callback_bf_username_err2 = json.dumps({
    "status": "402",
    "msg": "账号不存在，请注册"
    }, ensure_ascii=False), 200

callback_bf_token_verify = json.dumps({
    "status": "200",
    "msg": "验证成功",
    "username": "",
    "token": "leave out ..."
    }, ensure_ascii=False), 200

callback_system_info_l2 = json.dumps({
    "status": "200",
    "leak": "/api/il/l1/getNext1, This is the first system_info vulnerability",
    "msg": "这是第一个系统信息泄露漏洞，该类型漏洞可能会泄露SQL查询语句及错误信息、系统运行环境版本、系统绝对路径以及某些配置信息，可能会导致被攻击者进一步利用或为SQL注入以及其他漏洞提供有力支持。"
    }, ensure_ascii=False), 200

callback_system_info_l1 = json.dumps({
    "status": "200",
    "msg": "输入其他的字符试试吧！"
    }, ensure_ascii=False), 200

callback_rce_ping_iperror = json.dumps({
    "status": "411",
    "msg": "请检查IP输入"
    }, ensure_ascii=False), 200


def update_callback(original_callback, updates):
    original_data = json.loads(original_callback[0])
    updated_data = {**original_data, **updates}
    updated_response_content = json.dumps(updated_data, ensure_ascii=False)
    status_code = original_callback[1]
    return updated_response_content, status_code


from functools import wraps
from flask import request

def check_params(param_names, param_source):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            source = getattr(request, param_source)
            missing_or_empty_params = [param for param in param_names if not source.get(param)]
            if missing_or_empty_params:
                if param_source == 'headers' and 'Authorization' in missing_or_empty_params:
                    return callback_public_noauth
                return callback_public_noparam
            return func(*args, **kwargs)
        return wrapper
    return decorator


def check_get(param_names):
    return check_params(param_names, param_source='args')

def check_post(param_names):
    return check_params(param_names, param_source='form')

def check_header(param_names):
    return check_params(param_names, param_source='headers')