#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Ben liu"
# 依赖 mysql-connector-python
from mysql.connector import MySQLConnection, Error
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# config connection
config = {
  'user': 'root',
  'password': 'Tsw567@abc',
  'host': 'localhost',
  'database': 'platform',
  'raise_on_warnings': True,
  'charset': 'utf8'
}

# 轮循订单日志表，查找支付成功的订单,并累加消费金额、进行二级分佣，产生冻结佣金
def call_cost_sp():

    try:
        cnx = MySQLConnection(**config)
        cursor = cnx.cursor()
        query = '''select order_id,user_id,actual_price from nideshop_order_log 
        where status=0 and type=0;'''
        cursor.execute(query)
        rows = cursor.fetchall()
        print("read", cursor.rowcount, "rows of data.")
        # 支付成功的订单，将进行录入并做冻结二级分佣
        for row in rows:
            aList = [row[0], row[1], float(row[2])]
            print(aList)
            # 调用存储过程做录入、冻结二级分佣操作，做完操作会将轮循日志表type=1状态	
            cursor.callproc('sp_add_user_cost', aList)
            cnx.commit()
        print u'调用存储过程sp_add_user_cost 完毕................'
        # 查询已签收的并已录入、冻结二级分佣的订单进行解冻、分佣操作
        query = ''' select order_id,user_id,actual_price from nideshop_order_log 
        where status = 1 and type = 1;'''
        cursor.execute(query)
        sussRows = cursor.fetchall()
        print("read", cursor.rowcount, "rows of data.")
        for row in sussRows:
            bList = [row[0], row[1], float(row[2])]
            print(bList)
            cursor.callproc("sp_two_level_funds", bList)
            cnx.commit()
        print u'调用存储过程sp_two_level_funds 完毕................'
        # 查询已签收的并已做解冻、已二级分佣的订单,进行代理商分佣
        query = ''' select order_id,user_id,actual_price from nideshop_order_log 
        where status = 1 and type = 2;'''
        cursor.execute(query)
        rows = cursor.fetchall()
        print("read", cursor.rowcount, "rows of data.")
        for row in rows:
            bList = [row[0], row[1], float(row[2])]
            print(bList)
            cursor.callproc("sp_proxy_funds_operation", bList)
            cnx.commit()
        print u'调用存储过程sp_proxy_funds_operation完毕................'
        # 查询已退款的订单,进行退款操作
        query = ''' select order_id, user_id, actual_price, type from nideshop_order_log 
        where status = 2;'''
        cursor.execute(query)
        rows = cursor.fetchall()
        print("read", cursor.rowcount, "rows of data.")
        for row in rows:
            bList = [row[0], row[1], float(row[2]),row[3]]
            print(bList)
            cursor.callproc("sp_back_funds", bList)
            cnx.commit()
        print u'调用存储过程sp_back_funds执行退款操作完毕................'
    except Error as e:
        print(e)
    finally:
        cursor.close()
        cnx.close()
if __name__ == '__main__': 
    call_cost_sp()
