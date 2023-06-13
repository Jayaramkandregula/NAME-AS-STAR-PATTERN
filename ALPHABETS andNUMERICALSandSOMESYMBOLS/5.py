#Direct list method
t='* '
N5=[[t,t,t,t,t],[t,'  ','  ','  ','  '],[t,t,t,t,t],['  ','  ','  ','  ',t],[t,t,t,t,t]]
for i in N5:    
    for j in i:
        print(j,end='')
    print()

print()

#using loops
s='* '
for i in range(5):   
    for j in range(5):
        if(i==0 or i==2 or i==4 or (i==1 and j==0)or(j==4 and i==3)):
            print(s,end='')
        else:
            print(" ",end=' ')
    print()

print()

#Using Nested with for loop
w='* '
N5=[['  'for j in range(5)]for i in range(5)]
for i in range (5):
    for j in range(5):
        if(i==0 or i==2 or i==4 or (i==1 and j==0)or(j==4 and i==3)):
           N5[i][j]=w
        print(N5[i][j],end='')
    print()    
