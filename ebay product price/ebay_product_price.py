print("Enter Prices Of Product Seperated By spaces")
n=list(map(int,input().split())) 
print("Enter distance Of Product Seperated By spaces")
m=list(map(int,input().split()))
print("Enter availability Of Product Seperated By spaces")
k=list(map(int,input().split()))
print("Final Price to be Paid Indiviually seperated by spaces")
avail=dict(zip(k,n))
price=dict(zip(n,m))
check=[]
checkprice=[]
final=[]
for a in k:
    if a>0:
        check.append(a)
for a in range(len(check)):
    for n in avail:
        if check[a]==n:
            checkprice.append(avail[n])
for a in range(len(checkprice)):
    for n in price:
        if checkprice[a]==n:
            final.append(price[n])
for a in range(len(final)):
    p=final[a]*checkprice[a]
    print(p,end=' ')
