#EMAIL GENERATOR V2.3 BY fsuxcks
#PLEASE DONT USE THIS CODE AS YOUR OWN
#IF YOU WANT TO CHANGE SOMETHING YOUR GOOD TO GO

try:
	import requests
	from bs4 import BeautifulSoup
	from threading import Thread
	from progress.bar import IncrementalBar

except:
	print("Some dependencies are not installed. Check README.md for instalations instructions")
	input()
	exit()

import platform
import time
import os

if platform.system() == "Windows":
	os.system("title EMAIL GENERATOR V2.3")
	os.system("color a")

def clearing():
	if platform.system() == "Windows":
		os.system("cls")
	elif platform.system() == "Linux":
		os.system("clear")

def logo():
	print("*"*56)
	print("               EMAIL GENERATOR V2.3 BY FSUXCKS")
	print("*"*56)
	time.sleep(0.4)

emails = 0
email = []
link = 'https://generator.email/'
threads = 1
potok = 0

clearing()
logo()

def getamount():
	try:
		amount = int(input("[*] Enter amount of emails: "))
		if amount > 500 or amount < 1:
			print("[!] Error code 2. Number of emails must be more than 1 and less than 500.")
			time.sleep(2.6)
			clearing()
			logo()
			return getamount()
		return amount
	except ValueError:
		print("[!] Error code 1. Please enter a number.")
		time.sleep(2.3)
		clearing()
		logo()
		return getamount()

def getthreads(amount):
	try:
		threads = int(input("[*] Enter amount of threads [MAX 8]: "))
		if threads > 8 or threads < 1:
			print("[!] Error code 8. Number of threads must be more than 1 and less than 8.")
			time.sleep(2.7)
			clearing()
			logo()
			print("[*] Enter amount of emails: " + str(amount))
			return getthreads(amount)
		if threads > amount:
			print("[!] Threads cant be more than amount of emails.")
			time.sleep(1.8)
			clearing()
			logo()
			print("[*] Enter amount of emails: " + str(amount))
			return getthreads(amount)
		return threads
	except ValueError:
		print("[!] Eror code 1. Please enter a number.")
		time.sleep(1.4)
		clearing()
		logo()
		print("[*] Enter amount of emails: " + str(amount))
		return getthreads(amount)

amount = getamount()
threads = getthreads(amount)
info = amount
amount = amount//threads

clearing()
print("*"*50)
print("[#] Please wait...")

try:
	r = requests.get(link)
except:
	clearing()
	os.system("color 4")
	print("[!] Error code 6. Please check your internet connection")
	input()
	exit()
	
if r.status_code != 200:
	clearing()
	os.system("color 4")
	print("[!] Error code 200. Please check your internet connection")
	input()
	exit()

if r.status_code == 404:
	clearing()
	os.system("color 4")
	print("[!] Error code 404. Site not found or changed. Please download the lastest version from GitHub.")
	input()
	exit()

code = r.text

print('[#] Succesfuly loaded generator.')
print('[#] Threads: ' + str(threads))
bar = IncrementalBar('Generating emails', max=info, suffix="Done: %(percent)d%%  Remaining time: %(eta)ds")
print("*"*50)
print("")

soup = BeautifulSoup(code, "html.parser")

if soup.find("div", class_="e7m container to1").find(class_="e7m row").find("b") == None:
	clearing()
	os.system("color 4")
	print("[!] Error code 4. Object not found. Try to install newest version.")
	input()
	exit()

def donetxt():
	clearing()
	print("*"*50)
	for name in email:
		print(name)
	print("*"*50)

	file = open("result.txt", "w")

	for i in range(len(email)):
		file.write(email[i] + "\n")
	file.close()

	time.sleep(0.4)
	print("")
	print("[?] Result.txt was created")
	print("[?] Press ENTER to quit...")
	input()


def work(code, emails, amount, email, r, bar):
	while emails != amount:
		soup = BeautifulSoup(code, "html.parser")
		email.append(soup.find("div", class_="e7m container to1").find(class_="e7m row").find("b").text)
		bar.next()
		emails  = emails + 1
		r.close
		try:
			r = requests.get(link)
		except:
			bar.finish()
			clearing()
			os.system("color 4")
			print("[!] Error code 9. Server blocked your requests. Try to use less emails and threads.")
			input()
			exit()
		code = r.text


while potok != threads-1:
	th = Thread(target=work, args=(code, emails, amount, email, r, bar))
	th.start()
	potok = potok + 1

work(code=code, emails=emails, amount=amount, email=email, r=r, bar=bar)

for i in range(threads):
	try:
			r = requests.get(link)
	except:
		clearing()
		os.system("color 4")
		bar.finish()
		print("[!] Error code 9. Server blocked your requests. Try to use less emails and threads.")
		input()
		exit()
	soup = BeautifulSoup(code, "html.parser")
	code = r.text
	email[i-1] = soup.find("div", class_="e7m container to1").find(class_="e7m row").find("b").text

time.sleep(0.5)
if threads > 1:
	if th.is_alive() == False:
		donetxt()
		bar.finish()
else:
	donetxt()
	bar.finish()




