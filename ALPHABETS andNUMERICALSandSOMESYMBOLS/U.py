#Direct list method
t='* '
U=[[t,'  ','  ','  ',t],[t,'  ','  ','  ',t],[t,'  ','  ','  ',t],[t,'  ','  ','  ',t],['  ',t,t,t,'  ']]
for i in U:    
    for j in i:
        print(j,end='')
    print()

print()

#using loops
s='* '
for i in range(5):   
    for j in range(5):
        if(((j==0 or j==4)and(i!=4))or(i==4 and (j!=0 and j!=4))):
             print(s,end='')
        else:
            print(" ",end=' ')
    print()

print()

#Using Nested with for loop
w='* '
U=[['  'for j in range(5)]for i in range(5)]
for i in range (5):
    for j in range(5):
        if(((j==0 or j==4)and(i!=4))or(i==4 and (j!=0 and j!=4))):
           U[i][j]=w
        print(U[i][j],end='')
    print()    
