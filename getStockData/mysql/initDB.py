import pymysql
import time

def initMysql(param):
    method = param['method']
    
    db = pymysql.connect(host='localhost',
                             user='wefRoot',
                             password='wefRoot',
                             db='test')
    cursor = db.cursor()
    if method == 0:
        insertData(db, cursor, param)
    
   
def insertData(db, cursor, param):
    tableName = param['tableName']
    allNum = param['allNum']
    availableNum = param['availableNum']
    date = time.strftime("%Y-%m-%d", time.localtime())
    insert_sql = "insert into `%s` (`allNum`, `availableNum`, `date`)values('%s','%s','%s')" % (tableName,allNum, availableNum, date)
    try:
        select_sql = "select `allNum` from `zunJia0` where `allNum`='%s'" % allNum
        response = cursor.execute(select_sql)
        db.commit()
        if response == 1:
            print('该数据已存在...')
        else:
            try:
                cursor.execute(insert_sql)
                db.commit()
                print('更新成功...')
            except Exception as e:
                print('更新错误...', e)
                db.rollback()
    except Exception as e:
        print('查询错误...', e)
        db.rollback()
    finally:
        cursor.close()
        db.close()


