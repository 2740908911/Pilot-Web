from flask import Blueprint, request, send_file
import responses

filedownload = Blueprint('filedownload', __name__)

# 下载接口
@filedownload.route('/api/fd/l1/download',methods=['GET'])
@responses.check_get(['file'])
def download():
    file_path = request.args['file']
    try:
        file = "download/" + file_path
        return send_file(file, as_attachment=True)
    except:
        return responses.callback_public_fileerr1