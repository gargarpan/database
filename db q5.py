import pymysql as pm

try:
    con = pm.connect(host='localhost', database='acadviewdb',\
                     user='root', password='root')
    
    cursor = con.cursor()
    
    query = 'create table authortitle(authortitleid int(5) primary key, \
    authorid int(10), titleid int(4)'
    
    cursor.execute(query)
    
    print('Table created successfully!!')
     """query = "insert into authortitle(authortitleid, authorid, titleid) \
    values(%s, %s, %s, %s)"
    
    records = [(1, 'abc', 12)
               (2, 'def', 13)
               (3, 'ghi', 14)]
    
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
