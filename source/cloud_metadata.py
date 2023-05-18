import requests
from flask import Flask
from flask import jsonify
from flask import request
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
s = requests.Session()

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
def metadata():
    with s:
        SSRF_url = "http://169.254.169.254/latest/meta-data/"
        get_data_request = s.get(url=SSRF_url)
        get_data_request.raise_for_status()
        get_data_response = json.dumps(get_data_request.json())

        return get_data_response
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port="80", threaded=True)
