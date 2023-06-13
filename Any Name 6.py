def namepattern(name):
    patterndic=dict();w='* '
    for k in range(65,92):patterndic[chr(k)]=[['  'for j in range(5)]for i in range(5)]
    for k in range(10):patterndic[str(k)]=[['  'for j in range(5)]for i in range(5)]
    patterndic['@']=[['  'for j in range(5)]for i in range(5)];patterndic['$']=[['  'for j in range(5)]for i in range(5)]
    patterndic[' ']=[['  'for j in range(5)]for i in range(5)];namelist=[]
    for i in range (5):
        for j in range(5):
            if(((i!=0)and(j==0 or j==4)) or ((i==0 or i==2) and (j!=0 and j!=4))):patterndic['A'][i][j]=w
            if(((i==0 or i==2 or i==4)and(j!=4))or(i==1 or i==3)and(j==0 or j==4)):patterndic['B'][i][j]=w
            if((i==0 or i==4)and(j>0)or(j==0 and(i>0 and i<4))):patterndic['C'][i][j]=w
            if(j==0 or ((i==0 or i==4)and j!=4)or(j==4 and (i!=0 and i!=4))):patterndic['D'][i][j]=w   
            if(j==0 or i==0 or i==4 or (i==2 and j!=4)):patterndic['E'][i][j]=w        
            if(i==0 or j==0 or(i==2 and j!=4)):patterndic['F'][i][j]=w
            if(i==0 or j==0 or ((j==2 or j==4) and (i!=1)) or (i+j==5 and i!=1)):patterndic['G'][i][j]=w
            if(i==2 or j==0 or j==4):patterndic['H'][i][j]=w
            if(j==2 or i==0 or i==4):patterndic['I'][i][j]=w
            if(j==2 or i==0 or (i==4 and (j==0 or j==1))):patterndic['J'][i][j]=w
            if(j==0 or ((i==0 or i==4)and(j==3 or j==4))or i+j==3 or (i==3 and j==2)):patterndic['K'][i][j]=w
            if(j==0 or i==4):patterndic['L'][i][j]=w
            if(j==0 or j==4 or (i==1 and j!=2)or (i==j==2)):patterndic['M'][i][j]=w
            if(j==0 or j==4 or i==j):patterndic['N'][i][j]=w
            if((i==0 or i==4 or j==0 or j==4) and (i+j!=0 and i+j!=4 and i+j!=8)):patterndic['O'][i][j]=w
            if(j==0 or ((i==0 or i==2)and j!=4)or(j==4 and i==1)):patterndic['P'][i][j]=w
            if(((i==0 or i==3)and(j>0 and j<4))or((i==1 or i==2)and(j==0 or j==4))or(i==j and (i!=0 and i!=1))):patterndic['Q'][i][j]=w
            if(j==0 or (j==4 and (i!=0 and i!=2))or(j!=4 and (i==0 or i==2))):patterndic['R'][i][j]=w
            if(i==2 or (i==0 and j!=0)or(i==4 and j!=4) or (i==1 and j==0)or(i==3 and j==4)):patterndic['S'][i][j]=w
            if(i==0 or j==2):patterndic['T'][i][j]=w
            if(((j==0 or j==4)and(i!=4))or(i==4 and (j!=0 and j!=4))):patterndic['U'][i][j]=w
            if(((j==0 or j==4)and(i!=4 and i!=3))or(i==3 and (j==1 or j==3))or(i==4 and j==2)):patterndic['V'][i][j]=w
            if(j==0 or j==4 or ((i==j or i+j==4)and(i!=1))):patterndic['W'][i][j]=w
            if(i==j or i+j==4):patterndic['X'][i][j]=w
            if((j==0 or j==4) and (i==0 or i==1) or (i==2 and j!=0 and j!=4)or(j==2 and i>2)):patterndic['Y'][i][j]=w
            if(i==0 or i+j==4 or i==4):patterndic['Z'][i][j]=w
            if(i==0 or j==0 or i==4 or j==4):patterndic['0'][i][j]=w
            if(i==4 or j==2 or (i+j==2)):patterndic['1'][i][j]=w
            if(i==4 or i==2 or i==0 or (i==1 and j==4)or(i==3 and j==0)):patterndic['2'][i][j]=w
            if(j==4 or i==0 or i==2 or i==4):patterndic['3'][i][j]=w
            if(j==4 or i==2 or (j==0 and i<3)):patterndic['4'][i][j]=w
            if(i==0 or i==2 or i==4 or (i==1 and j==0)or(j==4 and i==3)):patterndic['5'][i][j]=w
            if(i==0 or i==2 or i==4 or j==0 or (i==3 and j==4)):patterndic['6'][i][j]=w
            if(i==0 or i+j==4):patterndic['7'][i][j]=w
            if(i==0 or i==2 or i==4 or j==0 or j==4):patterndic['8'][i][j]=w
            if(i==0 or i==2 or i==4 or (j==0 and i==1) or j==4):patterndic['9'][i][j]=w
            if(((j==0 or j==4)and(i==1 or i==2))or((j==1 or j==3)and(i==3 or i==0))or(j==2 and (i==1 or i==4))):patterndic['@'][i][j]=w
            if(i==2 or i==1 or(i==4 and j==2)or(i==0 and (j==1 or j==3))or(i==3 and (j!=0 and j!=4))):patterndic['$'][i][j]=w
    for t in name:namelist.append(patterndic[t])
    for i in range(5):
        for j in range(len(namelist)):
            for k in range(5):
                print(namelist[j][i][k],end='')
            print(end='  ')
        print()
    print('\n')
print("\n") #main block
namepattern("JAYARAM 17")
j=len("JAYARAM 17")
print("21/04/2003".center(j*10+(j*2-3) , '-'),'\n','\n')
namepattern(" @ $ @ ")
j=len("     ")
print("         ".center(j*10+(j*2-3) , '-'),'\n','\n')
namepattern("       ")


