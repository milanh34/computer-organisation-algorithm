#CONVERTS DECIMAL TO BINARY
def bin_convert(a):
	bits=[]
	while(a>0):
		num=a
		b=int(num%2)
		bits.append(b)
		a=a//2
	bits.reverse()
	return bits

#LEFT SHIFT OPERATION
def left_shift(A,Q):
	val=A+Q
	l=len(val)
	for i in range(0,l-1):
		val[i]=0
		val[i]=val[i+1]
	del val[i]
	return val

#TAKES 2's COMPLIMENT
def twoc(value):
	one_comp=[]
	two_comp=[]

	for i in range(0,len(value)):
		if value[i]==0:
			one_comp.append(1)
		elif value[i]==1:
			one_comp.append(0)
	
	carry=1
	for j in range(len(value)-1,-1,-1):
		if(one_comp[j]==0 and carry==1):
			two_comp.append(1)
			carry=0
		elif(one_comp[j]==1 and carry==1):
			two_comp.append(0)
			carry=1
		elif(one_comp[j]==0 and carry==0):
			two_comp.append(0)
			carry=0
		elif(one_comp[j]==1 and carry==0):
			two_comp.append(1)
			carry=0
	two_comp.reverse()
	return two_comp

#ADDING TWO BINARY NOS.
def addition(A,M):
	add=[]
	ad=A
	carry = 0
	for i in range(len(ad)-1,-1,-1):
		if(A[i]==0 and M[i]==0 and carry==0):
			add.append(0)
			carry=0
		elif(A[i]==0 and M[i]==0 and carry==1):
			add.append(1)
			carry=0
		elif(A[i]==0 and M[i]==1 and carry==0):
			add.append(1)
			carry=0
		elif(A[i]==0 and M[i]==1 and carry==1):
			add.append(0)
			carry=1
		elif(A[i]==1 and M[i]==0 and carry==0):
			add.append(1)
			carry=0
		elif(A[i]==1 and M[i]==0 and carry==1):
			add.append(0)
			carry=1
		elif(A[i]==1 and M[i]==1 and carry==0):
			add.append(0)
			carry=1
		elif(A[i]==1 and M[i]==1 and carry==1):
			add.append(1)
			carry=1
	add.reverse()
	return add

#CONVERTS BINARY TO DECIMAL
def dec_convert(a):
	a.reverse()
	dec=0
	for i in range(0,len(a)):
		if(a[i]==1):
			dec=dec+(a[i]*(2**i))
		elif(a[i]==0):
			pass
	return dec

#CODE EXECUTES FROM HERE
print("DIVISION RESTORING ALGORITHM\n")
dividend=int(input("Enter value of Dividend -> Q: "))
divisor=int(input("Enter value of Divisor -> M: "))
print("")

#CONVERTING TO BINARY
q=bin_convert(dividend)
m=bin_convert(divisor)

#SETTING THE M VALUE
if len(m)<len(q):
	diff=len(q)-len(m)
	for i in range(0,diff+1):
		m.insert(0,0)
elif len(m)==len(q):
	m.insert(0,0)

#ASSIGNING VALUE OF A to 0
ACC = []
for i in range(0,len(m)):
	ACC.append(0)

#VALUE OF -M
negM = twoc(m)

print("Q: ",*q)
print("M: ",*m)
print("A: ",*ACC)
print("-M: ",*negM,"\n")
print("RESTORING DIVISON ALGORITHM TABLE\n")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("|\tCycles\t|\t    A    \t\t|\t    Q    \t\t|\t\t   Action\t\t\t|")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")
counter = len(q)
while counter>0:

	#INITIAL ITERATION
	if(counter == len(q)):
		print("|\t",counter,"\t|\t",*ACC,"\t|\t",*q,"    \t|\t\tInitial\t\t\t|")
		print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")

	#LEFT SHIFT A, Q
	a = left_shift(ACC,q)

	#TAKING THE "A" AND "Q" PART FROM "a"
	newA=a[0:len(ACC)]
	newQ=a[len(ACC):]
	print("|\t","","\t|\t",*newA,"\t|\t",*newQ,"_\t\t|\t\tLeft Shift A, Q\t\t|")
	print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")

	#A<-A-M
	sumAM = addition(newA,negM)
	print("|\t","","\t|\t",*sumAM,"\t|\t",*newQ,"_\t\t|\t\tA <-- A - M\t\t|")
	print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")

	if(sumAM[0]==1):  #IF MSB(A) = 1 means A<0
		newQ.insert(len(newQ)+1,0)
		sumAM=addition(sumAM,m)
		op = "A <-- A + M   &   Q0 <-- 0"
	elif(sumAM[0]==0):  #IF MSB(A) = 0 means A>0
		newQ.insert(len(newQ)+1,1)
		op = "        Q0 <-- 1         "

	ACC=sumAM
	q=newQ

	print("|\t",counter-1,"\t|\t",*ACC,"\t|\t",*q,"    \t|\t",op,"\t\t|")
	print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")
	counter=counter-1

print("\nQuotient: ",*q,"  ->  ",dec_convert(q))
print("Remainder: ",*ACC,"  ->  ",dec_convert(ACC))
