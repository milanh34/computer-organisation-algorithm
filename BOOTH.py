#Functon to return binary string of a number
def conversion(a):
    curr_len = len(a)
    if curr_len < count+1:
        q = "0"*(count+1 - curr_len) + a
    else:
        q = a
    return q

#Function to add binary numbers in string
def add(x,y):
    max_len = max(len(x),len(y))
    result = ''
    carry = 0
    for i in range(max_len-1, -1, -1):
           r = carry
           if x[i] == '1':
               r += 1
           if y[i] == '1':
               r += 1 
           if r % 2 == 1:
               result = "1" + result 
           else: 
               result = "0" + result
           if r<2:
               carry =0
           else:
               carry= 1  
    return result

#Function to find 2's complement
def twoc(a):
    l = list(a)
    for i in range(len(l)):
         if l[i] == "1" :
             l[i] = "0"
         else: l[i] ="1"
    b = "0"*(len(l)-1) + "1" 
    return add("".join(l),b)

#Function to do right shift
def right_shift(ac,q,q1): 
    a = ac[0]
    for i in range(1,len(ac)):
        a+=ac[i-1]
    b = ac[-1]
    for j in range(1,len(q)):
        b+=q[j-1]
    c = q[-1]
    return a,b,c

#Inputs
x = bin(int(input("Enter multiplicand : "))) #Q
y = bin(int(input("Enter multiplier : "))) #M 
a = x.replace("0b", "")
b = y.replace("0b", "")
negative_a=0
negative_b=0
if (a[0]=="-"):
        a = a.replace("-","")
        negative_a =1
if (b[0]=="-"):
        b = b.replace("-","")
        negative_b =1
        
#No. of bits
count=max(len(str(a)),len(str(b)))
count1 = count

#Assign
firstP = conversion(a) #positive multiplicand 
secondP = conversion(b) #positive multiplier
firstN = twoc(firstP) #2's complement of multiplicand
secondN = twoc(secondP) #2's complement of multiplier

#Assigning Signed Variable
if negative_a ==0:
    M = firstP
    M2 = firstN
else:
    M = firstN
    M2 = firstP
if negative_b ==0:
    Q = secondP
else:
    Q = secondN

#Initialising few values
AC = conversion("0")
Q1 = "0"

#Booth's Algorithm
print("\nBooth's Algorithm")
print("Cycle \t\tAC \t\tQ \t\tQ0 \t\tOperation \n")
print(f"{str(count)} \t\t{AC} \t\t{Q} \t\t{Q1} \t\tInitial ")
print("\n")

#Loop 
while (count>=0):
    compare = Q[-1] + Q1
    if compare[0]==compare[-1]:
        AC, Q, Q1 =right_shift(AC,Q,Q1)
        Op = "right shift" 
    elif compare =="10":
        AC = add(AC,M2)
        AC, Q, Q1 =right_shift(AC,Q,Q1)
        Op = "AC=AC-M and right shift"
    elif compare == "01":
        AC = add(AC,M)
        AC, Q, Q1 =right_shift(AC,Q,Q1)
        Op = "AC=AC+M and right shift"
    
    print(f"{str(count)} \t\t{AC} \t\t{Q} \t\t{Q1} \t\t{Op} ")
    print("\n")
    count = count-1

#Answer   
answer = AC+Q
if negative_a==negative_b:
    ans_d = str(int(answer,2))
else:
    ans_d = "-" + str(int(twoc(answer),2))

print("The product in binary is:" + answer)
print("Decimal conversion:" + ans_d)