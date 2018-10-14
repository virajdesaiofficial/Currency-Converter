#displays all queries asked till date and asks user whether he/she would like to add another query

def help():
	print("Please search for your query here! ")
	f=open('Help&FAQs.txt','r')
	f1=f.readlines()		
	for x in f1:							#displays the Help&FAQs.txt file
		print(x)
	f.close()
	l=int(input("If you want to ask new query press 1 "))
	if l==1:					
		query=input("Enter your query ")
		f=open('Help&FAQs.txt','a+')				#appends the new query to the file
		f.write(query+"\n")
		print("Query asked successfully!Please wait for the response ")
	
