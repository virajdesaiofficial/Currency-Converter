#Main program for the application
#author: Viraj Desai

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
	while True:
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
		if n==1:
			reg.register_user()
		elif n==2:
			login_status=lg.login()
		elif n==3:
			if login_status:
				cc.compare()
			else:
				print("Please login")
		elif n==4:
			if not login_status:
				print("Please login")
			elif pp.pay():
				print("Payment successfull")
			else:
				print("Payment unsuccessfull! Enter valid usernames or amount!")
		elif n==5:
			if login_status:
				rec.receive()
			else:
				print("Please login")
		elif n==6:
			if login_status:
				ct.convert()
			else:
				print("Please login")
		elif n==7:
			if login_status:
				dr.display()
			else:
				print("Please login")
		elif n==8:
			if login_status:
				hf.help()
			else:
				print("Please login")
		elif n==9:
			print("Successfully logged out! Thank you!")
			break
		else:
			print("Enter valid number")
			
			
			
	
