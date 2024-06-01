from flask import Blueprint, request, session, send_file
from db import query_db
from io import BytesIO
import responses
import hashlib

vc_bypass_s = Blueprint('vc_bypass_s', __name__)


# 登录接口
@vc_bypass_s.route('/api/vc/l2/login',methods=['POST'])
@responses.check_post(['username', 'password', 'code'])
def Login():
    username = request.form['username']
    password = request.form['password']
    code = request.form['code']
    if 'code' in session and session['code'] == code:
        user = query_db("SELECT USERNAME FROM USER WHERE (USERNAME = %s AND PASSWORD = %s)", (username, hashlib.md5(password.encode("utf-8")).hexdigest()))
        if user:
            return responses.update_callback(responses.callback_public_loginsucc, {'username': user[0]["USERNAME"]})
        else:
            return responses.callback_public_loginerr1
    else:
        return responses.callback_public_vcerror

# 生成验证码
@vc_bypass_s.route('/api/vc/l2/getcode',methods=['GET'])
def captcha():
    captcha_text, captcha_image = generate_captcha()
    session['code'] = captcha_text.lower()
    return send_file(BytesIO(captcha_image), mimetype='image/png')


from PIL import Image
from captcha.image import ImageCaptcha
import string
import random

def generate_captcha():
    # 生成随机验证码文本
    captcha_text = ''.join(random.choices(string.ascii_letters + string.digits, k=4))

    # 创建验证码图片
    image = ImageCaptcha(width=160, height=60)
    data = image.generate(captcha_text)
    image = Image.open(data)

    # 将图片转换为二进制格式
    img_byte_arr = BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    return captcha_text, img_byte_arr
