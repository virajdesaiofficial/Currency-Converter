#returns the conversion rate of country c2 wrt country c1

def getRate(c1,c2):
	r1,r2,flag=0,0,0
	f=open('ConversionRates.txt','r')
	f1=f.readlines()
	for line in f1:
		c,r=line.strip().split(" ")
		if c==c1:
			flag+=1
			r1=float(r)	#rate between c1 and USD
		if c==c2:
			flag+=1
			r2=float(r)	#rate between c2 and USD
		if flag==2:
			break
	return round(r1/r2,2)     #since base currency is fixed we need to use this to get direct conversion rate
	
