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
#-------------------------------------------------------------------
#Variables are consistent with the rule number in the rule book
c_a = input('The entire Scrambler does not exceed 1.00 m in height and depth and not exceed 0.75 m in width. Y/n:')
file.write('The entire Scrambler does not exceed 1.00 m in height and depth and not exceed 0.75 m in width - ' + c_a)
if c_a == 'N' or c_a == 'n':
    tier = 'Tier 2'
c_c = input('Mass must NOT exceed 2.00 kg and must be detachable. Y/n: ')
file.write('Mass must NOT exceed 2.00 kg and must be detachable: ' + c_c)
if c_c == 'N' or c_c == 'n':
    tier = 'Tier 2'
