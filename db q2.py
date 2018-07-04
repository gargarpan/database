import pymysql as pm

try:
    con = pm.connect(host='localhost', database='acadviewdb',\
                     user='root', password='root')
    
    cursor = con.cursor()
    
    query = 'create table title(titleid int(5) primary key, \
    title varchar(10), publisherid int(4),publisheryear int(6)'
    
    cursor.execute(query)
    
    print('Table created successfully!!')

     """query = "insert into book(titleid, title, publisherid,publisheryear) \
    values(%s, %s, %s, %s)"
    
    records = [(1, 'abc', 4 ,2012)
               (2, 'def', 5,2019)
               (3, 'ghi', 6,2012)]
    
    cursor.executemany(query, records)"""
    con.commit()
    
except pm.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)
    
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('DONE!!')
