from flask import Blueprint, request
import responses

reflected = Blueprint('reflected', __name__)

# 跳转URL
@reflected.route('/api/xss/l1/reflected', methods=['GET'])
@responses.check_get(['search'])
def xss_reflected():
    xss = request.args['search']
    # 伪造搜索
    res = "'" + xss + "' 的搜索结果：未找到资源！"
    return responses.update_callback(responses.callback_public_getinfo, {"msg": res})
