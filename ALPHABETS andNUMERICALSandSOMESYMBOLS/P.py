#Direct list method
t='* '
P=[[t,t,t,t,'  '],[t,'  ','  ','  ',t],[t,t,t,t,'  '],[t,'  ','  ','  ','  '],[t,'  ','  ','  ','  ']]
for i in P:    
    for j in i:
        print(j,end='')
    print()

print()

#using loops
s='* '
for i in range(5):   
    for j in range(5):
        if(j==0 or ((i==0 or i==2)and j!=4)or(j==4 and i==1)):
             print(s,end='')
        else:
            print(" ",end=' ')
    print()

print()

#Using Nested with for loop
w='* '
P=[['  'for j in range(5)]for i in range(5)]
for i in range (5):
    for j in range(5):
        if(j==0 or ((i==0 or i==2)and j!=4)or(j==4 and i==1)):
           P[i][j]=w
        print(P[i][j],end='')
    print()    
