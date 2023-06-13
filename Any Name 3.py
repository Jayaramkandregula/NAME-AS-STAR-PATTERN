#function block
def namepattern(name):
    w='* '
    A=[['  'for j in range(5)]for i in range(5)]
    for i in range (5):
        for j in range(5):
            if(((i!=0)and(j==0 or j==4)) or ((i==0 or i==2) and (j!=0 and j!=4))):
                A[i][j]=w
    B=[['  'for j in range(5)]for i in range(5)]
    for i in range (5):
        for j in range(5):
            if(((i==0 or i==2 or i==4)and(j!=4))or(i==1 or i==3)and(j==0 or j==4)):
                B[i][j]=w       
    C=[['  'for j in range(5)]for i in range(5)]
    for i in range (5):
        for j in range(5):
            if((i==0 or i==4)and(j>0)or(j==0 and(i>0 and i<4))):
                C[i][j]=w    
    D=[['  'for j in range(5)]for i in range(5)]
    for i in range (5):
        for j in range(5):
            if(j==0 or ((i==0 or i==4)and j!=4)or(j==4 and (i!=0 and i!=4))):
                D[i][j]=w   
    E=[['  'for j in range(5)]for i in range(5)]
    for i in range (5):
        for j in range(5):
            if(j==0 or i==0 or i==4 or (i==2 and j!=4)):
                E[i][j]=w        
    F=[['  'for j in range(5)]for i in range(5)]
    for i in range (5):
        for j in range(5):
            if(i==0 or j==0 or(i==2 and j!=4)):
                F[i][j]=w
    G=[['  'for j in range(5)]for i in range(5)]
    for i in range (5):
        for j in range(5):
            if(i==0 or j==0 or ((j==2 or j==4) and (i!=1)) or (i+j==5 and i!=1)):
                G[i][j]=w
    H=[['  'for j in range(5)]for i in range(5)]
    for i in range (5):
        for j in range(5):
            if(i==2 or j==0 or j==4):
                H[i][j]=w
    I=[['  'for j in range(5)]for i in range(5)]
    for i in range (5):
        for j in range(5):
            if(j==2 or i==0 or i==4):
                I[i][j]=w
    J=[['  'for j in range(5)]for i in range(5)]
    for i in range (5):
        for j in range(5):
            if(j==2 or i==0 or (i==4 and (j==0 or j==1))):
                J[i][j]=w
    K=[['  'for j in range(5)]for i in range(5)]
    for i in range (5):
        for j in range(5):
            if(j==0 or ((i==0 or i==4)and(j==3 or j==4))or i+j==3 or (i==3 and j==2)):
                K[i][j]=w
    L=[['  'for j in range(5)]for i in range(5)]
    for i in range (5):
        for j in range(5):
            if(j==0 or i==4):
                L[i][j]=w
    M=[['  'for j in range(5)]for i in range(5)]
    for i in range (5):
        for j in range(5):
            if(j==0 or j==4 or (i==1 and j!=2)or (i==j==2)):
                M[i][j]=w
    N=[['  'for j in range(5)]for i in range(5)]
    for i in range (5):
        for j in range(5):
            if(j==0 or j==4 or i==j):
                N[i][j]=w
    O=[['  'for j in range(5)]for i in range(5)]
    for i in range (5):
        for j in range(5):
            if((i==0 or i==4 or j==0 or j==4) and (i+j!=0 and i+j!=4 and i+j!=8)):
                O[i][j]=w
    P=[['  'for j in range(5)]for i in range(5)]
    for i in range (5):
        for j in range(5):
            if(j==0 or ((i==0 or i==2)and j!=4)or(j==4 and i==1)):
                P[i][j]=w
    Q=[['  'for j in range(5)]for i in range(5)]
    for i in range (5):
        for j in range(5):
            if(((i==0 or i==3)and(j>0 and j<4))or((i==1 or i==2)and(j==0 or j==4))or(i==j and (i!=0 and i!=1))):
                Q[i][j]=w
    R=[['  'for j in range(5)]for i in range(5)]
    for i in range (5):
        for j in range(5):
            if(j==0 or (j==4 and (i!=0 and i!=2))or(j!=4 and (i==0 or i==2))):
                R[i][j]=w
    S=[['  'for j in range(5)]for i in range(5)]
    for i in range (5):
        for j in range(5):
            if(i==2 or (i==0 and j!=0)or(i==4 and j!=4) or (i==1 and j==0)or(i==3 and j==4)):
                S[i][j]=w
    T=[['  'for j in range(5)]for i in range(5)]
    for i in range (5):
        for j in range(5):
            if(i==0 or j==2):
                T[i][j]=w
    U=[['  'for j in range(5)]for i in range(5)]
    for i in range (5):
        for j in range(5):
            if(((j==0 or j==4)and(i!=4))or(i==4 and (j!=0 and j!=4))):
                U[i][j]=w
    V=[['  'for j in range(5)]for i in range(5)]
    for i in range (5):
        for j in range(5):
            if(((j==0 or j==4)and(i!=4 and i!=3))or(i==3 and (j==1 or j==3))or(i==4 and j==2)):
                V[i][j]=w
    W=[['  'for j in range(5)]for i in range(5)]
    for i in range (5):
        for j in range(5):
            if(j==0 or j==4 or ((i==j or i+j==4)and(i!=1))):
                W[i][j]=w
    X=[['  'for j in range(5)]for i in range(5)]
    for i in range (5):
        for j in range(5):
            if(i==j or i+j==4):
                X[i][j]=w
    Y=[['  'for j in range(5)]for i in range(5)]
    for i in range (5):
        for j in range(5):
            if((j==0 or j==4) and (i==0 or i==1) or (i==2 and j!=0 and j!=4)or(j==2 and i>2)):
                Y[i][j]=w
    Z=[['  'for j in range(5)]for i in range(5)]
    for i in range (5):
        for j in range(5):
            if(i==0 or i+j==4 or i==4):
                Z[i][j]=w
    N0=[['  'for j in range(5)]for i in range(5)]
    for i in range (5):
        for j in range(5):
            if(i==0 or j==0 or i==4 or j==4):
                N0[i][j]=w
    N1=[['  'for j in range(5)]for i in range(5)]
    for i in range (5):
       for j in range(5):
            if(i==4 or j==2 or (i+j==2)):
                N1[i][j]=w
    N2=[['  'for j in range(5)]for i in range(5)]
    for i in range (5):
        for j in range(5):
            if(i==4 or i==2 or i==0 or (i==1 and j==4)or(i==3 and j==0)):
                N2[i][j]=w
    N3=[['  'for j in range(5)]for i in range(5)]
    for i in range (5):
        for j in range(5):
            if(j==4 or i==0 or i==2 or i==4):
                N3[i][j]=w
    N4=[['  'for j in range(5)]for i in range(5)]
    for i in range (5):
        for j in range(5):
            if(j==4 or i==2 or (j==0 and i<3)):
                N4[i][j]=w
    N5=[['  'for j in range(5)]for i in range(5)]
    for i in range (5):
        for j in range(5):
            if(i==0 or i==2 or i==4 or (i==1 and j==0)or(j==4 and i==3)):
                N5[i][j]=w
    N6=[['  'for j in range(5)]for i in range(5)]
    for i in range (5):
        for j in range(5):
            if(i==0 or i==2 or i==4 or j==0 or (i==3 and j==4)):
                N6[i][j]=w
    N7=[['  'for j in range(5)]for i in range(5)]
    for i in range (5):
        for j in range(5):
            if(i==0 or i+j==4):
                N7[i][j]=w
    N8=[['  'for j in range(5)]for i in range(5)]
    for i in range (5):
        for j in range(5):
            if(i==0 or i==2 or i==4 or j==0 or j==4):
                N8[i][j]=w
    N9=[['  'for j in range(5)]for i in range(5)]
    for i in range (5):
        for j in range(5):
            if(i==0 or i==2 or i==4 or (j==0 and i==1) or j==4):
                N9[i][j]=w
    L_=[['  'for j in range(5)]for i in range(5)]
    for i in range (5):
        for j in range(5):
            if(((j==0 or j==4)and(i==1 or i==2))or((j==1 or j==3)and(i==3 or i==0))or(j==2 and (i==1 or i==4))):
                L_[i][j]=w
    L__=[['  'for j in range(5)]for i in range(5)]
    for i in range (5):
        for j in range(5):
            if(i==2 or i==1 or(i==4 and j==2)or(i==0 and (j==1 or j==3))or(i==3 and (j!=0 and j!=4))):
                L__[i][j]=w
    S_=[['  'for j in range(5)]for i in range(5)]
    patterndic={"A":A,"B":B,"C":C,"D":D,"E":E,"F":F,"G":G,"H":H,"I":I,"J":J,"K":K,"L":L,"M":M,"N":N,"O":O,"P":P,"Q":Q,"R":R,"S":S,"T":T,"U":U,"V":V,"W":W,"X":X,"Y":Y,"Z":Z,"0":N0,"1":N1,"2":N2,"3":N3,"4":N4,"5":N5,"6":N6,"7":N7,"8":N8,"9":N9,"@":L_,"$":L__,' ':S_}
    namelist=[]
    for t in name:
        namelist.append(patterndic[t])
    #print(namelist)
    #print nested list which contains name in pattern   
    for i in range(5):
        for j in range(len(namelist)):
            for k in range(5):
                print(namelist[j][i][k],end='')
            print(end='  ')
        print()
    print('\n')

