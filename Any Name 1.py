#function block
def namepattern(name):
    t='* '
    namelist=[]
    for i in name:
        if i=='A':
            A=[['  ',t,t,t,'  '],[t,'  ','  ','  ',t],[t,t,t,t,t],[t,'  ','  ','  ',t],[t,'  ','  ','  ',t]]
            namelist.append(A)
        elif i=='B':
            B=[[t,t,t,t,'  '],[t,'  ','  ','  ',t],[t,t,t,t,'  '],[t,'  ','  ','  ',t],[t,t,t,t,'  ']]
            namelist.append(B)
        elif i=='C':
            C=[['  ',t,t,t,t],[t,'  ','  ','  ','  '],[t,'  ','  ','  ','  '],[t,'  ','  ','  ','  '],['  ',t,t,t,t]]
            namelist.append(C)
        elif i=='D':
            D=[[t,t,t,t,'  '],[t,'  ','  ','  ',t],[t,'  ','  ','  ',t],[t,'  ','  ','  ',t],[t,t,t,t,"  "]]
            namelist.append(D)
        elif i=='E':
            E=[[t,t,t,t,t],[t,'  ','  ','  ','  '],[t,t,t,t,'  '],[t,'  ','  ','  ','  '],[t,t,t,t,t]]
            namelist.append(E)
        elif i=='F':
            F=[[t,t,t,t,t],[t,'  ','  ','  ','  '],[t,t,t,t,'  '],[t,'  ','  ','  ','  '],[t,'  ','  ','  ','  ']]
            namelist.append(F)
        elif i=='G':
            G=[[t,t,t,t,t],[t,'  ','  ','  ','  '],[t,'  ',t,t,t],[t,'  ',t,'  ',t],[t,t,t,'  ',t]]
            namelist.append(G)
        elif i=='H':
            H=[[t,'  ','  ','  ',t],[t,'  ','  ','  ',t],[t,t,t,t,t],[t,'  ','  ','  ',t],[t,'  ','  ','  ',t]]
            namelist.append(H)
        elif i=='I':
            I=[[t,t,t,t,t],['  ','  ',t,'  ','  '],['  ','  ',t,'  ','  '],['  ','  ',t,'  ','  '],[t,t,t,t,t]]
            namelist.append(I)
        elif i=='J':
            J=[[t,t,t,t,t],['  ','  ',t,'  ','  '],['  ','  ',t,'  ','  '],['  ','  ',t,'  ','  '],[t,t,t,'  ','  ']]
            namelist.append(J)
        elif i=='K':
            K=[[t,'  ','  ',t,t],[t,'  ',t,'  ','  '],[t,t,'  ','  ','  '],[t,'  ',t,'  ','  '],[t,'  ','  ',t,t]]
            namelist.append(K)
        elif i=='L':
            L=[[t,'  ','  ','  ','  '],[t,'  ','  ','  ','  '],[t,'  ','  ','  ','  '],[t,'  ','  ','  ','  '],[t,t,t,t,t]]
            namelist.append(L)
        elif i=='M':
            M=[[t,'  ','  ','  ',t],[t,t,'  ',t,t],[t,'  ',t,'  ',t],[t,'  ','  ','  ',t],[t,'  ','  ','  ',t]]
            namelist.append(M)
        elif i=='N':
            N=[[t,'  ','  ','  ',t],[t,t,'  ','  ',t],[t,'  ',t,'  ',t],[t,'  ','  ',t,t],[t,'  ','  ','  ',t]]
            namelist.append(N)
        elif i=='O':
            O=[['  ',t,t,t,'  '],[t,'  ','  ','  ',t],[t,'  ','  ','  ',t],[t,'  ','  ','  ',t],['  ',t,t,t,'  ']]
            namelist.append(O)
        elif i=='P':
            P=[[t,t,t,t,'  '],[t,'  ','  ','  ',t],[t,t,t,t,'  '],[t,'  ','  ','  ','  '],[t,'  ','  ','  ','  ']]
            namelist.append(P)
        elif i=='Q':
            Q=[['  ',t,t,t,'  '],[t,'  ','  ','  ',t],[t,'  ',t,'  ',t],['  ',t,t,t,'  '],['  ','  ','  ','  ',t]]
            namelist.append(Q)
        elif i=='R':
            R=[[t,t,t,t,'  '],[t,'  ','  ','  ',t],[t,t,t,t,'  '],[t,'  ','  ','  ',t],[t,'  ','  ','  ',t]]
            namelist.append(R)
        elif i=='S':
            S=[['  ',t,t,t,t],[t,'  ','  ','  ','  '],[t,t,t,t,t],['  ','  ','  ','  ',t],[t,t,t,t,'  ']]
            namelist.append(S)
        elif i=='T':
            T=[[t,t,t,t,t],['  ','  ',t,'  ','  '],['  ','  ',t,'  ','  '],['  ','  ',t,'  ','  '],['  ','  ',t,'  ','  ']]
            namelist.append(T)
        elif i=='U':
            U=[[t,'  ','  ','  ',t],[t,'  ','  ','  ',t],[t,'  ','  ','  ',t],[t,'  ','  ','  ',t],['  ',t,t,t,'  ']]
            namelist.append(U)
        elif i=='V':
            V=[[t,'  ','  ','  ',t],[t,'  ','  ','  ',t],[t,'  ','  ','  ',t],['  ',t,'  ',t,'  '],['  ','  ',t,'  ','  ']]
            namelist.append(V)
        elif i=='W':
            W=[[t,'  ','  ','  ',t],[t,'  ','  ','  ',t],[t,'  ',t,'  ',t],[t,t,'  ',t,t],[t,'  ','  ','  ',t]]
            namelist.append(W)
        elif i=='X':
            X=[[t,'  ','  ','  ',t],['  ',t,'  ',t,'  '],['  ','  ',t,'  ','  '],['  ',t,'  ',t,'  '],[t,'  ','  ','  ',t]]
            namelist.append(X)
        elif i=='Y':
            Y=[[t,'  ','  ','  ',t],[t,'  ','  ','  ',t],['  ',t,t,t,'  '],['  ','  ',t,'  ','  '],['  ','  ',t,'  ','  ']]
            namelist.append(Y)
        elif i=='Z':
            Z=[[t,t,t,t,t],['  ','  ','  ',t,'  '],['  ','  ',t,'  ','  '],['  ',t,'  ','  ','  '],[t,t,t,t,t]]
            namelist.append(Z)
        elif i=='0':
            N0=[[t,t,t,t,t],[t,'  ','  ','  ',t],[t,'  ','  ','  ',t],[t,'  ','  ','  ',t],[t,t,t,t,t]]
            namelist.append(N0)
        elif i=='1':
            N1=[['  ','  ',t,'  ','  '],['  ',t,t,'  ','  '],[t,'  ',t,'  ','  '],['  ','  ',t,'  ','  '],[t,t,t,t,t]]
            namelist.append(N1)
        elif i=='2':
            N2=[[t,t,t,t,t],['  ','  ','  ','  ',t],[t,t,t,t,t],[t,'  ','  ','  ','  '],[t,t,t,t,t]]
            namelist.append(N2)
        elif i=='3':
            N3=[[t,t,t,t,t],['  ','  ','  ','  ',t],[t,t,t,t,t],['  ','  ','  ','  ',t],[t,t,t,t,t]]
            namelist.append(N3)
        elif i=='4':
            N4=[[t,'  ','  ','  ',t],[t,'  ','  ','  ',t],[t,t,t,t,t],['  ','  ','  ','  ',t],['  ','  ','  ','  ',t]]
            namelist.append(N4)
        elif i=='5':
            N5=[[t,t,t,t,t],[t,'  ','  ','  ','  '],[t,t,t,t,t],['  ','  ','  ','  ',t],[t,t,t,t,t]]
            namelist.append(N5)
        elif i=='6':
            N6=[[t,t,t,t,t],[t,'  ','  ','  ','  '],[t,t,t,t,t],[t,'  ','  ','  ',t],[t,t,t,t,t]]
            namelist.append(N6)
        elif i=='7':
            N7=[[t,t,t,t,t],['  ','  ','  ',t,'  '],['  ','  ',t,'  ','  '],['  ',t,'  ','  ','  '],[t,'  ','  ','  ','  ']]
            namelist.append(N7)
        elif i=='8':
            N8=[[t,t,t,t,t],[t,'  ','  ','  ',t],[t,t,t,t,t],[t,'  ','  ','  ',t],[t,t,t,t,t]]
            namelist.append(N8)
        elif i=='9':
            N9=[[t,t,t,t,t],[t,'  ','  ','  ',t],[t,t,t,t,t],['  ','  ','  ','  ',t],[t,t,t,t,t]]
            namelist.append(N9)
        elif i=='@':
            L_=[['  ',t,'  ',t,'  '],[t,'  ',t,'  ',t],[t,'  ','  ','  ',t],['  ',t,'  ',t,'  '],['  ','  ',t,'  ','  ']]
            namelist.append(L_)
        else:
            print(invalid)
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
namepattern("JAYARAM")
namepattern("@")
namepattern("")
namepattern("")

