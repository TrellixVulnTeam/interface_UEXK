#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 14:00
# @Author  : Carewn
# @Software: PyCharm



#https://img02.ydm01.com/images/20180609/135841298478c06baa11e88cc7a54cacd1e82b.jpg
#
# import requests
# data = {
#     'imageUrl':'https://img02.ydm01.com/images/20180609/135841298478c06baa11e88cc7a54cacd1e82b.jpg'
# }
# headers = {
#     'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoie1wiQVVUSF9NQVBcIjp7XCI5MDAwMFwiOnRydWUsXCI5MDEwMFwiOnRydWUsXCI5MDEwMVwiOnRydWUsXCIxMDAwMDBcIjp0cnVlLFwiMTAwMTAwXCI6dHJ1ZSxcIjEwMDEwMVwiOnRydWUsXCIxMDAxMDJcIjp0cnVlLFwiMTAwMTAzXCI6dHJ1ZSxcIjEwMDIwMFwiOnRydWUsXCIxMDAyMDFcIjp0cnVlLFwiMTAwMjAyXCI6dHJ1ZSxcIjEwMDMwMFwiOnRydWUsXCIxMDAzMDFcIjp0cnVlLFwiMTAwMzAyXCI6dHJ1ZSxcIjEwMDUwMFwiOnRydWUsXCIxMDA1MDFcIjp0cnVlLFwiMTAwNjAwXCI6dHJ1ZSxcIjEwMDYwMVwiOnRydWUsXCIxMDA5MDBcIjp0cnVlLFwiMTAwOTAxXCI6dHJ1ZSxcIjEwMDkwMlwiOnRydWUsXCIxMDEwMDBcIjp0cnVlLFwiMTAxMDAxXCI6dHJ1ZSxcIjEwMTAwMlwiOnRydWUsXCIxMDExMDBcIjp0cnVlLFwiMTAxMTAxXCI6dHJ1ZSxcIjEwMTMwMFwiOnRydWUsXCIxMDEzMDFcIjp0cnVlLFwiMTAxMzAyXCI6dHJ1ZSxcIjEwMTQwMFwiOnRydWUsXCIxMDE0MDFcIjp0cnVlLFwiMTAxNDAyXCI6dHJ1ZSxcIjEwMTYwMFwiOnRydWUsXCIxMDE2MDFcIjp0cnVlLFwiMTAxNzAwXCI6dHJ1ZSxcIjEwMTcwMVwiOnRydWUsXCIxMDE4MDBcIjp0cnVlLFwiMTAxODAxXCI6dHJ1ZSxcIjEwMTkwMFwiOnRydWUsXCIxMDE5MDFcIjp0cnVlLFwiMTAyMDAwXCI6dHJ1ZSxcIjEwMjAwMVwiOnRydWUsXCIxMDIxMDBcIjp0cnVlLFwiMTAyMTAxXCI6dHJ1ZSxcIjEwMjEwMlwiOnRydWUsXCIxMTAwMDBcIjp0cnVlLFwiMTEwMTAwXCI6dHJ1ZSxcIjExMDEwMVwiOnRydWUsXCIxMTAxMDJcIjp0cnVlLFwiMTEwMTAzXCI6dHJ1ZSxcIjExMDEwNFwiOnRydWUsXCIxMTAxMDVcIjp0cnVlLFwiMTEwMjAwXCI6dHJ1ZSxcIjExMDIwMVwiOnRydWUsXCIxMTAyMDJcIjp0cnVlLFwiMTEwMzAwXCI6dHJ1ZSxcIjExMDMwMVwiOnRydWUsXCIxMTAzMDJcIjp0cnVlLFwiMTEwNDAwXCI6dHJ1ZSxcIjExMDQwMVwiOnRydWUsXCIxMTA0MDJcIjp0cnVlLFwiMTIwMDAwXCI6dHJ1ZSxcIjEyMDEwMFwiOnRydWUsXCIxMjAxMDFcIjp0cnVlLFwiMTIwMTAyXCI6dHJ1ZSxcIjEyMDEwM1wiOnRydWUsXCIxMjAxMDRcIjp0cnVlLFwiMTIwMTA2XCI6dHJ1ZSxcIjEyMDIwMFwiOnRydWUsXCIxMjAyMDFcIjp0cnVlLFwiMTMwMDAwXCI6dHJ1ZSxcIjEzMDEwMFwiOnRydWUsXCIxMzAxMDFcIjp0cnVlLFwiMTMwMTAyXCI6dHJ1ZSxcIjEzMDIwMFwiOnRydWUsXCIxMzAyMDFcIjp0cnVlLFwiMTMwMjAyXCI6dHJ1ZSxcIjEzMDMwMFwiOnRydWUsXCIxMzAzMDFcIjp0cnVlLFwiMTMwMzAyXCI6dHJ1ZSxcIjEzMDQwMFwiOnRydWUsXCIxMzA0MDFcIjp0cnVlLFwiMTMwNDAyXCI6dHJ1ZSxcIjEzMDUwMFwiOnRydWUsXCIxMzA1MDFcIjp0cnVlLFwiMTMwNTAyXCI6dHJ1ZSxcIjEzMDYwMFwiOnRydWUsXCIxMzA2MDFcIjp0cnVlLFwiMTMwNjAyXCI6dHJ1ZSxcIjEzMDcwMFwiOnRydWUsXCIxMzA3MDFcIjp0cnVlLFwiMTMwNzAyXCI6dHJ1ZSxcIjE0MDAwMFwiOnRydWUsXCIxNDAxMDBcIjp0cnVlLFwiMTQwMTAxXCI6dHJ1ZSxcIjE0MDEwMlwiOnRydWUsXCIxNDAyMDBcIjp0cnVlLFwiMTQwMjAxXCI6dHJ1ZSxcIjE0MDIwMlwiOnRydWUsXCIxNDAzMDBcIjp0cnVlLFwiMTQwMzAxXCI6dHJ1ZSxcIjE0MDMwMlwiOnRydWUsXCIxNDA0MDBcIjp0cnVlLFwiMTQwNDAxXCI6dHJ1ZSxcIjE0MDQwMlwiOnRydWUsXCIxNTAwMDBcIjp0cnVlLFwiMTUwMTAwXCI6dHJ1ZSxcIjE1MDEwMVwiOnRydWUsXCIxNTAxMDJcIjp0cnVlLFwiMTUwMjAwXCI6dHJ1ZSxcIjE1MDIwMVwiOnRydWUsXCIxNTAyMDJcIjp0cnVlLFwiMTUwMjA1XCI6dHJ1ZSxcIjE1MDMwMFwiOnRydWUsXCIxNTAzMDFcIjp0cnVlLFwiMTUwMzAyXCI6dHJ1ZSxcIjE1MDQwMFwiOnRydWUsXCIxNTA0MDFcIjp0cnVlLFwiMTUwNDAyXCI6dHJ1ZSxcIjE1MDUwMFwiOnRydWUsXCIxNTA1MDFcIjp0cnVlLFwiMTUwNTAyXCI6dHJ1ZSxcIjE1MDUwM1wiOnRydWUsXCIxNjAwMDBcIjp0cnVlLFwiMTYwMTAwXCI6dHJ1ZSxcIjE2MDEwMVwiOnRydWUsXCIxNjAxMDJcIjp0cnVlLFwiMTYwMTAzXCI6dHJ1ZSxcIjE2MDEwNFwiOnRydWUsXCIxNjAxMDZcIjp0cnVlLFwiMTYwMTA3XCI6dHJ1ZSxcIjE2MDEwOFwiOnRydWUsXCIxNjAxMDlcIjp0cnVlLFwiMTYwMTEwXCI6dHJ1ZSxcIjE2MDExMVwiOnRydWUsXCIxNjAxMTJcIjp0cnVlLFwiMTcwMDAwXCI6dHJ1ZSxcIjE3MDEwMFwiOnRydWUsXCIxNzAxMDFcIjp0cnVlLFwiMTcwMTAyXCI6dHJ1ZSxcIjE3MDEwM1wiOnRydWUsXCIxODAwMDBcIjp0cnVlLFwiMTgwMTAwXCI6dHJ1ZSxcIjE4MDEwMVwiOnRydWUsXCIxOTAwMDBcIjp0cnVlLFwiMTkwMTAwXCI6dHJ1ZSxcIjE5MDEwMVwiOnRydWUsXCIxOTAxMDJcIjp0cnVlLFwiMTkwMjAwXCI6dHJ1ZSxcIjE5MDIwMVwiOnRydWUsXCIxOTAzMDBcIjp0cnVlLFwiMTkwMzAxXCI6dHJ1ZSxcIjE5MDQwMFwiOnRydWUsXCIxOTA0MDFcIjp0cnVlLFwiMTkwNTAwXCI6dHJ1ZSxcIjE5MDUwMVwiOnRydWUsXCIyMDAwMDBcIjp0cnVlLFwiMjAwMTAwXCI6dHJ1ZSxcIjIwMDEwMVwiOnRydWUsXCIyMDAxMDJcIjp0cnVlLFwiMjEwMDAwXCI6dHJ1ZSxcIjIxMDEwMFwiOnRydWUsXCIyMTAxMDFcIjp0cnVlLFwiMjEwMjAwXCI6dHJ1ZSxcIjIxMDIwMVwiOnRydWUsXCIyMTAzMDBcIjp0cnVlLFwiMjEwMzAxXCI6dHJ1ZSxcIjIyMDAwMFwiOnRydWUsXCIyMjAxMDBcIjp0cnVlLFwiMjIwMTAxXCI6dHJ1ZSxcIjIyMDEwMlwiOnRydWUsXCIyMjAyMDBcIjp0cnVlLFwiMjIwMjAxXCI6dHJ1ZSxcIjIyMDIwMlwiOnRydWUsXCIyMzAwMDBcIjp0cnVlLFwiMjMwMTAwXCI6dHJ1ZSxcIjIzMDEwMVwiOnRydWUsXCIyMzAxMDNcIjp0cnVlLFwiMjMwMjAwXCI6dHJ1ZSxcIjIzMDIwMVwiOnRydWUsXCIyMzAyMDNcIjp0cnVlLFwiMjMwMzAwXCI6dHJ1ZSxcIjIzMDMwMVwiOnRydWUsXCIyMzAzMDNcIjp0cnVlLFwiMjMwNDAwXCI6dHJ1ZSxcIjIzMDQwMVwiOnRydWUsXCIyMzA0MDNcIjp0cnVlLFwiMjMwNTAwXCI6dHJ1ZSxcIjIzMDUwMVwiOnRydWUsXCIyMzA1MDNcIjp0cnVlLFwiMjMwNjAwXCI6dHJ1ZSxcIjIzMDYwMVwiOnRydWUsXCIyMzA2MDNcIjp0cnVlLFwiMjMwNzAwXCI6dHJ1ZSxcIjIzMDcwMVwiOnRydWUsXCIyMzA4MDBcIjp0cnVlLFwiMjMwODAxXCI6dHJ1ZSxcIjIzMDgwM1wiOnRydWUsXCIyNDAwMDBcIjp0cnVlLFwiMjQwMTAwXCI6dHJ1ZSxcIjI0MDEwMVwiOnRydWUsXCIyNDAxMDJcIjp0cnVlLFwiMjQwMjAwXCI6dHJ1ZSxcIjI0MDIwMVwiOnRydWUsXCIyNDAzMDBcIjp0cnVlLFwiMjQwMzAxXCI6dHJ1ZSxcIjI0MDQwMFwiOnRydWUsXCIyNDA0MDFcIjp0cnVlLFwiMjYwMDAwXCI6dHJ1ZSxcIjI2MDEwMFwiOnRydWUsXCIyNjAxMDFcIjp0cnVlLFwiMjYwMTAyXCI6dHJ1ZSxcIjI2MDEwM1wiOnRydWUsXCIyNjAxMDRcIjp0cnVlLFwiMjYwMTA1XCI6dHJ1ZSxcIjI2MDEwNlwiOnRydWUsXCIyNjAxMDdcIjp0cnVlLFwiMjYwMTA4XCI6dHJ1ZSxcIjI2MDEwOVwiOnRydWUsXCIyNjAxMTBcIjp0cnVlLFwiMjYwMTExXCI6dHJ1ZSxcIjI2MDExMlwiOnRydWUsXCIyNjAyMDBcIjp0cnVlLFwiMjYwMjAxXCI6dHJ1ZSxcIjI2MDIwMlwiOnRydWUsXCIyNjAzMDBcIjp0cnVlLFwiMjYwMzAxXCI6dHJ1ZSxcIjI2MDMwMlwiOnRydWUsXCIyNzAwMDBcIjp0cnVlLFwiMjcwMTAwXCI6dHJ1ZSxcIjI3MDEwMVwiOnRydWUsXCIyNzAxMDJcIjp0cnVlLFwiMjcwMjAwXCI6dHJ1ZSxcIjI3MDIwMVwiOnRydWUsXCIyNzAyMDJcIjp0cnVlLFwiMjcwMzAwXCI6dHJ1ZSxcIjI3MDMwMVwiOnRydWUsXCIyNzAzMDJcIjp0cnVlLFwiMjgwMDAwXCI6dHJ1ZSxcIjI4MDEwMFwiOnRydWUsXCIyODAxMDFcIjp0cnVlLFwiMjgwMTAyXCI6dHJ1ZSxcIjI5MDAwMFwiOnRydWUsXCIyOTAxMDBcIjp0cnVlLFwiMjkwMTAxXCI6dHJ1ZSxcIjI5MDIwMFwiOnRydWUsXCIyOTAyMDFcIjp0cnVlLFwiMjkwMzAwXCI6dHJ1ZSxcIjI5MDMwMVwiOnRydWUsXCIyOTA0MDBcIjp0cnVlLFwiMjkwNDAxXCI6dHJ1ZSxcIjI5MDUwMFwiOnRydWUsXCIyOTA1MDFcIjp0cnVlLFwiMzAwMDAwXCI6dHJ1ZSxcIjMwMDEwMFwiOnRydWV9LFwidXNlcl9pZFwiOjE2NzI1MyxcIlRFTFBIT05FXCI6XCIxODY2NDMwOTg2NFwiLFwibWVyY2hhbnRfaWRcIjo4MTEzNixcIk1FUl9BRE1JTl9JRFwiOjgxMTM2LFwiaXNfYWRtaW5cIjp0cnVlLFwiaXNfbWFzdGVyXCI6ZmFsc2UsXCJMT0dJTl9NRVJDSEFOVF9MSVNUXCI6W3tcIk1FUkNIQU5UX0lEXCI6ODI4NTIsXCJNRVJDSEFOVF9OQU1FXCI6XCLnvo7kuL3kuZ3kuZ1cIn0se1wiTUVSQ0hBTlRfSURcIjo4Mjg1NixcIk1FUkNIQU5UX05BTUVcIjpcIui_mOWOn-e-jlwifSx7XCJNRVJDSEFOVF9JRFwiOjgyOTM4LFwiTUVSQ0hBTlRfTkFNRVwiOlwi5L2g5aW95ryC5LquXCJ9LHtcIk1FUkNIQU5UX0lEXCI6ODExMzcsXCJNRVJDSEFOVF9OQU1FXCI6XCLljZPotorlupdcIn0se1wiTUVSQ0hBTlRfSURcIjo4MTE2NyxcIk1FUkNIQU5UX05BTUVcIjpcIuWNmuWbreW6l1wifSx7XCJNRVJDSEFOVF9JRFwiOjgxMzcwLFwiTUVSQ0hBTlRfTkFNRVwiOlwi576k5pif5bm_5Zy65bqXXCJ9LHtcIk1FUkNIQU5UX0lEXCI6ODEzOTUsXCJNRVJDSEFOVF9OQU1FXCI6XCLlh6Tlh7DlpKfljqblupdcIn0se1wiTUVSQ0hBTlRfSURcIjo4MTM5NixcIk1FUkNIQU5UX05BTUVcIjpcIuazouaJmOiPsuivuuW6l1wifSx7XCJNRVJDSEFOVF9JRFwiOjgxMzk3LFwiTUVSQ0hBTlRfTkFNRVwiOlwi6aaW5Zyw5a655b6h5bqXXCJ9LHtcIk1FUkNIQU5UX0lEXCI6ODEzNjQsXCJNRVJDSEFOVF9OQU1FXCI6XCLkuK3mtbfllYbln47lupdcIn0se1wiTUVSQ0hBTlRfSURcIjo4MjA5NCxcIk1FUkNIQU5UX05BTUVcIjpcIuWRiOaCpuWMu-eWl-mXqOivilwifSx7XCJNRVJDSEFOVF9JRFwiOjgxOTkyLFwiTUVSQ0hBTlRfTkFNRVwiOlwi5Lic5rW35Zu96ZmF5bqXXCJ9LHtcIk1FUkNIQU5UX0lEXCI6ODIwNDksXCJNRVJDSEFOVF9OQU1FXCI6XCLmmJPmgJ3ljZrlupdcIn0se1wiTUVSQ0hBTlRfSURcIjo4MjA1MCxcIk1FUkNIQU5UX05BTUVcIjpcIuWFhumCpuWfuuW6l1wifSx7XCJNRVJDSEFOVF9JRFwiOjgyMDcwLFwiTUVSQ0hBTlRfTkFNRVwiOlwi6b6Z5YWJ5bqXXCJ9LHtcIk1FUkNIQU5UX0lEXCI6ODIzNDksXCJNRVJDSEFOVF9OQU1FXCI6XCLor5fnvo7pgLhHT1wifSx7XCJNRVJDSEFOVF9JRFwiOjgyMDUxLFwiTUVSQ0hBTlRfTkFNRVwiOlwi5paw5aSp5LiW57qq5bqXXCJ9LHtcIk1FUkNIQU5UX0lEXCI6ODIzMTcsXCJNRVJDSEFOVF9OQU1FXCI6XCJHT-adpee-juWQp1wifSx7XCJNRVJDSEFOVF9JRFwiOjgyMjQzLFwiTUVSQ0hBTlRfTkFNRVwiOlwi5b-r5p2l576OXCJ9LHtcIk1FUkNIQU5UX0lEXCI6ODIwNzEsXCJNRVJDSEFOVF9OQU1FXCI6XCLmtbflsrjln47lupdcIn0se1wiTUVSQ0hBTlRfSURcIjo4MjA2NCxcIk1FUkNIQU5UX05BTUVcIjpcIuS4rea0suW6l1wifSx7XCJNRVJDSEFOVF9JRFwiOjgyMDY1LFwiTUVSQ0hBTlRfTkFNRVwiOlwi5aSn5Yay5bqXXCJ9LHtcIk1FUkNIQU5UX0lEXCI6ODIwNjYsXCJNRVJDSEFOVF9OQU1FXCI6XCLlsJrpg73lupdcIn0se1wiTUVSQ0hBTlRfSURcIjo4MjcwNixcIk1FUkNIQU5UX05BTUVcIjpcIuW_q-adpee-jumhuuW-t-W6l1wifSx7XCJNRVJDSEFOVF9JRFwiOjgyNzE4LFwiTUVSQ0hBTlRfTkFNRVwiOlwi5ruf5r6c5bGxR09cIn0se1wiTUVSQ0hBTlRfSURcIjo4MjcxNCxcIk1FUkNIQU5UX05BTUVcIjpcIuivl-e-jumAuOS4iemHjOays1wifV0sXCJ0aW1lc3RhbXBcIjoxNTI4NTIzODkwNTg0fSIsImFsZ29yaXRobSI6IkhTNTEyIiwiaWF0IjoxNTI4NTIzODkwLCJleHAiOjE1Mjg1MzEwOTB9.0-F7MkDlvNy3h7SXrNDkTeFD7Ra9jkdu5DSwW79GzQE'
# }
#
# r = requests.post('https://saas.ydm01.com/api/platform/licenseRecognition',data=data,headers=headers)
# print (r.json())
#
#
# url = 'https://api.youtu.qq.com/youtu/ocrapi/bizlicenseocr'
# #
# headers = {
#     "Host":'api.youtu.qq.com',
#     "Content_Length":1024,
#     "Content_Type":'text/json',
#     "Authorization":''
#
# }
# data = {
#     "app_id":'10136140',
#     "url":'https://img02.ydm01.com/images/20180609/135841298478c06baa11e88cc7a54cacd1e82b.jpg'
# }
# r = requests.post(url,data=data)
# print (r.json())
import requests
import time
import TencentYoutuyun


