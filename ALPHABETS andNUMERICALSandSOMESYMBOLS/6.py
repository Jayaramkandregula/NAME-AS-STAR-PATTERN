#Direct list method
t='* '
N6=[[t,t,t,t,t],[t,'  ','  ','  ','  '],[t,t,t,t,t],[t,'  ','  ','  ',t],[t,t,t,t,t]]
for i in N6:    
    for j in i:
        print(j,end='')
    print()

print()

#using loops
s='* '
for i in range(5):   
    for j in range(5):
        if(i==0 or i==2 or i==4 or j==0 or (i==3 and j==4)):
            print(s,end='')
        else:
            print(" ",end=' ')
    print()

print()

#Using Nested with for loop
w='* '
N6=[['  'for j in range(5)]for i in range(5)]
for i in range (5):
    for j in range(5):
        if(i==0 or i==2 or i==4 or j==0 or (i==3 and j==4)):
           N6[i][j]=w
        print(N6[i][j],end='')
    print()    
