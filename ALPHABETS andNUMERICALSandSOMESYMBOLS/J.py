#Direct list method
t='* '
J=[[t,t,t,t,t],['  ','  ',t,'  ','  '],['  ','  ',t,'  ','  '],['  ','  ',t,'  ','  '],[t,t,t,'  ','  ']]
for i in J:    
    for j in i:
        print(j,end='')
    print()

print()

#using loops
s='* '
for i in range(5):   
    for j in range(5):
        if(j==2 or i==0 or (i==4 and (j==0 or j==1))):
             print(s,end='')
        else:
            print(" ",end=' ')
    print()

print()

#Using Nested with for loop
w='* '
J=[['  'for j in range(5)]for i in range(5)]
for i in range (5):
    for j in range(5):
        if(j==2 or i==0 or (i==4 and (j==0 or j==1))):
           J[i][j]=w
        print(J[i][j],end='')
    print()    
