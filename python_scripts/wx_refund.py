#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Ben liu"
# 微信支付申请退款 test 
import requests
import hashlib
#from requests import Request,Session
adict = {}
def list2dict(list):
    sDict = {}
    for n in list:
        if type(n) == 'str':
            temp = n.split('=')
            sDict.update({temp[0]:temp[1]})
    return sDict
# 返回数据
def getResult(url,xml):
    req = requests.post(url,data=xml)
    if req.status_code == 200 :
        print '返回数据成功!'
        return 200
    else:
        return 500


def requestWx(adict):
    
    if(adict is None or len(adict) == 0):
        return 'not enter into params'

    s = requests.Session()
    s.cert = ("D:/python/benling/cert/apiclient_cert.pem","D:/python/benling/cert/apiclient_key.pem")
    url = "https://api.mch.weixin.qq.com/secapi/pay/refund"
    heads = {"Connection":"keep-alive", "Accept":"*/*", 
        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
        "Host":"api.mch.weixin.qq.com","X-Requested-With":"XMLHttpRequest",
        "Cache-Control":"max-age=0","User-Agent":"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)"
    }
    s.headers = heads

    # xml = '''
    # <xml>
    # <appid>wxc03e6d04e533f08b</appid>
    # <mch_id>1273298401</mch_id>
    # <nonce_str>9xvdt84c3mv95ya4</nonce_str>
    # <op_user_id>1273298401</op_user_id>
    # <out_refund_no>20180824112516172479514</out_refund_no>
    # <out_trade_no>20180821182040509452012</out_trade_no>
    # <refund_fee>1</refund_fee>
    # <sign>5AD5B5D4CE6A00D1A2DF6FE222690F03</sign>
    # <sub_appid>wx5a907d3a22f8c254</sub_appid>
    # <sub_mch_id >1509741601</sub_mch_id >
    # <total_fee>1</total_fee>
    # </xml>
    # '''
    dict = {
        "appid":"wxc03e6d04e533f08b","mch_id":"1273298401",
        "op_user_id":"1273298401","sub_appid":"wx5a907d3a22f8c254","sub_mch_id":"1509741601"
    }
    # 把传入的参数进行叠加
    dict.update(adict)
    print dict

    # dict = {
    #     "appid":"wxc03e6d04e533f08b","mch_id":"1273298401","nonce_str":"9xvdt84c3mv95ya4",
    #     "op_user_id":"1273298401","out_refund_no":"20180824112516172479514","out_trade_no":"20180821182040509452012",
    #     "refund_fee":'1',"sub_appid":"wx5a907d3a22f8c254","sub_mch_id":"1509741601","total_fee":'1'
    # }
    #dict.keys().sort()
    scret_key ="Tsw8AmW7aiK2Y490bpcqYwTf617Q0Key"
    list = []
    for key in sorted(dict.keys()):
        list.append('='.join((key,dict[key])))

    list.append('='.join(('key',scret_key)))
    str = '&'.join(list)
    print str
    h = hashlib.md5()
    h.update(str.encode(encoding='utf-8'))
    print u'Md5加密前:' + str

    sign = h.hexdigest()
    print u'Md5加密后:' + h.hexdigest()
    print sign.upper()
    x = {"sign": sign.upper()}
    dict.update(x)
    # 生成xml 文档
    #xml = '<xml>'
    tlist = []
    for key in sorted(dict.keys()):
        temp = '<%s>%s</%s>' % (key,dict[key],key)
        print temp
        tlist.append(temp)
    xml = '<xml>' + ''.join(tlist) + '</xml>'
    print xml
    req = s.post(url,data=xml,verify=True)
    print req.status_code
    if req.status_code == requests.codes.ok :
        print req.text.encode('ISO-8859-1').decode('utf-8')
        return req.text.encode('ISO-8859-1').decode('utf-8')
if __name__ == '__main__':
	requestWx(adict)    
