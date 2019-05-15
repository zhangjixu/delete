# -*- coding: utf-8 -*-

import requests
import json

if __name__ == '__main__':
    url = ""
    phone_info = json.dumps({"phones": "13003872621,13006863853", "updt_day": "1556640000000"})
    headers = {'content-type': 'application/json'}
    try:
        res = requests.post(url=url, data=phone_info, headers=headers)

        if res:
            print res.text
            json_result = json.loads(res.content)
            print json_result

    except Exception as e:
        print e