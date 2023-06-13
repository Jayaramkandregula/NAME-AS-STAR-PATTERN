#Direct list method
t='* '
T=[[t,t,t,t,t],['  ','  ',t,'  ','  '],['  ','  ',t,'  ','  '],['  ','  ',t,'  ','  '],['  ','  ',t,'  ','  ']]
for i in T:    
    for j in i:
        print(j,end='')
    print()

print()

#using loops
s='* '
for i in range(5):   
    for j in range(5):
        if(i==0 or j==2):
             print(s,end='')
        else:
            print(" ",end=' ')
    print()

print()

#Using Nested with for loop
w='* '
T=[['  'for j in range(5)]for i in range(5)]
for i in range (5):
    for j in range(5):
        if(i==0 or j==2):
           T[i][j]=w
        print(T[i][j],end='')
    print()    
