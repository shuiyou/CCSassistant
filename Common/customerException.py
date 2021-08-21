class ParamException(Exception):
    def __init__(self,params,needType):
        self.paramType = type(params)
        self.needType =needType
    def __str__(self):
        print('传入参数的类型 ：'+self.paramType+'所需要的参数类型 ：'+self.needType)