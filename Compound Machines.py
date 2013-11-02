#Compound Machine
#Scoring Guidelines
#Version 1.2
#Stephanie Gu

#==========================================

import math
from math import *
import datetime
d= str(datetime.date.today())
print(d)
file = open('Compound_Machine'+d+'.txt','w')
print('2014 LA Regionals\n' + 'Compound Machines Cabinet Evaluations')
name = input('Name: ')
#File Write Top Part
file.write('2014 LA Regionals - COMPOUND MACHINES')
file.write('Test Date: ' + d + '\n')
file.write('Name: ' + name + '\n')

construction_score = 1

#event parameter
e_c = input("Everything fits inside a box no larger than 100 cm x 100 cm x 50.0 cm. Y/N " )
file.write('Everything fits inside a box no larger than 100cm x 100 cm x 50.0 cm: ' + e_c + '\n')
if e_c == "N" or e_c == "n":
    construction_score = 0

#construction parameters
c_a_1 = input("The device is a class 1 lever connected directly in series to a class 2 lever. Y/N ")
file.write('The device is a class 1 lever connected directly in series to a class 2 lever. ' + c_a_1 + '\n')
if c_a_1 == "N" or c_a_1 == "n":
    construction_score = 0

c_a_2 = input("Each lever has a single beam of length <= 50.0 cm. Y/N ")
file.write('Each lever has a single beam of length <= 50.0 cm. ' + c_a_2 + '\n')
if c_a_2 == "N" or c_a_2 == "n":
    construction_score = 0

c_b = input("The device is not made out of electric or electronic components. Y/N ")
file.write('The device is not made out of electric or electronic components. ' + c_b + '\n')
if c_b == "N" or c_b == "n":
    construction_score = 0

c_c = input("Is the device able to accommodate the masses? Y/N ")
file.write('The device is able to accommodate the masses. ' + c_c + '\n')
if c_c == "N" or c_c == "n":
    construction_score = 0

#competition_b_iii says that competitors can use
#their written test time to fix their devices
#but we're gonna be strict
#and not allow that! :D

if construction_score == 1:
    time = input("Number of seconds that the team took to calculate the mass ")
#convert int to str
    time1 = str(time)
    file.write('Number of seconds that the team took to calculate the mass: ' + time1 + '\n')

if construction_score == 1:
#AM is actual mass
#CM is calculated mass
    AM = input("The actual mass is how many grams? ")
    CM = input("The calculated mass is how many grams? ")
    AM1 = str(AM)
    CM1 = str(CM)
    file.write('You calcuated ' + CM1 + '\n')
    file.write('The actual mass is ' + AM1 + '\n')
else:
    final_score = 0
    
#score calculation
if construction_score == 1:
    time_score = ((240 - time) / 240 ) * 20
    mass_score = (1 - ( fabs(AM - CM) / AM)) * 30
    final_score = time_score + mass_score
else:
    final_score = 0

print "The final score is ", final_score

final_score1 = str(final_score)
file.write('Final score: ' + final_score1 + '\n')
file.close()
