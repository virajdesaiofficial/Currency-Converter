#displaying all the conversion rates where standard currency is USD

def display():
	print("The following are the conversion rates based on USD ")
	f=open('ConversionRates.txt','r') #file in which rates are stored
	f1=f.readlines()
	for x in f1:
		print(x)
