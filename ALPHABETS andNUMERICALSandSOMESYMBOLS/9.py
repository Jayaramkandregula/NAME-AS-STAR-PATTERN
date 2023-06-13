#Direct list method
t='* '
N9=[[t,t,t,t,t],[t,'  ','  ','  ',t],[t,t,t,t,t],['  ','  ','  ','  ',t],[t,t,t,t,t]]
for i in N9:    
    for j in i:
        print(j,end='')
    print()

print()

#using loops
s='* '
for i in range(5):   
    for j in range(5):
        if(i==0 or i==2 or i==4 or (j==0 and i==1) or j==4):
            print(s,end='')
        else:
            print(" ",end=' ')
    print()

print()

#Using Nested with for loop
w='* '
N9=[['  'for j in range(5)]for i in range(5)]
for i in range (5):
    for j in range(5):
        if(i==0 or i==2 or i==4 or (j==0 and i==1) or j==4):
           N9[i][j]=w
        print(N9[i][j],end='')
    print()    
