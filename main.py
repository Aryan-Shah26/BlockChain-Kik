import string
import random

user_data = {}

def generate_salt(lenght = 6):
    char = string.ascii_letters + string.digits
    return ''.join(random.choice(char) for i in range(lenght))

def hash(password,salt) :
    comb = password + salt
    hash_value = 0
    for i in comb :
        hash_value += ord(i)*(hash_value%7 + 1)
    return str(hash_value%100000000)

def sign_up():
    username  = input("Enter username : ")
    if username in user_data:
        print('Username already exists. Try another !')
        return
    
    password = input('Enter password : ')
    salt = generate_salt()
    hashed_password = hash(password,salt)
    user_data[username] = {'salt' : salt, 'hashed_password' : hashed_password}
    print('Sign-up successful !')

def log_in():
    username  = input("Enter username : ")
    if username not in user_data:
        print('Username does not exists. Try again!')
        return
    
    password = input('Enter password : ')
    salt = user_data[username]['salt']
    hashed_password = hash(password,salt)

    if hashed_password == user_data[username]['hashed_password']:
        print('Login Successful')

    else :
        print('Invalid Password')

while True:
    print("1. Sign Up")
    print("2. Log In")
    print("3. Exit")
    choice = input("Select an option: ")
    if choice == '1':
        sign_up()
    elif choice == '2':
        log_in()
    elif choice == '3':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.")