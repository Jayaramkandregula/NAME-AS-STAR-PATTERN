#Direct list method
t='* '
Q=[['  ',t,t,t,'  '],[t,'  ','  ','  ',t],[t,'  ',t,'  ',t],['  ',t,t,t,'  '],['  ','  ','  ','  ',t]]
for i in Q:    
    for j in i:
        print(j,end='')
    print()

print()

#using loops
s='* '
for i in range(5):   
    for j in range(5):
        if(((i==0 or i==3)and(j>0 and j<4))or((i==1 or i==2)and(j==0 or j==4))or(i==j and (i!=0 and i!=1))):
             print(s,end='')
        else:
            print(" ",end=' ')
    print()

print()

#Using Nested with for loop
w='* '
Q=[['  'for j in range(5)]for i in range(5)]
for i in range (5):
    for j in range(5):
        if(((i==0 or i==3)and(j>0 and j<4))or((i==1 or i==2)and(j==0 or j==4))or(i==j and (i!=0 and i!=1))):
           Q[i][j]=w
        print(Q[i][j],end='')
    print()    
