#Direct list method
t='* '
R=[[t,t,t,t,'  '],[t,'  ','  ','  ',t],[t,t,t,t,'  '],[t,'  ','  ','  ',t],[t,'  ','  ','  ',t]]
for i in R:    
    for j in i:
        print(j,end='')
    print()

print()

#using loops
s='* '
for i in range(5):   
    for j in range(5):
        if(j==0 or (j==4 and (i!=0 and i!=2))or(j!=4 and (i==0 or i==2))):
             print(s,end='')
        else:
            print(" ",end=' ')
    print()

print()

#Using Nested with for loop
w='* '
R=[['  'for j in range(5)]for i in range(5)]
for i in range (5):
    for j in range(5):
        if(j==0 or (j==4 and (i!=0 and i!=2))or(j!=4 and (i==0 or i==2))):
           R[i][j]=w
        print(R[i][j],end='')
    print()    
