# -*- coding: utf-8 -*-
import json
import uuid

from com.aliyun.api.gateway.sdk import client
from com.aliyun.api.gateway.sdk.http import request
from com.aliyun.api.gateway.sdk.common import constant

host = "${HOST}"
url = "${URL}"

cli = client.DefaultClient(app_key="${APP_KEY}", app_secret="${APP_SECRET}")

req_post = request.Request(host=host, protocol=constant.HTTPS, url=url, method="POST", time_out=30000, sign_with_body=False)
bodyMap = {
    'id': str(uuid.uuid4()),
    'version': "1.0",
    'request': {
        'iotToken': "xxxx",
        'apiVer': "1.0.0"
    },
    'params': {
        #接口参数
    }
}
req_post.set_body(bodyMap)
req_post.set_content_type(constant.CONTENT_TYPE_JSON)
print(cli.execute(req_post))
