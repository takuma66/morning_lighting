import json
import time
import hashlib
import hmac
import base64
import uuid
import requests

# Declare empty header dictionary
apiHeader = {}

class Switchbot_Auth:
    def __init__(self, token, secret) -> None:
        self.token = token
        self.secret = secret

    def get_apiHeader(self):
        nonce = uuid.uuid4()
        t = int(round(time.time() * 1000))
        string_to_sign = '{}{}{}'.format(self.token, t, nonce)

        string_to_sign = bytes(string_to_sign, 'utf-8')
        self.secret = bytes(self.secret, 'utf-8')

        sign = base64.b64encode(hmac.new(self.secret, msg=string_to_sign, digestmod=hashlib.sha256).digest())
        # print ('Authorization: {}'.format(token))
        # print ('t: {}'.format(t))
        # print ('sign: {}'.format(str(sign, 'utf-8')))
        # print ('nonce: {}'.format(nonce))

        #Build api header JSON
        apiHeader['Authorization']=self.token
        apiHeader['Content-Type']='application/json'
        apiHeader['charset']='utf8'
        apiHeader['t']=str(t)
        apiHeader['sign']=str(sign, 'utf-8')
        apiHeader['nonce']=str(nonce)
        return apiHeader