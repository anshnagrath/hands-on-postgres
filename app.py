from user import User
my_user = User.load_from_db_email('anshnagrath@gmail.com')
print(my_user)