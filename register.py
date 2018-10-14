#this function registers a new user with the system

import getData as gd

def register_user():
	uname,password,name,email,contact=gd.getData(1)
	amount=int(input("Enter amount to be deposited "))
	f=open('UserData.txt','a+') 
	f1=open('Backup.txt','a+')
	f.write(uname+" "+password+" "+name+" "+email+" "+contact+" "+str(amount)+"\n")		#save details in UserData.txt file
	f1.write(uname+" "+password+" "+name+" "+email+" "+contact+" "+str(amount)+"\n")	#create a Backup file concurrently
	f.close()
	f1.close()
	print("Successfully registered ")
	return True

