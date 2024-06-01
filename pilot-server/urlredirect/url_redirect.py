from flask import Blueprint, request, redirect
import responses

url_redirect = Blueprint('url_redirect', __name__)

# 跳转URL
@url_redirect.route('/api/ur/l1/getimg', methods=['GET'])
@responses.check_get(['url'])
def get_img():
    url = request.args['url']
    if url.startswith('http://') or url.startswith('https://'):
        return redirect(url)
    else:
        return responses.callback_public_urlerr1
