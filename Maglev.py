#MagLev
#Scoring Guidelines
#Version 1.0
#Stephanie Gu

#=============================================

import math
from math import *
import datetime
d= str(datetime.date.today())
print(d)
file = open('MagLev'+d+'.txt','w')
print('2014 LA Regionals\n' + 'MagLev Cabinet Evaluations')
name = input('Name: ')
#File Write Top Part
file.write('2014 LA Regionals - MAGLEV')
file.write('Test Date: ' + d + '\n')
file.write('Name: ' + name + '\n')

penalty = 0
time_list = []

#event parameter
e_d = input("Teams are wearing eye protection at all times. Y/N ")
file.write('Teams are wearing eye protection at all times ' + e_d + '\n')
if e_d == "N" or e_d == "n":
    final_score = 0

#construction parameters
c_a = input("Does the vehicle modify the track? Y/N ")
file.write('Does the vehicle modify the track? ' + c_a + '\n')
if c_a == "Y" or c_a == "y":
    penalty = 20

c_b = input("The length of the vehicle is between 15.0 and 22.0 cm. Y/N ")
file.write('The length of the vehicle is between 15.0 and 22.0 cm. ' + c_b + '\n')
if c_b == "n" or c_b == "N":
    penalty = 20

c_c = input("The mass of the vehicle is: ")
c_c1 = str(c_c)
file.write('Does the vehicle modify the track? ' + c_c1 + '\n')
if c_c > 2000.0 or c_c < 250.0:
    penalty = 20

c_e = input("The vehicle is within the the vertical planes of the track. Y/N ")
file.write('The vehicle is within the vertical planes of the track ' + c_e + '\n')
if c_e == "N" or c_e == "n":
    penalty = 20

c_f_1 = input("The vehicle has a 1/4 inch dowel attached within 5.0 cm of the front edge. Y/N ")
file.write('The vehicle has a 1/4 inch dowl attached within 5.0 cm of the front edge. ' + c_f_1 + '\n')
if c_f_1 == "N" or c_f_1 == "n":
    penalty = 20

c_f_2 = input("The dowel is between 30.0 and 35.0 cm above the lowest vehicle surface. Y/N ")
file.write('The dowel is between 30.0 and 35.0 cm above the lowest vehicle surface ' + c_f_2 + '\n')
if c_f_2 == "N" or c_f_2 == "n":
    penalty = 20
    
c_f_3 = input("The dowel has a rigid flag that is at least 5.0 by 5.0 cm. Y/N ")
file.write('The dowel has a rigid flag that is at least 5.0 by 5.0 cm. ' + c_f_3 + '\n')
if c_f_3 == "N" or c_f_3 == "n":
    penalty = 20

c_f_4 = input("One side of the flag is parallel to the track and the other side is parallel to the dowel. Y/N ")
file.write('Sides of the flag are parallel to the track and the dowel. ' + c_f_4 + '\n')
if c_f_4 == "N" or c_f_4 == "n":
    penalty = 20

c_g_1 = input("Batteries are the only energy source. Y/N ")
file.write('Batteries are the only energy source. ' + c_g_1 + '\n')
if c_g_1 == "N" or c_g_1 == "n":
    penalty = 20

c_g_2 = input("Total voltage is at most 9.0 V. Y/N ")
file.write('Voltage is less than or equal to 9.0 V ' + c_g_2 + '\n')
if c_g_2 == "N" or c_g_2 == "n":
    penalty = 20

c_h_1 = input("Vehicle has one motor corresponding to one propeller. Y/N ")
file.write('Vehicle has one motor corresponding to one propellor ' + c_h_1 + '\n')
if c_h_1 == "N" or c_h_1 == "n":
    penalty = 20

c_h_2 = input("Propellers have a diameter <= 14.0 cm. Y/N ")
file.write('Propellers have a diameter less than or equal to 14.0 cm. ' + c_h_2 + '\n')
if c_h_2 == "N" or c_h_2 == "n":
    penalty = 20

c_h_3 = input("Propellers are shielded from direct contact so that a 1/4 inch dowel cannot make contact with it. Y/N ")
file.write('Propellers are shielded from direct contact so that a 1/4 inch dowel cannot make contacat with it. ' + c_h_3 + '\n')
if c_h_3 == "N" or c_h_3 == "n":
    penalty = 20

c_i = input("Brushless motors and integrated circuits are used. Y/N ")
file.write('Brushless motors and integrated circuits are used. ' + c_i + '\n')
if c_i == "Y" or c_i == "y":
    penalty = 20

c_j = input("Rare earth metals are used. Y/N ")
file.write('Rare earth metals are used ' + c_j + '\n')
if c_j == "Y" or c_j == "y":
    penalty = 20

c_k = input("Vehicle levitates. Y/N ")
file.write('Vehicle levitates. ' + c_k + '\n')
if c_k == "N" or c_k == "n":
    penalty = 20

