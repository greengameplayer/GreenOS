import time
import pickle
import hashlib
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os


def cls(): print("\n" * 100)
newHandoff = 0




#Prints out the time and intro
print("GreenOS - made by greengameplayer")
print(time.asctime( time.localtime(time.time())))

#asks user for information
user = input("Please input a Userfile, or type New for a new user: ")
#User creation
if user == "New":
    user = input("Please type a name: ")
    if user == "My name is Jeff":
        if _debug_:
            print("There was an error handling the new file: Jeff is a school meme. Don't use him like this!")
        raise SystemExit("There was an error handling the new file: Jeff is a school meme. Don't use him like this!")

    trueUser = user
    password  = input("Please input a password: ")
    encrypt = input("Would you like the file encrypted (y/n): ")
    if encrypt == "n":
        cls()
        print("!!!WARNING!!!WARNING!!!WARNING!!!WARNING!!!WARNING!!!WARNING!!!WARNING!!!WARNING!!!WARNING!!!")
        print("     Using an unencrypted file is unsecure! Do not use this file for any private data!")
        _useless = input("                              Acknowladge?")
        _useless = ("null")
        encrypted = 0
    if encrypt == "y":
        password = bytes(password, 'utf8')
        user = bytes(user, 'utf8')
        salt = os.urandom(16)
        kdf= PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
            )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        passwordTrue = password.decode('utf8')
        enc = Fernet(key)
        user = enc.encrypt(user)
        password = enc.encrypt(password)
        encrypted = 1
    
    userInfo = list()
    list.append(userInfo, user)
    list.append(userInfo, password)
    list.append(userInfo, encrypted)
    list.append(userInfo, salt)
    countdown = 5
    for x in range(0, 5):
        
        print("User creation succeded! Returning to login in: " + str(countdown) + " ")
        countdown = countdown - 1
        time.sleep(1)
        cls()
    #Tries to save a new Userfile
    newHandoff = 1
    try:
        pickle.dump(userInfo, open(trueUser, "wb"))
    except IOError:
        print("There was an error handling the new file: Please make sure you have adequate permissions to create a Userfile.")
        raise SystemExit("There was an error handling the new file: Please make sure you have adequete permissions to make a new Userfile.")

#Code for logging in
if user != "New":
    #Requesting information
    if newHandoff == 1:
        print("New-user handoff detected. Use same password.")
        user = enc.decrypt(user)
        user = user.decode('utf-8')
    inputPassword = input("Please input password")

#Attempting to load the Userfile
userFile = pickle.load( open( user, "rb" ) )
if newHandoff != 1:
    userLoaded = userFile[1]
    passwordLoaded = userFile[2]
    fileEncrypted = userFile[3]
    salt = userFile[4]
    if fileEncrypted == 1:
        key = base64.urlsafe_b64encode(kdf.derive(inputPassword))
        userDecrypted = enc.decrypt(userLoaded)
        passwordDecrypted = enc.decrypt(passwordLoaded)

if newHandoff == 1:
    print("end of my work for tonight")
