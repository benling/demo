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

# 不断轮循初、中、高级代理，如果满足不同关系链中有四个以上（包含四个）平级代理，则升级
def call_user_grade():

    try:
        cnx = MySQLConnection(**config)
        cursor = cnx.cursor()
        # 查初级代理商，并调用存储过程检查不同关系链中有没有四个以上（包含四个）初级代理，如有则升级为中级代理
        query = '''select id,user_level_id from nideshop_user 
        where user_level_id=2;'''
        cursor.execute(query)
        rows = cursor.fetchall()
        print("read", cursor.rowcount, "rows of data.")
        for row in rows:
            bList = [row[0], row[1]]
            print(bList)
            cursor.callproc("sp_change_user_grade", bList)
            cnx.commit()
        print u'调用存储过程sp_change_user_grade 完毕................'
        # 查中级代理商，并调用存储过程检查不同关系链中有没有四个以上（包含四个）中级代理，如有则升级为高级代理
        query = '''select id,user_level_id from nideshop_user 
        where user_level_id=3;'''
        cursor.execute(query)
        sussRows = cursor.fetchall()
        print("read", cursor.rowcount, "rows of data.")
        for row in sussRows:
            bList = [row[0], row[1]]
            print(bList)
            cursor.callproc("sp_change_user_grade", bList)
            cnx.commit()
        print u'调用存储过程sp_change_user_grade完毕................'
        # 查高级代理商，并调用存储过程检查不同关系链中有没有四个以上（包含四个）高级代理，如有则升级为合伙人
        query = '''select id,user_level_id from nideshop_user 
        where user_level_id=4;'''
        cursor.execute(query)
        rows = cursor.fetchall()
        print("read", cursor.rowcount, "rows of data.")
        for row in sussRows:
            bList = [row[0], row[1]]
            print(bList)
            cursor.callproc("sp_change_user_grade", bList)
            cnx.commit()
        print u'调用存储过程sp_change_user_grade完毕................'
    except Error as e:
        print(e)
    finally:
        cursor.close()
        cnx.close()
if __name__ == '__main__': 
    call_user_grade()
