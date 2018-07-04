import pymysql as pm

try:
    con = pm.connect(host='localhost', database='acadviewdb',\
                     user='root', password='root')
    
    cursor = con.cursor()
    
    query = 'create table author(authorid int(5) primary key, \
    firstname varchar(10), middlename varchar(4),lastname varchar(5)'
    
    cursor.execute(query)
    
    print('Table created successfully!!')

     """query = "insert into author(authorid, firstname, middlename,lastname) \
    values(%s, %s, %s, %s)"
    
    records = [(1, 'abc', 'asd','asdf')
               (2, 'def', 'qw'.'asc')
               (3, 'ghi','vb','cf')]
    
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
