#Direct list method
t='* '
Y=[[t,'  ','  ','  ',t],[t,'  ','  ','  ',t],['  ',t,t,t,'  '],['  ','  ',t,'  ','  '],['  ','  ',t,'  ','  ']]
for i in Y:    
    for j in i:
        print(j,end='')
    print()

print()

#using loops
s='* '
for i in range(5):   
    for j in range(5):
        if((j==0 or j==4) and (i==0 or i==1) or (i==2 and j!=0 and j!=4)or(j==2 and i>2)):
             print(s,end='')
        else:
            print(" ",end=' ')
    print()

print()

#Using Nested with for loop
w='* '
Y=[['  'for j in range(5)]for i in range(5)]
for i in range (5):
    for j in range(5):
        if((j==0 or j==4) and (i==0 or i==1) or (i==2 and j!=0 and j!=4)or(j==2 and i>2)):
           Y[i][j]=w
        print(Y[i][j],end='')
    print()    
