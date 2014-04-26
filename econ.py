L=700
R=100
B=200
D=950
Nw=50
interest_rate=.1

for i in range(240):
    res_amount=D*interest_rate
    off_by=R-res_amount

    R-=off_by
    L+=off_by
    D+=off_by
    R+=off_by
    print str(i)+" L="+str(L)+" R="+str(R)+" D="+str(D)
    
print str(L+R+200)+"=?="+str(D+50)

