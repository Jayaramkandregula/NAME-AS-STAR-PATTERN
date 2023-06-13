#Direct list method
t='* '
D=[[t,t,t,t,'  '],[t,'  ','  ','  ',t],[t,'  ','  ','  ',t],[t,'  ','  ','  ',t],[t,t,t,t,"  "]]
print(D)
for i in D:    
    for j in i:
        print(j,end='')
    print()

print()

#using loops
s='* '
for i in range(5):   
    for j in range(5):
        if(j==0 or ((i==0 or i==4)and j!=4)or(j==4 and (i!=0 and i!=4))):
             print(s,end='')
        else:
            print(" ",end=' ')
    print()

print()

#Using Nested with for loop
w='* '
D=[['  'for j in range(5)]for i in range(5)]
for i in range (5):
    for j in range(5):
        if(j==0 or ((i==0 or i==4)and j!=4)or(j==4 and (i!=0 and i!=4))):
            D[i][j]=w
        print(D[i][j],end='')
    print()    
