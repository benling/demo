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
    'host': '192.168.108.222',
    'database': 'platform',
    'raise_on_warnings': True,
    'charset': 'utf8'
}

#
# 查询会员消费金额，达到级别，进行分佣，并更新等级
def call_change_grade():

    try:
          cnx = MySQLConnection(**config)
          cursor = cnx.cursor()
          print(u'开始查询会员消费金额，达到等级要求的会员将进行升级分佣并更新等级操作')
          # 直属下线累积消费10000元或者，自身消费10000元的会员，达到升级初级代理要求 ( 会员升 初级)
          print(u'查询会员自我消费或直属下线累积消费达到1万元的会员....')
          query = '''select user_id, self_cost,total_cost from nideshop_user_cost 
          where grade = %d and (self_cost >= %f or total_cost >= %f);''' % (1, 10000, 10000)
          print(query)
          cursor.execute(query)
          rows = cursor.fetchall()
          print("read", cursor.rowcount, "rows of data.")
          aList = []
          for row in rows:
              selfCost = float(row[1])
              totalCost = float(row[2])
              cost = totalCost if totalCost >= selfCost else selfCost
              aList = [row[0], cost, 1, 2, 1]
              print(aList)
              cursor.callproc('sp_change_funds_operation', aList)
              cnx.commit()
          print(u'查询会员结束...')
          # 中级代理升级： 如果直属下线累积消费大于等于10万元，或自我消费大于等于5万元，则升级为中级，并分佣 ( 初级升 中级)
          print(u'开始查询直属下线累积消费10万元或自我消费大于等于5万的初级代理....')
          query = '''select user_id, self_cost, total_cost from nideshop_user_cost where grade = %d and (self_cost >= %f or total_cost >= %f ); ''' % (2, 50000, 100000)
          print(query)
          cursor.execute(query)
          rows = cursor.fetchall()
          print("read", cursor.rowcount, "rows of data .")
          for row in rows: 
			  selfCost = float( row[1])
			  totalCost = float( row[2])
			  cost = totalCost if totalCost >= selfCost else selfCost
			  aList = [row[0], cost, 2, 3, 2]
			  print(aList)
			  cursor.callproc("sp_change_funds_operation",aList)
			  cnx.commit()
          print(u'查询初级代理结束...')
          # 中级升高级,直属下线累积消费大于20万元，或者自我消费大于等于10万元的
          print(u'开始查询直属下线累积消费大于等于20万元，或者自我消费大于等于10万元的中级代理')
          query = '''select user_id, self_cost,total_cost from nideshop_user_cost 
          where grade = %d and (self_cost >= %f or total_cost >= %f);''' % (3, 100000, 200000)
          print(query)
          cursor.execute(query)
          rows = cursor.fetchall()
          print("read", cursor.rowcount, "rows of data.")
          for row in rows: 
			  selfCost = float( row[1])
			  totalCost = float( row[2])
			  cost = totalCost if totalCost >= selfCost else selfCost
			  aList = [row[0], cost, 3, 4, 3]
			  print(aList)
			  cursor.callproc("sp_change_funds_operation",aList)
			  cnx.commit()
          print(u'查询中级代理结束...')
    except Error as e:
	    print(e)
    finally:
	    cursor.close()
	    cnx.close()
if __name__ == '__main__':
	call_change_grade()