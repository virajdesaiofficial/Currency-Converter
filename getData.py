#Getting input from user while registering and logging in the system

def getData(c):
	uname=input("Enter user name ")
	if c==1:					#for registering new user
		password=input("Set password ")
		while True:
			if len(password)<6:
				password=input("Enter password longer than 6 characters ")
			else:
				break
		name=input("Enter your name ")
		email=input("Enter your email ")
		contact=input("Enter your contact number ")
		return uname,password,name,email,contact
	else:						#for login
		password=input("Enter your password ")
		return uname,password
		 