import sys

#sys.path.insert(os.path.join(os.path.dirname('.')+'/TencentYoutuyun'))

#------------------------------------------腾讯优图api
# appid = '10136140'
# secret_id = 'AKIDDG5g3CGmESRBhyiqQmtlQt88vTmqMFZe'
# secret_key = 'we7LJ3kFYdWCfvyoQp10mKgqoY9WfZGk'
# youtus = TencentYoutuyun.YouTu(appid=appid,secret_id=secret_id,secret_key=secret_key)
# youtuss = youtus.bizlicenseocr(image_path='https://img02.ydm01.com/images/20180609/135841298478c06baa11e88cc7a54cacd1e82b.jpg',data_type=1)
# for i in youtuss['items']:
#     print (str(i).encode('utf-8').decode('gbk'))
ssss = 1
i = True
while i:
    import requests
    url = 'http://ggbxcwx.ydm01.cn/api/ydm_xc_new/create_project_order'
    data = {
        'userId':'190273',
        'merchantId':'81167',
        "shareMerchantId":"81167",
        "cMerchantId":"81136",
        "login_merchant_id":"81136",
        "login_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoie1wieGNfdXNlcl9pZFwiOjE5MDI3MyxcInhjX21lcmNoYW50X2lkXCI6ODExMzYsXCJtYWxsX2lkXCI6MjM5NjMsXCJtYWxsX3VzZXJfaWRcIjoxOTAyNzMsXCJ0aW1lc3RhbXBcIjoxNTI4NDUzMjA3NTg4fSIsImFsZ29yaXRobSI6IkhTNTEyIiwiaWF0IjoxNTI4NDUzMjA3LCJleHAiOjE1MzEwNDUyMDd9.HBQFDSFJTRM0k7Z3QourluK09qOrUN-c6JD7b3G68D8",
        "order_id":"127226",
        "projectId":"45531",
        "beauticianId":"",
        "count":"2",
        "makeTime":"",
        "saleId":"",
        "isCart":"false",
        "couponId":"",
        "redBgId":""
    }
    headers = {
        'authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoie1wieGNfdXNlcl9pZFwiOjE5MDI3MyxcInhjX21lcmNoYW50X2lkXCI6ODExMzYsXCJtYWxsX2lkXCI6MjM5NjMsXCJtYWxsX3VzZXJfaWRcIjoxOTAyNzMsXCJ0aW1lc3RhbXBcIjoxNTI4NDUzMjA3NTg4fSIsImFsZ29yaXRobSI6IkhTNTEyIiwiaWF0IjoxNTI4NDUzMjA3LCJleHAiOjE1MzEwNDUyMDd9.HBQFDSFJTRM0k7Z3QourluK09qOrUN-c6JD7b3G68D8'
    }
    r = requests.post(url,data=data,headers=headers)
    print (r.json())

    urls = 'http://ggbxcwx.ydm01.cn/api/ydm_xc_new/queryWaitOrderDetail'
    ss = {
        "login_merchant_id":"81136",
        "login_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoie1wieGNfdXNlcl9pZFwiOjE5MDI3MyxcInhjX21lcmNoYW50X2lkXCI6ODExMzYsXCJtYWxsX2lkXCI6MjM5NjMsXCJtYWxsX3VzZXJfaWRcIjoxOTAyNzMsXCJ0aW1lc3RhbXBcIjoxNTI4NDUzMjA3NTg4fSIsImFsZ29yaXRobSI6IkhTNTEyIiwiaWF0IjoxNTI4NDUzMjA3LCJleHAiOjE1MzEwNDUyMDd9.HBQFDSFJTRM0k7Z3QourluK09qOrUN-c6JD7b3G68D8",
        "orderId":r.json()['orderId']
    }
    s = requests.post(urls,data=ss)
    print (s.json())
    ssss += 1
    print (ssss)










