#Direct list method
t='* '
N3=[[t,t,t,t,t],['  ','  ','  ','  ',t],[t,t,t,t,t],['  ','  ','  ','  ',t],[t,t,t,t,t]]
for i in N3:    
    for j in i:
        print(j,end='')
    print()

print()

#using loops
s='* '
for i in range(5):   
    for j in range(5):
        if(j==4 or i==0 or i==2 or i==4):
            print(s,end='')
        else:
            print(" ",end=' ')
    print()

print()

#Using Nested with for loop
w='* '
N3=[['  'for j in range(5)]for i in range(5)]
for i in range (5):
    for j in range(5):
        if(j==4 or i==0 or i==2 or i==4):
           N3[i][j]=w
        print(N3[i][j],end='')
    print()    
