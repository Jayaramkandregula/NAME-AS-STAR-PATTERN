#Direct list method
t='* '
S=[['  ',t,t,t,t],[t,'  ','  ','  ','  '],[t,t,t,t,t],['  ','  ','  ','  ',t],[t,t,t,t,'  ']]
for i in S:    
    for j in i:
        print(j,end='')
    print()

print()

#using loops
s='* '
for i in range(5):   
    for j in range(5):
        if(i==2 or (i==0 and j!=0)or(i==4 and j!=4) or (i==1 and j==0)or(i==3 and j==4)):
             print(s,end='')
        else:
            print(" ",end=' ')
    print()

print()

#Using Nested with for loop
w='* '
S=[['  'for j in range(5)]for i in range(5)]
for i in range (5):
    for j in range(5):
        if(i==2 or (i==0 and j!=0)or(i==4 and j!=4) or (i==1 and j==0)or(i==3 and j==4)):
           S[i][j]=w
        print(S[i][j],end='')
    print()    
