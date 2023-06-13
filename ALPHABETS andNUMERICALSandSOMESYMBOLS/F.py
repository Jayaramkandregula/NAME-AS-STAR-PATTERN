#Direct list method
t='* '
F=[[t,t,t,t,t],[t,'  ','  ','  ','  '],[t,t,t,t,'  '],[t,'  ','  ','  ','  '],[t,'  ','  ','  ','  ']]
for i in F:    
    for j in i:
        print(j,end='')
    print()

print()

#using loops
s='* '
for i in range(5):   
    for j in range(5):
        if(i==0 or j==0 or(i==2 and j!=4)):
             print(s,end='')
        else:
            print(" ",end=' ')
    print()

print()

#Using Nested with for loop
w='* '
F=[['  'for j in range(5)]for i in range(5)]
for i in range (5):
    for j in range(5):
        if(i==0 or j==0 or(i==2 and j!=4)):
           F[i][j]=w
        print(F[i][j],end='')
    print()    
