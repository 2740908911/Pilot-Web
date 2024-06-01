from flask_cors import CORS
from flask import Flask

# flask route list
from bruteforce.bf_username import bf_username
from bruteforce.bf_password import bf_password
from bruteforce.bf_token import bf_token
from vcdefect.vc_bypass_c import vc_bypass_c
from vcdefect.vc_bypass_s import vc_bypass_s
from infoleak.system_info import system_info
from infoleak.private_info import private_info
from infoleak.account_info import account_info
from authority.unauthorized import unauthorized
from authority.horizontal import horizontal
from authority.vertical import vertical
from sqli.mysqli import mysqli
from sqli.mssqli import mssqli
from sqli.pgsqli import pgsqli
from xss.reflected import reflected
from xss.stored import stored
from urlredirect.url_redirect import url_redirect
from ssrf.ssrf import ssrf
from csrf.csrf import csrf
from upload.client import upload_client
from upload.server_1 import upload_server1
from upload.server_2 import upload_server2
from upload.upload_dir import upload_dir
from download.file_download import filedownload
from rce.rce import rce
from rce.rce_ping import rce_ping
from ssti.jinja2 import jinja2
from xxe.xxe import xxe
from serialize.serialize import serialize


pilot = Flask(__name__)
pilot.register_blueprint(bf_username, url_prefix="/")
pilot.register_blueprint(bf_password, url_prefix="/")
pilot.register_blueprint(bf_token, url_prefix="/")
pilot.register_blueprint(vc_bypass_c, url_prefix="/")
pilot.register_blueprint(vc_bypass_s, url_prefix="/")
pilot.register_blueprint(system_info, url_prefix="/")
pilot.register_blueprint(private_info, url_prefix="/")
pilot.register_blueprint(account_info, url_prefix="/")
pilot.register_blueprint(unauthorized, url_prefix="/")
pilot.register_blueprint(horizontal, url_prefix="/")
pilot.register_blueprint(vertical, url_prefix="/")
pilot.register_blueprint(mysqli, url_prefix="/")
pilot.register_blueprint(mssqli, url_prefix="/")
pilot.register_blueprint(pgsqli, url_prefix="/")
pilot.register_blueprint(reflected, url_prefix="/")
pilot.register_blueprint(stored, url_prefix="/")
pilot.register_blueprint(url_redirect, url_prefix="/")
pilot.register_blueprint(ssrf, url_prefix="/")
pilot.register_blueprint(csrf, url_prefix="/")
pilot.register_blueprint(upload_client, url_prefix="/")
pilot.register_blueprint(upload_server1, url_prefix="/")
pilot.register_blueprint(upload_server2, url_prefix="/")
pilot.register_blueprint(upload_dir, url_prefix="/")
pilot.register_blueprint(filedownload, url_prefix="/")
pilot.register_blueprint(rce, url_prefix="/")
pilot.register_blueprint(rce_ping, url_prefix="/")
pilot.register_blueprint(jinja2, url_prefix="/")
pilot.register_blueprint(xxe, url_prefix="/")
pilot.register_blueprint(serialize, url_prefix="/")

pilot.secret_key = 'pilot/web'
cors = CORS(pilot, supports_credentials=True)

@pilot.after_request
def set_response_content_type(response):
    response.headers['Content-Type'] = 'application/json'
    return response

if __name__ == "__main__":
    pilot.run()