#Direct list method
t='* '
H=[[t,'  ','  ','  ',t],[t,'  ','  ','  ',t],[t,t,t,t,t],[t,'  ','  ','  ',t],[t,'  ','  ','  ',t]]
for i in H:    
    for j in i:
        print(j,end='')
    print()

print()

#using loops
s='* '
for i in range(5):   
    for j in range(5):
        if(i==2 or j==0 or j==4):
             print(s,end='')
        else:
            print(" ",end=' ')
    print()

print()

#Using Nested with for loop
w='* '
H=[['  'for j in range(5)]for i in range(5)]
for i in range (5):
    for j in range(5):
        if(i==2 or j==0 or j==4):
           H[i][j]=w
        print(H[i][j],end='')
    print()    
