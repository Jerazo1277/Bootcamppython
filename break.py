n=int(input('Digite un numero: '))
n1=0
n2=0
for i in range(n): #0,1----,1,2,3,5
    if i==0:
        print(i)
    elif i==1:
        print(i)
        n1=1
    else:
        print(n1+n2)
    
    n3=n1
    n1=n2
    n2=n1+n3
        
    
    