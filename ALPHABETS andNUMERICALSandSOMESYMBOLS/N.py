#Direct list method
t='* '
N=[[t,'  ','  ','  ',t],[t,t,'  ','  ',t],[t,'  ',t,'  ',t],[t,'  ','  ',t,t],[t,'  ','  ','  ',t]]
for i in N:    
    for j in i:
        print(j,end='')
    print()

print()

#using loops
s='* '
for i in range(5):   
    for j in range(5):
        if(j==0 or j==4 or i==j):
             print(s,end='')
        else:
            print(" ",end=' ')
    print()

print()

#Using Nested with for loop
w='* '
N=[['  'for j in range(5)]for i in range(5)]
for i in range (5):
    for j in range(5):
        if(j==0 or j==4 or i==j):
           N[i][j]=w
        print(N[i][j],end='')
    print()    
