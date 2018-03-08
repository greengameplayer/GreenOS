import time
import pickle
import PyCrypto
from Crypto.Cipher import AES









#Prints out the time
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
    #Tries to save a new Userfile
    try:
        pickle.dump(user, open(user, "wb"))
    except IOError:
        print("There was an error handling the new file: Please make sure you have adequate permissions to create a Userfile.")
        raise SystemExit("There was an error handling the new file: Please make sure you have adequete permissions to make a new Userfile.")

#Code for logging in
if user != "New":
    #Requesting information
    password = input("Please input password")

#Attempting to load the Userfile
passReq = pickle.load( open( user, "rb" ) )
pickle.dump( password, open( "password.p", "wb" ) )
