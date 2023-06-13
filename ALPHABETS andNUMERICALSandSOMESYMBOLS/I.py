#Direct list method
t='* '
I=[[t,t,t,t,t],['  ','  ',t,'  ','  '],['  ','  ',t,'  ','  '],['  ','  ',t,'  ','  '],[t,t,t,t,t]]
for i in I:    
    for j in i:
        print(j,end='')
    print()

print()

#using loops
s='* '
for i in range(5):   
    for j in range(5):
        if(j==2 or i==0 or i==4):
             print(s,end='')
        else:
            print(" ",end=' ')
    print()

print()

#Using Nested with for loop
w='* '
I=[['  'for j in range(5)]for i in range(5)]
for i in range (5):
    for j in range(5):
        if(j==2 or i==0 or i==4):
           I[i][j]=w
        print(I[i][j],end='')
    print()    
