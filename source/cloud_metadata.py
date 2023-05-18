import requests
from flask import Flask
from flask import jsonify
from flask import request
import json
from functools import wraps
from requests.exceptions import HTTPError as HTTPError
from requests.exceptions import RequestException as RequestException

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
s = requests.Session()

target_url_list = [

]


url_list = [
"http://instance-data",
"http://169.254.169.254",
"http://169.254.169.254.nip.io/",
"http://425.510.425.510/",
"http://2852039166/",
"http://7147006462/",
"http://0xA9.0xFE.0xA9.0xFE/",
"http://0xA9FEA9FE/",
"http://0x41414141A9FEA9FE/",
"http://0251.0376.0251.0376/",
"http://0251.00376.000251.0000376/",
"http://0251.254.169.254",
"http://169.254.169.254/latest/user-data",
"http://169.254.169.254/latest/meta-data/iam/security-credentials/",
"http://169.254.169.254/latest/meta-data/",
"http://169.254.169.254/latest/meta-data/iam/security-credentials/PhotonInstance",
"http://169.254.169.254/latest/meta-data/ami-id",
"http://169.254.169.254/latest/meta-data/reservation-id",
"http://169.254.169.254/latest/meta-data/hostname",
"http://169.254.169.254/latest/meta-data/public-keys/",
"http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key",
"http://169.254.169.254/latest/meta-data/iam/security-credentials/dummy",
"http://169.254.169.254/latest/meta-data/iam/security-credentials/s3access",
"http://169.254.169.254/latest/dynamic/instance-identity/document",
"http://2852039166/latest/meta-data/",
"http://169.254.170.2/v2/credentials"]

positive_response_list = []
negative_response_list = []

def url_loop():
    for url in url_list:
        try:
            with s:
                url_req = s.get(url, timeout=15)
                url_req_response = url_req.content
                positive_response_list.append("{}: {}".format(url, url_req_response))
        except RequestException as RE:
            negative_response_list.append("{}: {}".format(url, RE))

@app.errorhandler(500)
def internal_server_error(error):
    return "HTTP 500 error"

@app.errorhandler(404)
def not_found_error(error):
    not_found_msg = """
    <h1>These are not the droids you are looking for.</h1>
    """
    return not_found_msg


@app.route('/')
def home():
    return """ WELCOME TO CLOUD METADATA Exposed Check"""



@app.route("/cm")
def metadata():
    url_loop()
    if len(positive_response_list) > 0:
        return "CRITICAL: Positive url(s) found: ", jsonify(positive_response_list)
    else:
        return "ALL GOOD: Negative url(s) found: ", jsonify(negative_response_list)
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port="80", threaded=True)
