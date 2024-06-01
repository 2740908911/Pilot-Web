from flask import Blueprint, request
from db import query_db, modify_db
from datetime import datetime
import responses
import os

upload_server1 = Blueprint('upload_server1', __name__)


# 文件上传
@upload_server1.route('/api/upload/l2/client', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return responses.callback_public_fileerr1
    file = request.files['file']
    if file.filename == '':
        return responses.callback_public_fileerr1

    # 文件后缀黑名单
    if os.path.splitext(file.filename)[1] in [".html",".exe",".pdf",".py",".php",".svg",".zip",".rar",".7z",".tar",".js",".xml",".doc",".docx",".xlsx",".xls",".pptx",".ppt",".jsp"]:
        return responses.callback_public_uploaderr
        
    if file:
        encrypted_filename = encrypt_filename(file.filename)
        filepath = os.path.join('../pilot-client/pages/upload/', encrypted_filename)
        file.save(filepath)
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        modify_db("INSERT INTO FILE (FILENAME, HASHNAME, TIME) VALUES (%s, %s, %s)",(file.filename, encrypted_filename, time))
        return responses.update_callback(responses.callback_public_uploadsucc, {'file': encrypted_filename, 'filename': file.filename, 'time': time})
    else:
        return responses.callback_public_fileerr1

# 文件列表
@upload_server1.route('/api/upload/l2/getfile', methods=['GET'])
def get_file():
    res = query_db("SELECT FILENAME,HASHNAME,TIME FROM FILE")
    return responses.update_callback(responses.callback_public_getinfo, {"msg": res})

# 文件删除
@upload_server1.route('/api/upload/l2/delfile', methods=['GET'])
@responses.check_get(['file'])
def del_file():
    hashname = request.args['file']
    if query_db("SELECT FILENAME FROM FILE WHERE HASHNAME = %s", (hashname)) and hashname != "fanqieLogo.png":
        modify_db("DELETE FROM FILE WHERE HASHNAME = %s",(hashname))
        file_path = os.path.join('../pilot-client/pages/upload/', hashname)
        if os.path.exists(file_path):
            os.remove(file_path)
        else :
            return responses.callback_public_filedelerr
        return responses.callback_public_filedelsucc
    else:
        return responses.callback_public_filedelerr


import hashlib
SALT = "fanqie./upload"

def encrypt_filename(filename):
    name_part, extension = os.path.splitext(filename)
    name = name_part + SALT + datetime.now().strftime("%Y%m%d%H%M%S%f")
    md5_hash = hashlib.md5(name.encode()).hexdigest()
    encrypted_filename = f"{md5_hash}{extension}"
    return encrypted_filename
