#Direct list method
t='* '
Z=[[t,t,t,t,t],['  ','  ','  ',t,'  '],['  ','  ',t,'  ','  '],['  ',t,'  ','  ','  '],[t,t,t,t,t]]
for i in Z:    
    for j in i:
        print(j,end='')
    print()

print()

#using loops
s='* '
for i in range(5):   
    for j in range(5):
        if(i==0 or i+j==4 or i==4):
             print(s,end='')
        else:
            print(" ",end=' ')
    print()

print()

#Using Nested with for loop
w='* '
Z=[['  'for j in range(5)]for i in range(5)]
for i in range (5):
    for j in range(5):
        if(i==0 or i+j==4 or i==4):
           Z[i][j]=w
        print(Z[i][j],end='')
    print()    
