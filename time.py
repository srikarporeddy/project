hrs  = input ('enter a hrs')
min  = input ('enter a min')
sec  = input ('enter a sec')

d=(int(hrs)*int(60)*int(60))+(int(min)*int(60)+int(sec))
#print(d)
standar_time= 86400
f=abs((int(d)-int(standar_time)))
print(f)
g=abs(float(f)/60)
print(g)
h=abs(float(g)/60)
print(h)

print('remianing \M-\C-x hours: %2f' %(h))
#print'remaining time in hours:%f ' ihy
#%d abs((int(d)-int(standar_time)))
'''
import sys
print (sys.platform)
print (2 ** 100)
raw_input( )
sec="60"
min="60"
hrs="24"

#hours=
#minutes=(int(min)*int(sec))
#seconds=(int(sec)

giventime = "hours+minutes+seconds"
#print 'total number of seconds for hours: %d'% ((int(hrs)*int(60)*int(60))+(int(min)*int(60)+int(sec)))
#print 'total number of seconds for minute: %d'% (int(min)*int(60)+int(sec))
 #print 'total number given seconds: %d'% (int(sec))'''
