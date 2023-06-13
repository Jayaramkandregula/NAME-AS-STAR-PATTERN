#Direct list method
t='* '
K=[[t,'  ','  ',t,t],[t,'  ',t,'  ','  '],[t,t,'  ','  ','  '],[t,'  ',t,'  ','  '],[t,'  ','  ',t,t]]
for i in K:    
    for j in i:
        print(j,end='')
    print()

print()

#using loops
s='* '
for i in range(5):   
    for j in range(5):
        if(j==0 or ((i==0 or i==4)and(j==3 or j==4))or i+j==3 or (i==3 and j==2)):
             print(s,end='')
        else:
            print(" ",end=' ')
    print()

print()

#Using Nested with for loop
w='* '
K=[['  'for j in range(5)]for i in range(5)]
for i in range (5):
    for j in range(5):
        if(j==0 or ((i==0 or i==4)and(j==3 or j==4))or i+j==3 or (i==3 and j==2)):
           K[i][j]=w
        print(K[i][j],end='')
    print()    
