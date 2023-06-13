#Direct list method
t='* '
X=[[t,'  ','  ','  ',t],['  ',t,'  ',t,'  '],['  ','  ',t,'  ','  '],['  ',t,'  ',t,'  '],[t,'  ','  ','  ',t]]
for i in X:    
    for j in i:
        print(j,end='')
    print()

print()

#using loops
s='* '
for i in range(5):   
    for j in range(5):
        if(i==j or i+j==4):
             print(s,end='')
        else:
            print(" ",end=' ')
    print()

print()

#Using Nested with for loop
w='* '
X=[['  'for j in range(5)]for i in range(5)]
for i in range (5):
    for j in range(5):
        if(i==j or i+j==4):
           X[i][j]=w
        print(X[i][j],end='')
    print()    
