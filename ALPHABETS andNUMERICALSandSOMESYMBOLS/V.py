#Direct list method
t='* '
V=[[t,'  ','  ','  ',t],[t,'  ','  ','  ',t],[t,'  ','  ','  ',t],['  ',t,'  ',t,'  '],['  ','  ',t,'  ','  ']]
for i in V:    
    for j in i:
        print(j,end='')
    print()

print()

#using loops
s='* '
for i in range(5):   
    for j in range(5):
        if(((j==0 or j==4)and(i!=4 and i!=3))or(i==3 and (j==1 or j==3))or(i==4 and j==2)):
             print(s,end='')
        else:
            print(" ",end=' ')
    print()

print()

#Using Nested with for loop
w='* '
V=[['  'for j in range(5)]for i in range(5)]
for i in range (5):
    for j in range(5):
        if(((j==0 or j==4)and(i!=4 and i!=3))or(i==3 and (j==1 or j==3))or(i==4 and j==2)):
           V[i][j]=w
        print(V[i][j],end='')
    print()    
