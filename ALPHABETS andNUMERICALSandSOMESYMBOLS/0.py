#Direct list method
t='* '
N0=[[t,t,t,t,t],[t,'  ','  ','  ',t],[t,'  ','  ','  ',t],[t,'  ','  ','  ',t],[t,t,t,t,t]]
for i in N0:    
    for j in i:
        print(j,end='')
    print()

print()

#using loops
s='* '
for i in range(5):   
    for j in range(5):
        if(i==0 or j==0 or i==4 or j==4):
             print(s,end='')
        else:
            print(" ",end=' ')
    print()

print()

#Using Nested with for loop
w='* '
N0=[['  'for j in range(5)]for i in range(5)]
for i in range (5):
    for j in range(5):
        if(i==0 or j==0 or i==4 or j==4):
           N0[i][j]=w
        print(N0[i][j],end='')
    print()    
