from database import ConnectionFromPool
class User:
    def __init__(self,email,first_name,last_name,id):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def __repr__(self):
        return  '< User {} >'.format(self.first_name)  

    def save_to_db(self):
        with ConnectionFromPool() as conection:
            with conection.cursor() as cursor:
               cursor.execute('INSERT INTO users (email, first_name, last_name) values (%s,%s,%s)',(self.email,self.first_name,self.last_name))
   
    @classmethod
    def load_from_db_email(cls,email):
        with ConnectionFromPool() as conection:
            with conection.cursor() as cursor:
                cursor.execute('select * from users where email=%s',(email,))
                user_data = cursor.fetchone()
                return cls(user_data[1],user_data[2],user_data[3],user_data[0])