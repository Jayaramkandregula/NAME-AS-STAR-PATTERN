#Direct list method
t='* '
C=[["  ",t,t,t,t],[t,"  ",'  ','  ','  '],[t,"  ",'  ','  ','  '],[t,"  ",'  ','  ','  '],["  ",t,t,t,t]]
for i in C:    
    for j in i:
        print(j,end='')
    print()

print()

#using loops
s='* '
for i in range(5):   
    for j in range(5):
        if((i==0 or i==4)and(j>0)or(j==0 and(i>0 and i<4))):
             print(s,end='')
        else:
            print(" ",end=' ')
    print()

print()

#Using Nested with for loop
w='* '
C=[['  'for j in range(5)]for i in range(5)]
for i in range (5):
    for j in range(5):
        if((i==0 or i==4)and(j>0)or(j==0 and(i>0 and i<4))):
            C[i][j]=w
        print(C[i][j],end='')
    print()    
