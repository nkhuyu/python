def mutliplesof3and5(n):
    if(n%3==0 or n%5==0):
        return 1
    else:
        return 0

              
def sum(n):
    temp=0
    for i in range(3,n):# 3:n-1
        if(mutliplesof3and5(i)):
            temp=temp+i
    return temp  
## 
n=5   
sum(n)   