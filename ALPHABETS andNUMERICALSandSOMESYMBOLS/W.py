#Direct list method
t='* '
W=[[t,'  ','  ','  ',t],[t,'  ','  ','  ',t],[t,'  ',t,'  ',t],[t,t,'  ',t,t],[t,'  ','  ','  ',t]]
for i in W:    
    for j in i:
        print(j,end='')
    print()

print()

#using loops
s='* '
for i in range(5):   
    for j in range(5):
        if(j==0 or j==4 or ((i==j or i+j==4)and(i!=1))):
             print(s,end='')
        else:
            print(" ",end=' ')
    print()

print()

#Using Nested with for loop
w='* '
W=[['  'for j in range(5)]for i in range(5)]
for i in range (5):
    for j in range(5):
        if(j==0 or j==4 or ((i==j or i+j==4)and(i!=1))):
           W[i][j]=w
        print(W[i][j],end='')
    print()    
