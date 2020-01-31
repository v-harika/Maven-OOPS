x=0
i=31
sum=0
while(x):
    sum=sum+((1<<i)*(x&1))
    i-=1
    x=x>>1
print(sum)
