from flask import Blueprint, request
from db import query_db, modify_db
from datetime import datetime
import responses
import os

upload_dir = Blueprint('upload_dir', __name__)


# 文件上传
@upload_dir.route('/api/upload/l4/client', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return responses.callback_public_fileerr1
    file = request.files['file']
    if file.filename == '':
        return responses.callback_public_fileerr1
    if file:
        filepath = os.path.join('../pilot-client/pages/upload/', file.filename)
        file.save(filepath)
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        modify_db("INSERT INTO FILE (FILENAME, HASHNAME, TIME) VALUES (%s, %s, %s)",(file.filename, file.filename, time))
        return responses.update_callback(responses.callback_public_uploadsucc, {'file': "/pages/upload/"+file.filename, 'filename': file.filename, 'time': time})
    else:
        return responses.callback_public_fileerr1

# 文件列表
@upload_dir.route('/api/upload/l4/getfile', methods=['GET'])
def get_file():
    res = query_db("SELECT FILENAME,HASHNAME,TIME FROM FILE")
    return responses.update_callback(responses.callback_public_getinfo, {"msg": res})

# 文件删除
@upload_dir.route('/api/upload/l4/delfile', methods=['GET'])
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