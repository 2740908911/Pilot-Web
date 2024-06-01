from flask import Blueprint, request
import requests
import responses

ssrf = Blueprint('ssrf', __name__)

# SSRF远程解析
@ssrf.route('/api/ssrf/l1/getinfo', methods=['GET'])
@responses.check_get(['url'])
def fetch():
    url = request.args['url']
    if url.startswith('file://'):
        try:
            filepath = url[7:]
            with open(filepath, 'r', encoding="utf-8") as file:
                return file.read()
        except Exception as e:
            print(e)
            return responses.callback_public_urlerr1
    else:
        try:
            res = requests.get(url)
            res.encoding = 'utf-8'
            return res.text
        except Exception as e:
            return responses.callback_public_urlerr1