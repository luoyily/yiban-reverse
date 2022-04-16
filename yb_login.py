import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import requests
from urllib.parse import urlencode

pwd_enc_key = RSA.import_key(open("./pwd_enc_key.pem").read())


# RSA加密
def rsa_encrypt(pubkey, message):
    cipher = PKCS1_v1_5.new(pubkey)
    return base64.b64encode(cipher.encrypt(message.encode())).decode()


# print(rsa_encrypt(pwd_enc_key, "123456"))
def login(user, password):
    url = 'https://m.yiban.cn/api/v4/passport/login'
    headers = {'Authorization': 'Bearer',
               'loginToken': '',
               'AppVersion': '5.0.8',
               'User-Agent': 'YiBan/5.0.8 Mozilla/5.0 (Linux; Android 7.1.2; wv) AppleWebKit/537.36 (KHTML, like Gecko)'
                             ' Version/4.0 Chrome/81.0.4044.114 Mobile Safari/537.36',
               'Content-Type': 'application/x-www-form-urlencoded',
               'Host': 'm.yiban.cn',
               'Connection': 'Keep-Alive',
               'Accept-Encoding': 'gzip'
               }
    payload = {'device': 'XINGZOU:Note 7 Pro',
               'v': '5.0.8',
               'password': rsa_encrypt(pwd_enc_key, password),
               'token': '',
               'mobile': user,
               'ct': '2',
               'identify': '114514191981011',
               'sversion': '25',
               'app': '1',
               'apn': 'wifi',
               'authCode': '',
               'sig': '7170zo191911bb45'
               }
    r = requests.post(url, data=urlencode(payload), headers=headers)
    return r.text.encode('utf-8').decode('unicode_escape')


res = login('13911451919', '123456')
print(res)

