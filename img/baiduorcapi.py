# encoding:utf-8
import time

import base64
import requests
import os


def bdocrapitoken():
    clientid = 'w6TSCukAAg2eVKCR7LlWy86G'
    client_secret = '8lnwebUtd8WGMb4QqQYdY2k6xMgGQ2Yl'
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + clientid + '&client_secret=' + client_secret
    response = requests.get(host)
    token = response.json()['access_token']
    return token


'''
通用文字识别（高精度版）
'''


def bdocrapi(img):
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    # 二进制方式打开图片文件
    f = open(img, 'rb')
    img = base64.b64encode(f.read())
    f.close()
    params = {'image': img}
    access_token = bdocrapitoken()
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    # if response.json()['words_result_num']== 0:
    #     for i in range(10):
    #         time.sleep(10)
    #         respon = requests.post(request_url, data=params, headers=headers)
    #         print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    #         print('第'+str(i)+'次orcapi识别为空' + str(respon.json()))
    #         if response.json()['words_result_num']!= 0:
    #             response = respon
    #             print(response.json())
    #             return response
    if not str.find(str(response.json()), 'error_code') == 0:
        print('返回为空重新请求一遍')
        response = requests.post(request_url, data=params, headers=headers)
    print(response.json())
    code = response.json()['words_result']
    os.remove('../Upt/code.png')
    return code



if __name__ == '__main__':
    bdocrapi('./easy_img/aaa.png')