c_l = input("Vehicle has an electric switch to permit safe starting. Y/N ")
file.write('Vehicle has an electric switch to permit safe starting ' + c_l + '\n')
if c_l == "N" or c_l == "n":
    penalty = 20

#testing

#run 1
time_1 = input("How many seconds did the vehicle take to travel 95.0 cm? If failed, respond with 0. ")
time_1_1 = str(time_1)
if time_1 >= 5.0 and time_1 <= 15.0:
    time_list.append(time_1)
file.write('Trial 1 time was ' + time_1_1 + '\n')

#run 2
time_2 = input("How many seconds did the vehicle take to travel 95.0 cm? If failed, respond with 0. ")
time_2_1 = str(time_2)
if time_2 >= 5.0 and time_2 <= 15.0:
    time_list.append(time_2)
file.write('Trial 2 time was ' + time_2_1 + '\n')

#other runs
if time_2 == 0:
    time_3 = input("How many seconds did the vehicle take to travel 95.0 cm? If failed, respond with 0. ")
    time_3_1 = str(time_3)
    if time_3 >= 5.0 and time_3 <= 15.0:
        time_list.append(time_3)
    file.write('Trial 3 time was ' + time_3_1 + '\n')
if len(time_list) < 2:
    time_4 = input("How many seconds did the vehicle take to travel 95.0 cm? If failed, respond with 0. ")
    time_4_1 = str(time_4)
    if time_4 >= 5.0 and time_4 <= 15.0:
        if len(time_list) < 3:
            time_list.append(time_4)
    file.write('Trial 4 time was ' + time_4_1 + '\n')
if len(time_list) < 2:
    time_5 = input("How many seconds did the vehicle take to travel 95.0 cm? If failed, respond with 0. ")
    time_5_1 = str(time_5)
    if time_5 >= 5.0 and time_5 <= 15.0:
        if len(time_list) < 3:
            time_list.append(time_5)
    file.write('Trial 5 time was ' + time_5_1 + '\n')

#competition rules will be designated as cc

cc_b_iii_1 = input("Competitors placed their vehicle on the track directly before the start line. Y/N ")
file.write('Competitors placed their vehicle on the track directly before the start line. ' + cc_b_iii_1 + '\n')
if cc_b_iii_1 == "N" or cc_b_iii_1 == "n":
    penalty = penalty + 2

cc_b_iii_2 = input("Competitors placed an object in front of their vehicle to keep it from moving. Y/N ")
file.write('Competitors placed an object in front of their vehicle to keep it from moving. ' + cc_b_iii_2 + '\n')
if cc_b_iii_2 == "N" or cc_b_iii_2 == "n":
    penalty = penalty + 2

cc_b_iii_3 = input("Team demonstrated a safe starting and ending process before a run. Y/N ")
file.write('Team demonstrated a safe starting and ending process before a run. ' + cc_b_iii_3 + '\n')
if cc_b_iii_3 == "N" or cc_b_iii_3 == "n":
    penalty = penalty + 2

cc_b_v = input("Competitors touch the vehicle after they have turned on their motor. Y/N ")
file.write('Competitors touch the vehicle after they have turned on their motor. ' + cc_b_v + '\n')
if cc_b_v == "Y" or cc_b_v == "y":
    penalty = penalty + 2

#Scoring

print "Calculating Scores"    
#mass score
heavy = input("What is the mass of the heaviest successful vehicle?")
file.write('The mass of the vehicle is ' + c_c1 + '\n')
mass_score = (c_c / heavy) * 25

if len(time_list) == 0:
    mass_score = 0

attempt = input("Did the team attempt any runs or move past the start line? Y/N ")
file.write('Did the team attempt any runs or move past the start line? ' + attempt + '\n')
if attempt == "N" or attempt == "n":
    mass_score = -5

impound = input("Did the team impound? Y/N ")
file.write('Impound? ' + impound + '\n')
if impound == "N" or impound == "n":
    mass_score = -10

mass_score_str = str(mass_score)
file.write('Mass score: ' + mass_score_str + '\n')

#time score
target = input("What was the target time in seconds? ")
target_str = str(target)
file.write('Target Time: ' + target_str + '\n')

TS = []
if len(time_list) == 0:
    time_score = 0
else:
    for x in time_list:
        list_score = (1 - (abs(x - target) / x)) * 25
        TS.append(list_score)
    
time_score = max(TS)
TS_str = str(time_score)
file.write('Time Score: ' + TS_str + '\n')

#final score
penalty_str = str(penalty)
file.write('Penalty: ' + penalty_str + '\n')
final_score = mass_score + time_score - penalty
print "The final sccore is ", final_score
final_score_str = str(final_score)
file.write('Final Score: ' + final_score_str + '\n')
file.close()
