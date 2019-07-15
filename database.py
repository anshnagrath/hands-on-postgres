from psycopg2 import pool

# using one pool connection througout
class Database:
    cp = None
    def initialise(self, **kwargs):
        cp =  pool.SimpleConnectionPool(1,1,**kwargs)

    @classmethod
    def get_connection(cls):
        return cls.cp.getconn()

    @classmethod
    def returnconnection(cls,connection):
        Database.cp.putconn(connection)  

    @classmethod
    def closeallconnection(cls):
        cls.cp.closeall()      

class ConnectionFromPool:
    global cp  
    cp =  pool.SimpleConnectionPool(1,1,user='postgres', password='wezzy33beat',database='learning',host='localhost')
    def __init__(self):
       self.connection = None
    def __enter__(self):
        self.connection = cp.getconn()    
        return self.connection
    def __exit__(self,exc_type,exc_val,exc_tb):
        if exc_val is not None:
            self.connection.rollback()
        else:    
            self.connection.commit()
            cp.putconn(self.connection)