def born():
    for i in range(13):
        for j in range(13):
            if((i>2 and i<7)or(i==0 and (j==2 or j==3 or j==9 or j==10))or(i==1 and ((j>0 and j<5)or(j>7 and j<12)))or(i==2 and j!=6)or(i-j<7 and i+j<19 and i!=0 and i!=1 and i!=2)):
                print("* ",end='')
            else:
                print("  ",end='')
        print()
    print("\n")
def broke():
    for i in range(13):
        for j in range(13):
            if((j==3 and i==0)or(j==4 and (i==1 or i==5 or i==9))or(j==5 and (i==2 or i==4 or i==6 or i==8 or i==10))or(j==6 and (i==3 or i==7 or i>10))):
                print("*     ",end='')
            elif((i>2 and i<7)or(i==0 and (j==2 or j==3 or j==9 or j==10))or(i==1 and ((j>0 and j<5)or(j>7 and j<12)))or(i==2 and j!=6)or(i-j<7 and i+j<19 and i!=0 and i!=1 and i!=2)):
                print("* ",end='')
            else:
                print("  ",end='')
        print()
    print('\n')

        
#main block
print("\n")
namepattern("JAYARAM")
j=len("JAYARAM")
print("21/04/2003".center(j*10+(j*2-3) , '-'),'\n','\n')
namepattern(" @ $ @ ")
broke()
born()
j=len("      ")
print("        ".center(j*10+(j*2-3) , '-'),'\n','\n')
namepattern("         ")


