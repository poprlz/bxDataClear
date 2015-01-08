#-*- coding:utf-8 -*-
__author__ = 'poprlz'

import MySQLdb
import datetime



class ClearWorker:
    def __init__(self,dbConnect):
        self.dbConnect = dbConnect;

    def getClear(self,startDate=datetime.datetime.now(),endDate=datetime.datetime.now()):
        sqlCmd = "SELECT id FROM vehicle_enquiry WHERE date_created>='" + startDate.strftime('%Y-%m-%d %H:%M:%S')
        sqlCmd += "' AND date_created<='" + endDate.strftime('%Y-%m-%d %H:%M:%S') +"'"
        print sqlCmd
        cur = self.dbConnect.cursor()
        cur.execute(sqlCmd)
        result = [row[0] for row in cur.fetchall()]
        print result
        cur.close()
        return result

class EnquiryClear:
    def __init__(self,enquiryId,dbConnect):
        self.enquiryId = enquiryId
        self.dbConnect = dbConnect

    def clear(self):
        sqlCmds=[
            "DELETE FROM vehicle_enquiry_temp WHERE id ='" + self.enquiryId +"'",
            "DELETE FROM quote_task_history WHERE enquiry_id ='" + self.enquiryId +"'",
            "DELETE FROM insure_task_history WHERE enquiry_id ='" + self.enquiryId +"'"
        ]
        for sqlCmd in sqlCmds:
            print(sqlCmd)


dbConnection = MySQLdb.connect(db='b2b_biz1',host='203.195.162.237',user='slaveroot',passwd='64CiM2brB%',port=33041)
EnquiryClear('1212121',dbConnection).clear()



