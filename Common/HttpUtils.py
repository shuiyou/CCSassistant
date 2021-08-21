import requests

from Common.customerException import ParamException


@staticmethod
def dopost(url,data,charset,*args):
    rep = requests.post()


@staticmethod
def doget(url,token,params):
    finalurl = url+'？'+'token='+token
    if isinstance(params,dict):
        rep = requests.get(finalurl)
    else:
        raise ParamException()
