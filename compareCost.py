import getRate as gr

#Compare the cost of an item between currencies of two different countries.
def compare():
	c1=input("Enter home country ")
	c2=input("Enter target country ")
	rate=gr.getRate(c1,c2) #get the conversion rate between countries c1 and c2
	amount=int(input("Enter amount in home country "))
	#display both the costs
	print(c1 + " " +str(amount))
	print(c2 + " " +str(amount*rate))

