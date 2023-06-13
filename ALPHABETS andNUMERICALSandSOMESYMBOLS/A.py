#Direct list method
t='* '
A=[["  ",t,t,t,"  "],[t,'  ','  ','  ',t],[t,t,t,t,t],[t,'  ','  ','  ',t],[t,'  ','  ','  ',t]] #Nested list
for i in A:    #i is sublist
    for j in i:
        print(j,end='')
    print()

print()

#Using loops
s='* '
for i in range(5):    #i as rows and j as columns
    for j in range(5):
        if(((i!=0)and(j==0 or j==4)) or ((i==0 or i==2) and (j!=0 and j!=4))):
            print(s,end='')
        else:
            print(" ",end=' ')
    print()

print()

#Using Nested lists with for loop
w='* '
A=[['  'for j in range(5)]for i in range(5)]
for i in range (5):
    for j in range(5):
        if(((i!=0)and(j==0 or j==4)) or ((i==0 or i==2) and (j!=0 and j!=4))):
            A[i][j]=w
        print(A[i][j],end='')
    print()    
