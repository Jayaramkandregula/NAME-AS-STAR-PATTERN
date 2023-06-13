#Direct list method
t='* '
N2=[[t,t,t,t,t],['  ','  ','  ','  ',t],[t,t,t,t,t],[t,'  ','  ','  ','  '],[t,t,t,t,t]]
for i in N2:    
    for j in i:
        print(j,end='')
    print()

print()

#using loops
s='* '
for i in range(5):   
    for j in range(5):
        if(i==4 or i==2 or i==0 or (i==1 and j==4)or(i==3 and j==0)):
            print(s,end='')
        else:
            print(" ",end=' ')
    print()

print()

#Using Nested with for loop
w='* '
N2=[['  'for j in range(5)]for i in range(5)]
for i in range (5):
    for j in range(5):
        if(i==4 or i==2 or i==0 or (i==1 and j==4)or(i==3 and j==0)):
           N2[i][j]=w
        print(N2[i][j],end='')
    print()    
