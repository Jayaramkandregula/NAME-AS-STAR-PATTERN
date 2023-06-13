#Direct list method
t='* '
N1=[['  ','  ',t,'  ','  '],['  ',t,t,'  ','  '],[t,'  ',t,'  ','  '],['  ','  ',t,'  ','  '],[t,t,t,t,t]]
for i in N1:    
    for j in i:
        print(j,end='')
    print()

print()

#using loops
s='* '
for i in range(5):   
    for j in range(5):
        if(i==4 or j==2 or (i+j==2)):
            print(s,end='')
        else:
            print(" ",end=' ')
    print()

print()

#Using Nested with for loop
w='* '
N1=[['  'for j in range(5)]for i in range(5)]
for i in range (5):
    for j in range(5):
        if(i==4 or j==2 or (i+j==2)):
           N1[i][j]=w
        print(N1[i][j],end='')
    print()    
