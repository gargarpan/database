import pymysql as pm

try:
    con = pm.connect(host='localhost', database='acadviewdb',\
                     user='root', password='root')
    
    cursor = con.cursor()
    
    query = 'create table zipcode(zipcodeid int(5) primary key, \
    state varchar(10), city varchar(4)'
    
    cursor.execute(query)
    
    print('Table created successfully!!')
    
     """query = "insert into zipcode(zipcodeid, state, city) \
    values(%s, %s, %s, %s)"
    
    records = [(1, 'abc', 'aaa' )
               (2, 'def', 'sss')
               (3, 'ghi', 'ddd')]
    
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
