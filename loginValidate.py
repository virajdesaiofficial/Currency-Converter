#functions to verify the authentication of the user trying to log in

def loginValidate(entered_uname,entered_password):
	logged_in=False
	with open('UserData.txt','r') as file:        
		for line in file:		
			uname,password,name,email,contact,amount=line.strip().split(" ")
			if uname == entered_uname:						#searches for uname in file
				logged_in = (password==entered_password)			#is uname is found then it checks whether the password matches or not
				break
		return True
