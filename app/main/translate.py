import json,requests,random,hashlib
from flask_babel import _
from flask import current_app

def translate(text,source_language,dest_language):
    if not current_app.config['AUTH']:
        return _('Error:the translation service is not configured.')
    salt = random.randint(32768,65536)
    sign = current_app.config['AUTH']['appid'] + text + str(salt) + current_app.config['AUTH']['key']
    sign = hashlib.md5(sign.encode()).hexdigest()
    r = requests.get('http://api.fanyi.baidu.com/api/trans/vip/translate'
                     '?q={}&from={}&to={}&appid={}&salt={}&sign={}'.format(
                         text,source_language,dest_language,
                         current_app.config['AUTH']['appid'],salt,sign))
    if r.status_code != 200:
        return _('Error:the translation service failed.')
    rawString = json.loads(r.content.decode('utf-8-sig'))
    result = rawString['trans_result'][0]['dst']
    return result
