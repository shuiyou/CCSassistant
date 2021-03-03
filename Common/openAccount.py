import requests
from flask import json

from DataBaseUtils import sql_query
from config import CCS_DB
import URLconfig
from logger.logger_util import LoggerUtil

dbname = CCS_DB
CompanyVeifyurl = 'http://192.168.1.15:100/gateway/defensor/api/verify/company'
logger = LoggerUtil().logger(__name__)
needOpen =[{'客户名称': '张三', '客户类型': 'PERSONAL', '客户证件号': '61387487384475375487', '客户手机号': 13709876543, '客户配偶名称': '李四', '客户配偶证件号': 7.384787584738573e+16, '客户配偶手机号': 13812345678.0}, {'客户名称': '殷宏伟', '客户类型': 'PERSONAL', '客户证件号': '42020219770909191X', '客户手机号': 13709876543, '客户配偶名称': None, '客户配偶证件号': None, '客户配偶手机号': None}, {'客户名称': '彭思思', '客户类型': 'PERSONAL', '客户证件号': '420281198507024268', '客户手机号': 13709876543, '客户配偶名称': None, '客户配偶证件号': None, '客户配偶手机号': None}]

openCompanyResutl =[]



#判断公司用户是否已经存在
def isComExist(certNo)->bool:
    flag = False
    sql_company = "select * from cus_com where cert_code = '%s' " % certNo
    rs = sql_query(sql=sql_company,dbname=dbname)
    if rs is None or len(rs)==0:
        return flag
    cus_name = dict(rs[0])['CUS_NAME']
    cus_id = dict(rs[0])['CUST_MGR']
    queryINfo ="select r.USR_NAME,b.BCH_DESC from s_usr r, s_bch b  where r.USR_BCH=b.BCH_CDE and r.USR_CDE='%s'" %cus_id
    info =sql_query(sql=queryINfo,dbname=dbname)
    main_br_id =dict(info[0])['BCH_DESC']
    cus_mgr =dict(info[0])['USR_NAME']
    logger.info("信贷系统已经存在客户:%s,隶属于%s,管户人%s",cus_name,main_br_id,cus_mgr)
    flag = True
    return flag


def creatCompanyInfo(name,certNo,input):
    sql_insert='''
        
    '''
    logger.info("批量开户开始--->开户公司名称：%s,开户证件号：%s",name,certNo)
    pass


def OpenCompanyCust(name,certNo):
    if isComExist(certNo) is not True:
        if riskAuthCus(name,certNo) is True:
            creatCompanyInfo()
    logger.info("开户失败")




def riskAuthCus(name = None,certNO= None):
    flag = False
    cusCom ={}
    cusCom['name']=name
    cusCom['idNo']=certNO
    headers ={'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJjY3MiLCJhdXRoIjoiYXVfYWRtaW4sYXVfaW5uZXIsYXVfcmVnZW4scF8xcGVyLHBfMWVudCxwXzF1bmlvbixwXzFwb3N0LHBfMmNyZWRpdCxwXzJmbG93LG1fZW1wbG95ZWUsbV9yb2xlcyxtX3N1YmplY3QsbV9jb250cm9sLG1fcmlza19saXN0LG1fZ3JleSxtX3NfcmVwb3J0LHBfMXVuaW9uMixtX2N1c19tZ3IsbV9teV9jdXMsbV9hdV9za2lwX2FwcGx5LG1fY3JlZGl0X3VwbG9hZCxwXzJlbnRfY3JlZGl0LG1fbG9nbyIsInVpZCI6NTAsImFwcElkIjoiMDAwMDAwMDAwMCIsIm1pZCI6MjcsImlzQWRtaW4iOnRydWUsImV4cCI6MTY3MjM5MTYxNn0.CqbuukevXVU4vZy_sa2KXWvEAhoUk47BahpWgGpmPOpBqMe8ATX3XElk0CQFQTeQY3Eu1s5x4iRC5f7puJ2BCg','Content-Type':'application/json;charset=UTF-8'}
    rep =requests.post(CompanyVeifyurl,headers=headers,data=json.dumps(cusCom))
    data =json.loads(rep.text)
    if data['resCode']==0:
        flag =True
        return flag
    logger.info("湛卢验证结果%s",data['resMsg'])
    return flag





if __name__ == '__main__':
    OpenCompanyCust("重庆市展平商贸有限公司","915001045634716156")