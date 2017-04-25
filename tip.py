meal = input('enter meal bill:')
tax  = input('enter a tax:')
tip  = input('enter a tip:')
T=(float(tax)/100)
print(T)
p=(float(tip)/100)
print(p)
g=float(meal)+(float(meal)*float(T))
print(g)
total= float(g)+(float(g)*float(p))
print("%.2f" % total)
from datetime import datetime
now = str(datetime.now())
#print 'billing date&time')now

print   (now)


# Assign the variable total on line 8!
'''
meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + meal * tax
total= meal+meal*tip


print("%.2f" % total)
'''