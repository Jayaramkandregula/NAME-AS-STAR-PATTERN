#Direct list method
t='* '
N4=[[t,'  ','  ','  ',t],[t,'  ','  ','  ',t],[t,t,t,t,t],['  ','  ','  ','  ',t],['  ','  ','  ','  ',t]]
for i in N4:    
    for j in i:
        print(j,end='')
    print()

print()

#using loops
s='* '
for i in range(5):   
    for j in range(5):
        if(j==4 or i==2 or (j==0 and i<3)):
            print(s,end='')
        else:
            print(" ",end=' ')
    print()

print()

#Using Nested with for loop
w='* '
N4=[['  'for j in range(5)]for i in range(5)]
for i in range (5):
    for j in range(5):
        if(j==4 or i==2 or (j==0 and i<3)):
           N4[i][j]=w
        print(N4[i][j],end='')
    print()    
