n=int(input('Digite un numero: '))# 3
n1=0
n2=0
for i in range(n): #0,1----,1,2,3,5# n=3  ---i=0, i=1, i=2
    if i==0:
        print(i) ### 0
    elif i==1:
        print(i)
        n1=1
    else:
        print(n1+n2)# ///1
    
    n3=n1   ### n3= 0//// n3=1
    n1=n2 ###n1=0/////n1= 0
    n2=n1+n3## n2=0/////n2=1
    
    # 0,1,1
        
    
    