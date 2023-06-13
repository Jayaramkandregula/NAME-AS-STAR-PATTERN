#Direct list method
t='* '
O=[['  ',t,t,t,'  '],[t,'  ','  ','  ',t],[t,'  ','  ','  ',t],[t,'  ','  ','  ',t],['  ',t,t,t,'  ']]
for i in O:    
    for j in i:
        print(j,end='')
    print()

print()

#using loops
s='* '
for i in range(5):   
    for j in range(5):
        if((i==0 or i==4 or j==0 or j==4) and (i+j!=0 and i+j!=4 and i+j!=8)):
             print(s,end='')
        else:
            print(" ",end=' ')
    print()

print()

#Using Nested with for loop
w='* '
O=[['  'for j in range(5)]for i in range(5)]
for i in range (5):
    for j in range(5):
        if((i==0 or i==4 or j==0 or j==4) and (i+j!=0 and i+j!=4 and i+j!=8)):
           O[i][j]=w
        print(O[i][j],end='')
    print()    
