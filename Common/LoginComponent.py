import json
from collections import namedtuple

import requests

#登录组建 LoginComponent -->DefensorClient
class LoginComponent():

    def  __int__(self,currentToken =None):
        self.defensorClient =DefensorClient()
        self.currentToken = currentToken
    def obtainToken(self,fullUrl,appId,userName,password,rememberMe):
        ApiResult = self.defensorClient.login(fullUrl,appId,userName,password,rememberMe)
        return ApiResult




#登录湛卢
class DefensorClient():

      def login(self,fullUrl,appId,userName,password,rememberMe):
        parameters={}
        parameters['appId']=appId
        parameters['userName']=userName
        parameters['password']=password
        parameters['rememberMe']=rememberMe
        rep =requests.post(fullUrl, params=parameters,verify=False)
        print("JWT_Token获取结果："+rep.text)
        data=json.loads(str(rep.text), object_hook =lambda d : namedtuple('X', d.keys())
               (*d.values()))
        return  JwtTokenUtils.fetchJwt(data)




#获取jwt——token
class JwtTokenUtils():

    @staticmethod
    def fetchJwt(apiResult):
        if apiResult.resCode =='0':
            return apiResult.data.jwt
        print(apiResult.resMsg)
        return None





if __name__ == '__main__':
    a = DefensorClient()
    a.login('http://192.168.1.15:100/gateway/defensor/api/open/jwt/login', '0000000000', 'ccs', 'ccs1234qwer', 'true')



    # data=str(a.login('http://192.168.1.15:100/gateway/defensor/api/open/jwt/login','0000000000','ccs1','ccs1234qwer','true'))
    # print()
    # x =json.loads(data, object_hook =lambda d : namedtuple('X', d.keys())
    #            (*d.values()))
    # c =JwtTokenUtils.fetchJwt(x)
    # print(c)