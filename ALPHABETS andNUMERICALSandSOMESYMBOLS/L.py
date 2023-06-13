#Direct list method
t='* '
L=[[t,'  ','  ','  ','  '],[t,'  ','  ','  ','  '],[t,'  ','  ','  ','  '],[t,'  ','  ','  ','  '],[t,t,t,t,t]]
for i in L:    
    for j in i:
        print(j,end='')
    print()

print()

#using loops
s='* '
for i in range(5):   
    for j in range(5):
        if(j==0 or i==4):
             print(s,end='')
        else:
            print(" ",end=' ')
    print()

print()

#Using Nested with for loop
w='* '
L=[['  'for j in range(5)]for i in range(5)]
for i in range (5):
    for j in range(5):
        if(j==0 or i==4):
           L[i][j]=w
        print(L[i][j],end='')
    print()    
