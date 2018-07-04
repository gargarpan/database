import pymysql as pm

try:
    con = pm.connect(host='localhost', database='acadviewdb',\
                     user='root', password='root')
    
    cursor = con.cursor()
    
    query = 'create table book(Bno int(5) primary key, \
    Bname varchar(10), Bauthor varchar(10)'

     cursor.execute(query)
    
    print('Table created successfully!!')
    
    """query = "insert into book(bno, Bname, Bauthor) \
    values(%s, %s, %s, %s)"
    
    records = [(1, 'abc', 'ty' )
               (2, 'def', 'jg')
               (3, 'ghi', 'hj')]
    
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
