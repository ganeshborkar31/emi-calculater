#EMI calaulater
p=int(input('enter a principal Amount  '))
r=float(input('enter a rate per year  '))
t=int(input('enter a time in month  '))
print(p,   r,t)
r=r/(100*12)
#t=12*t    #if time in year
emi=(p*r*pow(1+r,t))/(pow(1+r,t)-1)
print('EMI=',emi)
print('total pay=',emi*t)