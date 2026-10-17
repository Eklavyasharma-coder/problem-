l = [1,2,3,6]

for item in l:
    print(item)

else:
    print("done")  # this is printed when the loop  exhausts!

#Break


for i in range(100):
    if(i==34):
        break #this mine exit the loop
    print(i)


for i in range(100):
    if(i==34):
        continue # Skip this iteration
print(i)


#pass
l=[222,33,44,55]
for i in l:
    pass 

i=0
while (i<45):
    print(i)
    i += 1