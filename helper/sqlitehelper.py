import sqlite3


class SQLiteHelper(object):
    def __init__(self,db_name,):
        self.db_name = db_name
        
    def create_table(self,table_name,columns):
        name=str(self.db_name)
        self.conn = sqlite3.connect(name+'.db')
        self.c=self.conn.cursor()
        query='('
        query+='id INTEGER PRIMARY KEY'
        for key, value in columns.items():
            query+=','+key+' '+value
        query+=')'
        #print(query)
        self.c.execute("CREATE TABLE IF NOT EXISTS " + table_name+' '+query)
        self.conn.commit()
        #print("created")

    
    def selectAll(self,table_name):
        query="SELECT * FROM "+table_name
        return self.c.execute(query).fetchall()

    def getColumns(self,table_name):
        cursor = self.c.execute('select * from '+table_name)
        return list(map(lambda x: x[0], cursor.description))

    def selectWhereId(self,table_name,id):
        query="SELECT * FROM "+table_name
        query+=' where id='+str(id)
        cursor=self.c.execute(query).fetchone()
        columns=self.getColumns(table_name)
        data={}
        
        for i in range(0,len(columns)):
            data[columns[i]]=cursor[i]
        return data

    def insert(self,table_name,values):
        query='('
        query+='id'
        values_="("
        values_+='NULL'
        for key,value in values.items():
            values_+=",'"+str(value)+"'"
            query+=','+key
        query+=')'
        values_+=")"
        #print(values_)
        self.c.execute("INSERT INTO "+table_name+query+"VALUES"+values_)
        self.conn.commit()
        #print("inserted")