""" Calculates the day of the week for any given date.

Name: Anastasia Kim
UPI: akim517
ID: 6574566

"""

year = 1986    #16th of February, 1986 (my birthday)
month = 2
day = 16

a = int((14-month)/12)

y = year - a

m = month + 12*a - 2

d = (day + y + int(y/4) - int(y/100) + int(y/400) + int(31*m/12))%7

print (d)

