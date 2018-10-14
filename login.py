#login function to get access to other functions of the application
import getData as gd
import loginValidate as lgv

def login():
	uname,password=gd.getData(2)
	flag=lgv.loginValidate(uname,password)		#validation of user
	if flag==True:
		print("Successfully logged in")
		return True
	else:
		print("Invalid credentials")
		return False
	

