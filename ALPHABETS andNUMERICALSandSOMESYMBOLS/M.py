#Direct list method
t='* '
M=[[t,'  ','  ','  ',t],[t,t,'  ',t,t],[t,'  ',t,'  ',t],[t,'  ','  ','  ',t],[t,'  ','  ','  ',t]]
for i in M:    
    for j in i:
        print(j,end='')
    print()

print()

#using loops
s='* '
for i in range(5):   
    for j in range(5):
        if(j==0 or j==4 or (i==1 and j!=2)or (i==j==2)):
             print(s,end='')
        else:
            print(" ",end=' ')
    print()

print()

#Using Nested with for loop
w='* '
M=[['  'for j in range(5)]for i in range(5)]
for i in range (5):
    for j in range(5):
        if(j==0 or j==4 or (i==1 and j!=2)or (i==j==2)):
           M[i][j]=w
        print(M[i][j],end='')
    print()    
