__author__ = 'Indah'

t = input()

result=[]
for i in range(0,int(t)):
    if (t<=30):
        a,b=raw_input().split()
        if (0<int(a)<=20 and int(b)>0 and int(b)<2147483000):
            x=len(a)
            ld=a[x-1]
            if(int(ld)==2):
                val=int(b)%4
                if(val==1):
                    result.append(2)
                elif (val==2):
                    result.append(4)
                elif(val==3):
                    result.append(8)
                else:
                    result.append(6)
            elif(int(ld)==3):
                val=int(b)%4
                if(val==1):
                    result.append(3)
                elif (val==2):
                    result.append(9)
                elif(val==3):
                    result.append(7)
                else:
                    result.append(1)
            elif(int(ld)==4):
                val=int(b)%2
                if(val==1):
                    result.append(4)
                else:
                    result.append(6)
            elif(int(ld)==7):
                val=int(b)%4
                if(val==1):
                    result.append(7)
                elif (val==2):
                    result.append(9)
                elif(val==3):
                    result.append(3)
                else:
                    result.append(1)
            elif (int(ld)==8):
                val=int(b)%4
                if(val==1):
                    result.append(8)
                elif (val==2):
                    result.append(4)
                elif(val==3):
                    result.append(2)
                else:
                    result.append(6)
            elif(int(ld)==9):
                val=int(b)%2
                if(val==1):
                    result.append(9)
                else:
                    result.append(1)
            else :
                result.append(ld)

for i in range(0,len(result)):
    print result[i]
