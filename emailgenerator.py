#EMAIL GENERATOR V1.0 BY fsuxcks
#PLEASE DONT USE THIS CODE AS YOUR OWN
#IF YOU WANT TO CHANGE SOMETHING YOUR GOOD TO GO

import requests
from bs4 import BeautifulSoup
import time
import os

def logo():
	os.system("title EMAIL GENERATOR V1.0")
	os.system("color a")
	print("*"*60)
	print("               EMAIL GENERATOR V1.0 BY FSUXCKS")
	print("*"*60)
	time.sleep(0.4)

emails = 0
email = []
link = 'https://generator.email/'

def getamount():
	try:
		logo()
		amount = int(input("[*] Enter amount of emails: "))
		if amount > 100 or amount < 1:
			print("[!] Error code 2. Number of email must be more than 1 and less than 100.")
			time.sleep(2.3)
			os.system("cls")
			return getamount()
		return amount
	except ValueError:
		print("[!] Eror code 1. Please enter a number.")
		time.sleep(1.4)
		os.system("cls")
		return getamount()

amount = getamount()


os.system("cls")
print("*"*50)
print("[#] Please wait...")
try:
	r = requests.get(link)
except:
	os.system("cls")
	os.system("color 4")
	print("[!] Error code 6. Please check your internet connection")
	input()
	exit()
	
if r.status_code != 200:
	os.system("cls")
	os.system("color 4")
	print("[!] Error code 200. Please check your internet connection")
	input()
	exit()
if r.status_code == 404:
	os.system("cls")
	os.system("color 4")
	print("[!] Error code 404. Site not found or changed. Please download the lastest version from GitHub.")
	input()
	exit()

code = r.text

print('[#] Succesfuly loaded generator.')
print('[#] Parsing email(-s)...')
print("*"*50)

soup = BeautifulSoup(code, "lxml")
if soup.find("div", class_="e7m container to1").find(class_="e7m row").find("b") == None:
	os.system("cls")
	os.system("color 4")
	print("[!] Error code 4. Object not found. Try to install newest version.")
	input()
	exit()

while emails != amount:
	soup = BeautifulSoup(code, "lxml")
	email.append(soup.find("div", class_="e7m container to1").find(class_="e7m row").find("b").text)
	print("[#] Email " + str(emails+1) + "/" + str(amount) + " is done")
	emails = emails + 1
	r.close
	r = requests.get(link)
	code = r.text

print("*"*50)
time.sleep(0.5)


number = 1
os.system("cls")
print("*"*50)
for name in email:
	print(name)
	number = number + 1
print("*"*50)
time.sleep(1.7)

print("")
print("[?] Use CTRL+ALT+C to copy")
print("[?] Press ENTER to quit...")
input()

