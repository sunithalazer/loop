# # strong number,.....
sum=0
n=int(input())
b=n
while n:
    i=1
    fact=1
    re=n%10
    while i<=re:
        fact=fact*i
        i+=1
    n=n//10
    sum=sum+fact
if sum==b:
    print("strong number")
else:
    print("not a strong number")

