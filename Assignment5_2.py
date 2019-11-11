i=0

def display(num):
	global i
	if(i<num):
		print(i+1,end=" ")
		i=i+1
		display(num)

def main():
	num=int(input("Enter the number : "))
	display(num)

if (__name__=="__main__"):
	main()