import pymysql as pm

try:
    con = pm.connect(host='localhost', database='acadviewdb',\
                     user='root', password='root')
    
    cursor = con.cursor()
    
    query = 'create table publisher(pubid int(5) primary key, \
    pubname varchar(10), publisheradd int(4),publisheryear int(6)'
    
    cursor.execute(query)
    
    print('Table created successfully!!')

     """query = "insert into publisher(pubid, pubname, publisheradd,publisheryear) \
    values(%s, %s, %s, %s)"
    
    records = [(1, 'abc', 'aaa' ,2012)
               (2, 'def', 'sss',2019)
               (3, 'ghi', 'ddd',2012)]
    
    cursor.executemany(query, records)
    con.commit()"""
    
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
