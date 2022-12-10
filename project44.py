start= int(input("Enter the starting range:"))
end=int(input("Enter the ending range: "))
print("Range is",(start, end))
print("Then the status of each number in the range is:")
count_prime=[]
count_comp=[]
for i in range(start,end+1):
    f=0
    for j in range(2,i):
        if (i%j==0):
            f=1
            print(i,"is composite")
            count_comp.append(i)            
            break
    if (f==0):
        print(i,"is prime")
        count_prime.append(i)
print("Count:",len(count_prime),"prime and",len(count_comp),"composite numbers in the range")
# made by 
# probodh sahoo,tejasva aghrahari,kanak sharma
# roll no:-444,45,43
# registration no:-12220565,12221307,12219836
    