import pandas as pd
from sqlalchemy import create_engine
from CCSsqlCF import afterLoanReportSql
from ExcelUtil import writeExcel
from config import CCS_DB



def chooseMysqlDB(dbname):
    DB_URI = 'mysql+pymysql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % dbname
    _DB_ENGINE = create_engine(DB_URI, encoding="utf8")
    return _DB_ENGINE



def sql_to_df(sql, dbname,index_col=None, coerce_float=True, params=None,
              parse_dates=None, columns=None, chunksize=None):
    df = pd.read_sql(sql, con=chooseMysqlDB(dbname), index_col=index_col, coerce_float=coerce_float, params=params,
                     parse_dates=parse_dates, columns=columns, chunksize=chunksize)
    return df



"""
获取sql 查询结果 
 :return: resultList [{'key'}:'val']
"""
def sql_query(sql, dbname,index_col=None, coerce_float=True, params=None,
               parse_dates=None, columns=None, chunksize=None):
    sqlService = chooseMysqlDB(dbname)
    res_rows = sqlService.execute(sql).fetchall()
    result = [dict(zip(result.keys(), result)) for result in res_rows]
    return result












if __name__ == '__main__':
    a =CCS_DB
    # sqlStrate = '''
    #     select cus_id from cus_indiv where cus_name='林小龙'
    #
    # '''
    # df =sql_query(sql=sqlStrate,dbname=a)
    # print(dict(df[0])['cus_id'])
    sqlStrate =afterLoanReportSql
    df = sql_to_df(sql=sqlStrate, dbname=a)
    writeExcel(df,'/Users/hanxiaodi/PycharmProjects/CCSassistant/excelTempleFile/贷后报告统计.xlsx')
