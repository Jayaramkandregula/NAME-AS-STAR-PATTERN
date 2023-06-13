#Direct List method
t='* '
L_=[['  ',t,'  ',t,'  '],[t,'  ',t,'  ',t],[t,'  ','  ','  ',t],['  ',t,'  ',t,'  '],['  ','  ',t,'  ','  ']]
for i in L_:    
    for j in i:
        print(j,end='')
    print()

print()

#using Loops
s='* '
for i in range(5):   
    for j in range(5):
        if(((j==0 or j==4)and(i==1 or i==2))or((j==1 or j==3)and(i==3 or i==0))or(j==2 and (i==1 or i==4))):
             print(s,end='')
        else:
            print(" ",end=' ')
    print()

print()

#Using Nested with for Loop
w='* '
L_=[['  'for j in range(5)]for i in range(5)]
for i in range (5):
    for j in range(5):
        if(((j==0 or j==4)and(i==1 or i==2))or((j==1 or j==3)and(i==3 or i==0))or(j==2 and (i==1 or i==4))):
           L_[i][j]=w
        print(L_[i][j],end='')
    print()    
