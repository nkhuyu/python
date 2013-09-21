Fib={}
#find the max index such that Fib[n]<4,000,000
Fib[0]=1
Fib[1]=2
i=2
val=1
while(val==1):
    Fib[i]=Fib[i-1]+Fib[i-2]
    if(Fib[i]>=4000000):
        break
    i=i+1
#print i-1

sum=0
for j in range(0,i):
    if(j%3==1):
        sum=sum+Fib[j]
print sum    