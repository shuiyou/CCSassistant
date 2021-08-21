import yaml

ConfigYamlPath ='../config/'

class LoadingYamlFIle():

    def __init__(self, filename):
        if filename is None:
            self.context = None
        self.context =self.openSpecifyYamlFIle(filename)

    def openSpecifyYamlFIle(self,filename):
        yaml.warnings({'YAMLLoadWarning': False})
        f = open(ConfigYamlPath+filename, 'r', encoding='utf-8')
        cfg = f.read()
        d=yaml.load(cfg)
        return d


#获取数据库连接信息
    def connectInfoDB(self,dbName):
        if dbName is not None:
            self.host =self.context[dbName]['host']
            self.username =self.context[dbName]['username']
            self.passwork =self.context[dbName]['passwork']
            self.port =self.context[dbName]['port']
            self.database=self.context[dbName]['database']
            infoList =[]
            infoList.append(self.host)
            infoList.append(self.self.username)
            infoList.append(self.passwork)
            infoList.append(self.port)
            infoList.append(self.database)
            return infoList
        return None











if __name__ == '__main__':
     a = LoadingYamlFIle('config.yaml')
     a.connectInfoDB('CCS_Extend')