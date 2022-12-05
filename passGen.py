# LPU Python Project
# Create a Password Generator
# Created by Sanjai 
# Reg no. 12205378
# Section & Roll no. K22HN 12
# Started On 20/11/2022 
# Completed On 29/11/2022

import string
import random
import datetime
def main():

	#style
	reset = '\033[0m'
	bold = '\033[01m'
	invisible = '\033[08m'

	#fg
	red = '\033[31m'
	green = '\033[32m'
	orange = '\033[33m'
	blue = '\033[34m'
	purple = '\033[35m'
	lightblue = '\033[94m'

	#bg
	bg_red = '\033[41m'
	#Printing The Banner
	
	print(red,"*"*33,"\n","*"," "*31,"*",sep='')
	print("*",lightblue,bold,"\tPassword Generator\t",reset,red,"*",sep='')
	print("*"," "*31,"*","\n","*"*33,sep='')

	#Main Program
	
	repeat = 'y'
	while(repeat == 'y'):
		print(orange,"\nHow many passwords you want to generate ?: ",reset,sep='',end='')
		totPass = int(input() or 1)
		pwLengths = []
		for i in range(totPass):
			print(orange,f"Enter Length of password {i+1} :\t",reset,sep='',end='')
			pwLen = int(input() or 12)
			if pwLen < 12:
				print(bg_red,invisible,"Error! Password Length must be more than 11\n",reset,sep='')
				continue
			pwLengths.append(pwLen)
		print()
		passWordList = []
		for i in range(len(pwLengths)):
			password = genRandomPass(pwLengths[i])
			print(purple,f"Password #{i+1} : ",bold,blue,password,sep='') 
			passWordList.append(password)
		print(reset,bold,end='',sep='')
		savePass = input("Want to save Passwords in a file ?[y/n]:\t")
		if savePass == 'y':
			with open('password.txt','w+') as f:
				timeNow  = datetime.datetime.now()
				timeNow = timeNow.strftime("%d-%m-%Y %H:%M:%S")
				f.write("Passwords that Created on %s\n\n"%timeNow)
				for passWord in passWordList:
					f.write("Password: %s\n"%passWord) 
				print("Passwords Saved Successfully!")
			f.close()
		print(reset,green,"Want to restart the program ?[y/n]:\t",sep='',end='')
		repeat = input() or 'n'
			
def genRandomPass(passLen):

	alphaLower = string.ascii_lowercase
	alphaUpper = string.ascii_uppercase
	digits = string.digits
	symbols = "!@#$%^&*?_-"
	avg = passLen//4 + 4
	
	randomAlphaLower = random.choices(alphaLower,k=avg)
	randomAlphaUpper = random.choices(alphaUpper,k=avg)
	randomDigits     = random.choices(digits,    k=avg)
	randomSymbols    = random.choices(symbols,   k=avg)
	
	randomComb = randomAlphaLower + randomAlphaUpper + randomDigits + randomSymbols

	random.shuffle(randomComb)
	randomComb = randomComb[:passLen]
	return ''.join(randomComb)

main()
