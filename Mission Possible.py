#Mission Possible
import sys 
print("2014 LA Regionals")
print("Mission Possible")
#Safety Test
name = input('Name:')
safety = ("Is the device safe? Y/n")
if safety == 'N' or safety == 'n':
  print('Not eligible to compete, team will be granted participation points only.')
  sys.exit()
#Construction Test Pt. 1
tier = 'Tier 1'
print("All parts of the device must fit and stay within a 60.0 cm x 60.0 cm x 60.0 cm box.")
3_a = input("Y/n")
if 3_a == "N" or 3_a == "n":
  tier = 'Tier 2'
print("The device must be designed and constructed to use forms of energy, list in 3.e., to complete a sequence of transfers that all contribute to the completion of the Final Task.")
3_b = input('Y/n')
if 3_b == 'N' or 3_b == 'n':
  tier == 'Tier 2'
print('The device must begin with the Start Task and end with the Final Task as listed in Section 4 and there are Five Basic Energy Forms availible.')
3_c = input('Y/n')
if 3_c == 'N' or 3_c == 'n':
  tier == 'Tier 2'
print('The machine operates autonomously.')
3_d = input('Y/n')
if 3_d == '
