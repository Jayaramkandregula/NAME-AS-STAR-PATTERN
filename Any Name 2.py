#function block
def namepattern(name):
    w='* '
    namelist=[]
    for i in name:
        if i=='A':
            A=[['  'for j in range(5)]for i in range(5)]
            for i in range (5):
                for j in range(5):
                    if(((i!=0)and(j==0 or j==4)) or ((i==0 or i==2) and (j!=0 and j!=4))):
                        A[i][j]=w
            namelist.append(A)
        elif i=='B':
            B=[['  'for j in range(5)]for i in range(5)]
            for i in range (5):
                for j in range(5):
                    if(((i==0 or i==2 or i==4)and(j!=4))or(i==1 or i==3)and(j==0 or j==4)):
                        B[i][j]=w
            namelist.append(B)
        elif i=='C':
            C=[['  'for j in range(5)]for i in range(5)]
            for i in range (5):
                for j in range(5):
                    if((i==0 or i==4)and(j>0)or(j==0 and(i>0 and i<4))):
                        C[i][j]=w
            namelist.append(C)
        elif i=='D':
            D=[['  'for j in range(5)]for i in range(5)]
            for i in range (5):
                for j in range(5):
                    if(j==0 or ((i==0 or i==4)and j!=4)or(j==4 and (i!=0 and i!=4))):
                        D[i][j]=w
            namelist.append(D)
        elif i=='E':
            E=[['  'for j in range(5)]for i in range(5)]
            for i in range (5):
                for j in range(5):
                    if(j==0 or i==0 or i==4 or (i==2 and j!=4)):
                        E[i][j]=w
            namelist.append(E)
        elif i=='F':
            F=[['  'for j in range(5)]for i in range(5)]
            for i in range (5):
                for j in range(5):
                    if(i==0 or j==0 or(i==2 and j!=4)):
                       F[i][j]=w
            namelist.append(F)
        elif i=='G':
            G=[['  'for j in range(5)]for i in range(5)]
            for i in range (5):
                for j in range(5):
                    if(i==0 or j==0 or ((j==2 or j==4) and (i!=1)) or (i+j==5 and i!=1)):
                        G[i][j]=w
            namelist.append(G)
        elif i=='H':
            H=[['  'for j in range(5)]for i in range(5)]
            for i in range (5):
                for j in range(5):
                    if(i==2 or j==0 or j==4):
                       H[i][j]=w
            namelist.append(H)
        elif i=='I':
            I=[['  'for j in range(5)]for i in range(5)]
            for i in range (5):
                for j in range(5):
                    if(j==2 or i==0 or i==4):
                       I[i][j]=w
            namelist.append(I)
        elif i=='J':
            J=[['  'for j in range(5)]for i in range(5)]
            for i in range (5):
                for j in range(5):
                    if(j==2 or i==0 or (i==4 and (j==0 or j==1))):
                       J[i][j]=w
            namelist.append(J)
        elif i=='K':
            K=[['  'for j in range(5)]for i in range(5)]
            for i in range (5):
                for j in range(5):
                    if(j==0 or ((i==0 or i==4)and(j==3 or j==4))or i+j==3 or (i==3 and j==2)):
                        K[i][j]=w
            namelist.append(K)
        elif i=='L':
            L=[['  'for j in range(5)]for i in range(5)]
            for i in range (5):
                for j in range(5):
                    if(j==0 or i==4):
                       L[i][j]=w
            namelist.append(L)
        elif i=='M':
            M=[['  'for j in range(5)]for i in range(5)]
            for i in range (5):
                for j in range(5):
                    if(j==0 or j==4 or (i==1 and j!=2)or (i==j==2)):
                        M[i][j]=w
            namelist.append(M)
        elif i=='N':
            N=[['  'for j in range(5)]for i in range(5)]
            for i in range (5):
                for j in range(5):
                    if(j==0 or j==4 or i==j):
                       N[i][j]=w
            namelist.append(N)
        elif i=='O':
            O=[['  'for j in range(5)]for i in range(5)]
            for i in range (5):
                for j in range(5):
                    if((i==0 or i==4 or j==0 or j==4) and (i+j!=0 and i+j!=4 and i+j!=8)):
                       O[i][j]=w
            namelist.append(O)
        elif i=='P':
            P=[['  'for j in range(5)]for i in range(5)]
            for i in range (5):
                for j in range(5):
                    if(j==0 or ((i==0 or i==2)and j!=4)or(j==4 and i==1)):
                       P[i][j]=w
            namelist.append(P)
        elif i=='Q':
            Q=[['  'for j in range(5)]for i in range(5)]
            for i in range (5):
                for j in range(5):
                    if(((i==0 or i==3)and(j>0 and j<4))or((i==1 or i==2)and(j==0 or j==4))or(i==j and (i!=0 and i!=1))):
                      Q[i][j]=w
            namelist.append(Q)
        elif i=='R':
            R=[['  'for j in range(5)]for i in range(5)]
            for i in range (5):
                for j in range(5):
                    if(j==0 or (j==4 and (i!=0 and i!=2))or(j!=4 and (i==0 or i==2))):
                       R[i][j]=w
            namelist.append(R)
        elif i=='S':
            S=[['  'for j in range(5)]for i in range(5)]
            for i in range (5):
                for j in range(5):
                    if(i==2 or (i==0 and j!=0)or(i==4 and j!=4) or (i==1 and j==0)or(i==3 and j==4)):
                       S[i][j]=w
            namelist.append(S)
        elif i=='T':
            T=[['  'for j in range(5)]for i in range(5)]
            for i in range (5):
                for j in range(5):
                    if(i==0 or j==2):
                       T[i][j]=w
            namelist.append(T)
        elif i=='U':
            U=[['  'for j in range(5)]for i in range(5)]
            for i in range (5):
                for j in range(5):
                    if(((j==0 or j==4)and(i!=4))or(i==4 and (j!=0 and j!=4))):
                        U[i][j]=w
            namelist.append(U)
        elif i=='V':
            V=[['  'for j in range(5)]for i in range(5)]
            for i in range (5):
                for j in range(5):
                    if(((j==0 or j==4)and(i!=4 and i!=3))or(i==3 and (j==1 or j==3))or(i==4 and j==2)):
                       V[i][j]=w
            namelist.append(V)
        elif i=='W':
            W=[['  'for j in range(5)]for i in range(5)]
            for i in range (5):
                for j in range(5):
                    if(j==0 or j==4 or ((i==j or i+j==4)and(i!=1))):
                       W[i][j]=w
            namelist.append(W)
        elif i=='X':
            X=[['  'for j in range(5)]for i in range(5)]
            for i in range (5):
                for j in range(5):
                    if(i==j or i+j==4):
                       X[i][j]=w
            namelist.append(X)
        elif i=='Y':
            Y=[['  'for j in range(5)]for i in range(5)]
            for i in range (5):
                for j in range(5):
                    if((j==0 or j==4) and (i==0 or i==1) or (i==2 and j!=0 and j!=4)or(j==2 and i>2)):
                       Y[i][j]=w
            namelist.append(Y)
        elif i=='Z':
            Z=[['  'for j in range(5)]for i in range(5)]
            for i in range (5):
                for j in range(5):
                    if(i==0 or i+j==4 or i==4):
                       Z[i][j]=w
            namelist.append(Z)
        elif i=='0':
            N0=[['  'for j in range(5)]for i in range(5)]
            for i in range (5):
                for j in range(5):
                    if(i==0 or j==0 or i==4 or j==4):
                       N0[i][j]=w
            namelist.append(N0)
        elif i=='1':
            N1=[['  'for j in range(5)]for i in range(5)]
            for i in range (5):
               for j in range(5):
                    if(i==4 or j==2 or (i+j==2)):
                       N1[i][j]=w
            namelist.append(N1)
        elif i=='2':
            N2=[['  'for j in range(5)]for i in range(5)]
            for i in range (5):
                for j in range(5):
                    if(i==4 or i==2 or i==0 or (i==1 and j==4)or(i==3 and j==0)):
                       N2[i][j]=w
            namelist.append(N2)
        elif i=='3':
            N3=[['  'for j in range(5)]for i in range(5)]
            for i in range (5):
                for j in range(5):
                    if(j==4 or i==0 or i==2 or i==4):
                        N3[i][j]=w
            namelist.append(N3)
        elif i=='4':
            N4=[['  'for j in range(5)]for i in range(5)]
            for i in range (5):
                for j in range(5):
                    if(j==4 or i==2 or (j==0 and i<3)):
                       N4[i][j]=w
            namelist.append(N4)
        elif i=='5':
            N5=[['  'for j in range(5)]for i in range(5)]
            for i in range (5):
                for j in range(5):
                   if(i==0 or i==2 or i==4 or (i==1 and j==0)or(j==4 and i==3)):
                       N5[i][j]=w
            namelist.append(N5)
        elif i=='6':
            N6=[['  'for j in range(5)]for i in range(5)]
            for i in range (5):
                for j in range(5):
                    if(i==0 or i==2 or i==4 or j==0 or (i==3 and j==4)):
                         N6[i][j]=w
            namelist.append(N6)
        elif i=='7':
            N7=[['  'for j in range(5)]for i in range(5)]
            for i in range (5):
                for j in range(5):
                    if(i==0 or i+j==4):
                       N7[i][j]=w
            namelist.append(N7)
        elif i=='8':
            N8=[['  'for j in range(5)]for i in range(5)]
            for i in range (5):
                for j in range(5):
                    if(i==0 or i==2 or i==4 or j==0 or j==4):
                       N8[i][j]=w
            namelist.append(N8)
        elif i=='9':
            N9=[['  'for j in range(5)]for i in range(5)]
            for i in range (5):
                for j in range(5):
                    if(i==0 or i==2 or i==4 or (j==0 and i==1) or j==4):
                       N9[i][j]=w
            namelist.append(N9)
        elif i=='@':
            L_=[['  'for j in range(5)]for i in range(5)]
            for i in range (5):
                for j in range(5):
                    if(((j==0 or j==4)and(i==1 or i==2))or((j==1 or j==3)and(i==3 or i==0))or(j==2 and (i==1 or i==4))):
                       L_[i][j]=w
            namelist.append(L_)
        elif i=='$':
            L__=[['  'for j in range(5)]for i in range(5)]
            for i in range (5):
                for j in range(5):
                    if(i==2 or i==1 or(i==4 and j==2)or(i==0 and (j==1 or j==3))or(i==3 and (j!=0 and j!=4))):
                       L__[i][j]=w
            namelist.append(L__)
        elif i==' ':
            S_=[['  'for j in range(5)]for i in range(5)]
            namelist.append(S_)
        else:
            print("invalid")
    #print(namelist)
    #print nested list which contains name in pattern   
    for i in range(5):
        for j in range(len(namelist)):
            for k in range(5):
                print(namelist[j][i][k],end='')
            print(end='  ')
        print()
    print('\n')
#main block
print("\n")
namepattern("JAYARAM")
j=len("JAYARAM")
print("21/04/2003".center(j*10+(j*2-3) , '-'),'\n','\n')
namepattern(" @ $ @ ")
j=len("      ")
print("       ".center(j*10+(j*2-3) , '-'),'\n','\n')
namepattern("      ")
