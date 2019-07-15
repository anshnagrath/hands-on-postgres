from user import User
from database import Database
db = Database()
db.initialise(user='postgres', password='wezzy33beat',database='learning',host='localhost')
user = User('ansh@gmail.com','ansh','nagrath',None)
user.save_to_db()
my_user = User.load_from_db_email('anshnagrath@gmail.com')
print(my_user)