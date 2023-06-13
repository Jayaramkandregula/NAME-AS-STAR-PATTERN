#Direct list method
t='* '
N7=[[t,t,t,t,t],['  ','  ','  ',t,'  '],['  ','  ',t,'  ','  '],['  ',t,'  ','  ','  '],[t,'  ','  ','  ','  ']]
for i in N7:    
    for j in i:
        print(j,end='')
    print()

print()

#using loops
s='* '
for i in range(5):   
    for j in range(5):
        if(i==0 or i+j==4):
            print(s,end='')
        else:
            print(" ",end=' ')
    print()

print()

#Using Nested with for loop
w='* '
N7=[['  'for j in range(5)]for i in range(5)]
for i in range (5):
    for j in range(5):
        if(i==0 or i+j==4):
           N7[i][j]=w
        print(N7[i][j],end='')
    print()    
