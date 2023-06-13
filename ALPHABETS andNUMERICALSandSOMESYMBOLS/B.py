#Direct list method
t='* '
B=[[t,t,t,t,'  '],[t,'  ','  ','  ',t],[t,t,t,t,'  '],[t,'  ','  ','  ',t],[t,t,t,t,'  ']]
for i in B:
    for j in i:
        print(j,end='')
    print()

print()

#Using loops
s='*'
for i in range(5):    
    for j in range(5):
        if(((i==0 or i==2 or i==4)and(j!=4))or(i==1 or i==3)and(j==0 or j==4)):
            print(s,end=' ')
        else:
            print('  ',end='')
    print()

print()

#Using Nested lists with for loop
w='* '
B=[['  'for j in range(5)]for i in range(5)]
for i in range (5):
    for j in range(5):
        if(((i==0 or i==2 or i==4)and(j!=4))or(i==1 or i==3)and(j==0 or j==4)):
            B[i][j]=w
        print(B[i][j],end='')
    print()

