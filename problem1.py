#problem 1
n = int(input("Enter the number"))

for i in range(1,11):
    print(f"{n} X {i} = {n*i}")

#problem 2
l={"harry" , "pokemon" , "sohan" , "sahil" , "shian"}

for name in l:
    if(name.startswith("s")):
        print(f"hello {name}")

#problem 3
n=int(input("Enter a number"))

i=1

while(i<11):
    print(f"{n} X {i} = {n*i}")
    i +=1

#problem 4
n=int(input("Enter a number "))
for i in range(2,n):
    if(n%i) == 0:
     print("number is not prime")
     break
else:
    print("number is prime")

#problem 5
n=int(input("Enter a number:"))
i=1
sum=0

while(i<=n):
      sum +=1
      i +=1
       
print(sum)

#problem 6
#5!=1X2X3x4x5 

n= int(input ("Enter the number "))
product=1
for i in range(1,n+1):
    product= product * i
    print(f"the factorical of {n} is {product}")

# Problem 7 
'''
For n=3
  *
 ***
*****

'''
n = int(input("enter the number"))
for i in range(1,n+1):
    print(" " * (n-i),end="")
    print("*" * (2*i-1),end="")
    print("")

# Problem 8
n = int(input("enter the number"))
for i in range(1,n+1):
    print("*" * i,end="")
    print("")

#Problem 9 
'''
*  *  *
*     *    fo n=3 
*  *  *
'''

n = int(input("enter the number"))
for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*n,end="")
    else:
        print("*",end="")
        print(" "*(n-2) ,end="")
        print("*",end="")
    print("")

#problem 10
n = int(input("enter the number"))

for i in range(1,11):
    print(f"{n} X {11-i} = {n*(11-i)}")
