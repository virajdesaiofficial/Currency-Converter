#function: main controller program for the application
#inputs: integer n 
#output: depending on selected function
#author: Viraj Desai
#last edited: 9/10/2018

import getData as gd
import register as reg
import login as lg
import compareCost as cc
import convert as ct
import pay as pp
import receive as rec
import help as hf
import displayRates as dr

#keep track of whether the user has logged in or not
login_status=False

if __name__ == '__main__':
	print("Welcome to currency converter")
	while True:								#The main menu which provides all the functionalities
		print("------------------------------------------------------------------")
		print("Press 1 to register")
		print("Press 2 to Login")
		print("Press 3 to Compare cost")
		print("Press 4 to Pay")
		print("Press 5 to Recieve")
		print("Press 6 to Convert")
		print("Press 7 to Display rates")
		print("Press 8 for Help and FAQs")
		print("Press 9 to logout and exit")
		n=int(input())
		print("------------------------------------------------------------------")
		if n==1:							#registration of new user 
			reg.register_user()
		elif n==2:							#login for user
			if login_status:					#checks whether another or same user is already logged in
				print("User already logged in")
			else:
				login_status=lg.login()
		elif n==3:							#for comparing costs			
			if login_status:					#works only if user is logged in
				cc.compare()
			else:
				print("Please login")
		elif n==4:							#pay
			if not login_status:					#works only if user is logged in
				print("Please login")
			elif pp.pay():
				print("Payment successfull")
			else:
				print("Payment unsuccessfull! Enter valid usernames or amount!")
		elif n==5:							#receive
			if login_status:					#works only if user is logged in
				rec.receive()
			else:
				print("Please login")
		elif n==6:							#Converting amount
			if login_status:					#works only if user is logged in
				ct.convert()	
			else:
				print("Please login")
		elif n==7:							#Display conversion rates
			if login_status:					#works only if user is logged in
				dr.display()
			else:
				print("Please login")
		elif n==8:							#help and FAQs
			if login_status:					#works only if user is logged in
				hf.help()		
			else:
				print("Please login")
		elif n==9:							#log out and exit the program
			print("Successfully logged out! Thank you!")
			break
		else:
			print("Enter valid number")
			
			
			
	
