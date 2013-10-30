#Scrambler
#Written in Python 3
import datetime
d= str(datetime.date.today())
print(d)
file = open('Scrambler'+d+'.txt','w')
print('2014 LA Regionals\n' + 'Scrambler Cabinet Evaluations')
name = input('Name: ')
#File Write Top Part
file.write('2014 LA Regionals - SCRAMBLER')
file.write('Test Date: ' + d + '\n')
file.write('Name: ' + name + '\n')
pts = 0
tier = 'Tier 1'
#-------------------------------------------------------------------
#Construction Test
#Please revise Tier 2/3/4
#-------------------------------------------------------------------
#Variables are consistent with the rule number in the rule book
c_a = input('The entire Scrambler does not exceed 1.00 m in height and depth and not exceed 0.75 m in width. Y/n:')
file.write('The entire Scrambler does not exceed 1.00 m in height and depth and not exceed 0.75 m in width: ' + c_a + '\n')
if c_a == 'N' or c_a == 'n':
    tier = 'Tier 3'
c_c = input('Mass must NOT exceed 2.00 kg and must be detachable. Y/n: ')
file.write('Mass must NOT exceed 2.00 kg and must be detachable: ' + c_c + '\n')
if c_c == 'N' or c_c == 'n':
    tier = 'Tier 3'
c_d = input('Stopping mechanism is contained entirely in the transport and not be remotely controlled. Y/n: ')
file.write('Stopping mechanism is contained entirely in the transport and not be remotely controlled: ' + c_d + '\n')
if c_d == 'n' or c_d == 'N':
    tier = 'Tier 3'
print('The egg must rest on top of two 1/4" wooden dowels which extend out a max of 4.0 cm from a rigid, unpadded and flat backstop for the egg.')
print('The bottom of the wooden dowels must be between 5.0 - 10.0 cm above the track. Backstop: rigid material and flat surface of 5.0 +/- 0.2 cm wide & high and 1.27 cm (0.50 cm") thick')
print('An additional vertical 1/4" wooden dowel must be permanently attached from the top center of the rigid backstop such that it will cross the laser path of the photogate system, approx. 20 cm from the floor')
c_e = input('Y/n: ')
file.write('Refer to Construction 2.e :' + c_e + '\n')
if c_e == 'n' or c_e == 'N':
    tier = "Tier 3"
c_f = input('Tape must be secured to the egg to the transport with no tape placed on the front/rear 2.0 cm of the egg. Y/n')
file.write('Tape must be secured to the egg to the transport with no tape placed on the front/rear 2.0 cm of the egg: ' + c_f + '\n')
if c_f == 'N' or c_f =='n':
    tier = 'Tier 3'
c_g = input('Competitors must start the Scrambler by using any part of an unsharpened #2 pencil with an unused eraser to start. Y/n: ')
file.write('Competitors must start the Scrambler by using any part of an unsharpened #2 pencil with an unused eraser to start.' + c_g + '\n')
if c_g == 'N' or c_g == 'n':
    tier = "Tier 3"
c_h = ('Only the wheel touches the ground, no pieces fall. Y/n:')
file.write('Only the wheel touches the ground, no pieces fall. Y/n:' + c_h + '\n')
if c_h == 'n' or c_h == 'N':
    tier = 'Tier 3'
c_i = input('No electronic device is used, EXCEPT for a calculator. Y/n: ')
file.write('No electronic device is used, EXCEPT for a calculator: ' + c_i + '\n')
if c_i == 'N' or c_i == 'n':
    tier = 'Tier 3'
#-------------------------------------------------------------------------------
#Competition - denoted using 'cc' variable
#-------------------------------------------------------------------------------
cc_d = input('Team does not roll their car on the track prior to actual test run. Y/n')
file.write('Team does not roll their car on the track prior to actual test run: ' + cc_d + '\n')
if cc_d == 'N' or cc_d == 'n':
    if tier == 'Tier 3':
        pass
    tier = 'Tier 2'
cc_e = input('Team keeps floor dry at all times, but may clean the floor. Y/n')
file.write('Team keeps floor dry at all times, but may clean the floor: ' + cc_e + '\n')
if cc_e == 'N' or cc_e == 'n':
    if tier == 'Tier 3':
        pass
    tier = 'Tier 2'
cc_f = input('All parts of the Scrambler are behind the starting line. Y/n:')
file.write('All parts of the Scrambler are behind the starting line: ' + cc_f + '\n')
if cc_f == 'N' or cc_f == 'n':
    if tier == 'Tier 3':
        pass
    tier = 'Tier 2'
print('Remind team to remove all sighting/aiming contraptions, press Enter to continue.')
input()
cc_h = input('Scrambler may be run only when triggered by No.2 pencil. Y/n')
file.write('Scrambler may be run only when triggered by No.2 pencil: ' + cc_h + '\n')
if cc_h == 'N' or cc_h == 'n':
    if tier == 'Tier 3':
        pass
    tier = 'Tier 2'
    
