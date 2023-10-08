L1=[]
L2=[]

LengthL1=len(L1)
LengthL2=len(L2)
i=0
while(i<=(LengthL1-1)):
    j=0
    while(j<=(LengthL2-1)):
        if(L1[i]==L2[j]):
            print(L1[i])
        j=j+1
    i=i+1