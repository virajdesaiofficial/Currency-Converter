#paying an amount to another user

def pay():
	uname_sender=input("Please enter your username ")
	uname_receiver=input("Please enter receiver's username ")
	pay_amount=int(input("Enter amount to be sent! "))
	flag=0
	f=open('Backup.txt','w')		#Backup file 
	with open('UserData.txt','r') as file:	
		for line in file:
			uname,password,name,email,contact,amount=line.strip().split(" ")
			new_amount=int(amount)
			if uname==uname_sender:
				flag+=1
				new_amount-=pay_amount		#pay_amount is deducted from sender's account
			if uname==uname_receiver:
				flag+=1	
				new_amount+=pay_amount		#pay_amount is added to the receiver's account
			f.write(uname+" "+password+" "+name+" "+email+" "+contact+" "+str(new_amount)+"\n")	#new details are stored in Backup file
			if flag==2:
				break
	if flag!=2:
		return False		
	file.close()	#closing UserData file	
	f.close()	#closing Backup file
	f=open('Backup.txt','r')		
	f1=f.readlines()
	f2=open('UserData.txt','w')
	for line in f1:				#copying updated Backup file to the UserData file 
		uname,password,name,email,contact,amount=line.strip().split(" ")
		f2.write(uname+" "+password+" "+name+" "+email+" "+contact+" "+amount+"\n")
	return True	
		
