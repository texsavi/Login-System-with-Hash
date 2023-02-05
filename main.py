from replit import db
import random, os, time


def add():
  time.sleep(.5)
  os.system("clear")
  user=input("Username> ")
  passw=input("Password> ")
  keys=db.keys()
  if user in keys:
    print("User Exists! ")
    return
  salt=random.randint(1000,10000)
  newPassw=f"{passw}{salt}"
  newPassw=hash(newPassw)
  db[user] = {"passw":newPassw,"salt":salt}
  print("Updated...")


def log():
  user=input("Username> ")
  passw=input("Password> ")
  keys=db.keys()
  if user not in keys:
    print("User not found!")
    return
  salt=db[user]["salt"]
  newPassw=f"{passw}{salt}"
  newPassw=hash(newPassw)
  if db[user]["passw"]==newPassw:
    print("Welcome in mon ami!")
  else:
    print("Nopsie! Forgot something?")
 
while True:
  menu=input("1. Add User\n2. Login\n>>")
  if menu=="1":
    add()
  else:
    log()
    
    
             