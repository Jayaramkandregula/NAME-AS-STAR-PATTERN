#Direct list method
t='* '
G=[[t,t,t,t,t],[t,'  ','  ','   ','  '],[t,'  ',t,t,t],[t,'  ',t,'  ',t],[t,t,t,'  ',t]]
for i in G:    
    for j in i:
        print(j,end='')
    print()

print()

#using loops
s='* '
for i in range(5):   
    for j in range(5):
        if(i==0 or j==0 or ((j==2 or j==4) and (i!=1)) or (i+j==5 and i!=1)):
             print(s,end='')
        else:
            print(" ",end=' ')
    print()

print()

#Using Nested with for loop
w='* '
G=[['  'for j in range(5)]for i in range(5)]
for i in range (5):
    for j in range(5):
        if(i==0 or j==0 or ((j==2 or j==4) and (i!=1)) or (i+j==5 and i!=1)):
            G[i][j]=w
        print(G[i][j],end='')
    print()    
