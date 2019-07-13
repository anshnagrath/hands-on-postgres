from psycopg2 import pool
# using one pool connection througout
cp =   pool.SimpleConnectionPool(1,1,user='postgres', password='wezzy33beat',database='learning',host='localhost')
class ConnectionFromPool:
    def __init__(self):
       self.connection = None

    def __enter__(self):
        self.connection = cp.getconn()    
        return self.connection
    def __exit__(self,exc_type,exc_val,exc_tb):
        self.connection.commit()
        cp.putconn(self.connection)
