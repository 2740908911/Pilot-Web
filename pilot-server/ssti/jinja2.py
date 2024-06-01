from flask import Blueprint, request, render_template_string
import responses

jinja2 = Blueprint('jinja2', __name__)

# 跳转URL
@jinja2.route('/api/ssti/l1/jinja2', methods=['GET'])
@responses.check_get(['param'])
def ssti_jinja2():
    param = request.args['param']
    rendered_template = render_template_string(param)
    return rendered_template
    
