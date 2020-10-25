a=int(input("enter a no. "))
b=int(input("enter a no. "))
c=int(input("enter a no. "))
if(a>b):
    if(a>c):
        max=a
    else:
         max=c
else:
    if(b>c):
        max=b
    else:
        max=c
print("Max is ",max)        
