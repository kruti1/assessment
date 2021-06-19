n=int(input("Number of the employees: "))
print()
l=['Fitbit plus','IPods','MI Band','Cult Pass','Macbook Pro','Digital Camera','Alexa','Sandwich Toaster','Microwave Oven','Scale']
m=[7980,22349,999,2799,229900,11101,9999,2195,9800,4999]
k=sorted(m)
print("Here the goodies that are selected for distribution are:")
k=[999,2195,2799,4999,7980,9800,9999,11101,22349,229900]
min1=k[:n]
for i in range(1,len(l)-n):
    min2=k[i:i+n]
    s1 = min1[-1]-min1[0]
    s2 = min2[-1]-min2[0]
    if s1>s2:
        temp=min1
        min1=min2
        min2=temp
for i in min1:
    g=m.index(i)
    print("{}: {}".format(l[g],m[g]))
res=min1[-1]-min1[0]
print("\nAnd the difference between the chosen goodie with highest price and the lowest price is {}".format(res))
