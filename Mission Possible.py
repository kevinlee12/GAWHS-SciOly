#Mission Possible
#Written in Python 3
import datetime
d= str(datetime.date.today())
print(d)
file = open('Mission Possible ' + d + '.txt','w')
print("2014 LA Regionals")
print("Mission Possible")
name = input('Name:')
file.write('Mission Possible\n')
file.write('Test Date:' + d +'\n')
file.write('Name:' + name + '\n')
pts = 0
#Safety Test
safety = input("Is the device safe? Y/n:")
file.write('Safe to operate-' + safety + '\n')
if safety == 'N' or safety == 'n':
    print('Not eligible to compete, team will be granted participation points only.')
    file.write('Not eligible to compete, team will be granted participation points only.')
    pts = 1
    quit()
#Construction Test Pt. 1
tier = 'Tier 1'
##Dimension Check
print("All parts of the device must fit and stay within a 60.0 cm x 60.0 cm x 60.0 cm box before, during, and after operation.")
c_a = input("Y/n:")
file.write('All parts of the device must fit and stay within a 60.0 cm x 60.0 cm x 60.0 cm box before, during, and after operation:' + c_a + '\n')
if c_a == "N" or c_a == "n":
    tier = 'Tier 2'
if c_a == 'Y' or c_a == 'y':
    length = input('Length (cm):')
    pts = pts + (60-float(length))*0.1
    width = input('Width (cm):')
    pts = pts + (60-float(width))*0.1
    height = input('Height(cm):')
    pts = pts + (60-float(height))*0.1
    file.write("\tDimensions:" + ' Length:' + str(length) + ' Width:' + str(width) + ' Height:' + str(height) + '\n')
print("The device must be designed and constructed to use forms of energy, list in 3.e., to complete a sequence of transfers that all contribute to the completion of the Final Task.")
c_b = input('Y/n:')
file.write('The device must be designed and constructed to use forms of energy, list in 3.e., to complete a sequence of transfers that all contribute to the completion of the Final Task: ' + c_b + '\n')
if c_b == 'N' or c_b == 'n':
    tier == 'Tier 2'
print('The device must begin with the Start Task and end with the Final Task as listed in Section 4 and there are Five Basic Energy Forms availible.')
c_c = input('Y/n:')
file.write('The device must begin with the Start Task and end with the Final Task as listed in Section 4 and there are Five Basic Energy Forms availible: ' + c_c + '\n')
if c_c == 'N' or c_c == 'n':
    tier == 'Tier 2'
print('All scorable actions are visible with the exception of radio and infared electromagnetic spectrum transfers.')
c_g = input('Y/n:')
file.write('All scorable actions are visible with the exception of radio and infared electromagnetic spectrum transfers: ' + c_g + '\n')
if c_g == 'N' or c_g == 'n':
    tier = 'Tier 2'
print("Power to any circuit must not exceed 10 volts, all batteries must be factory sealed and voltage labeled by the manufacturer.")
c_m = input("Y/n:")
file.write('Power does not exceed 10 v & battery is factory sealed:' + c_m + '\n')
if c_m == 'N' or c_m == "n":
    tier = 'Tier 2'
print('Top and at least 1 vertical wall is open or transparent for viewing')
c_o = input('Y/n:')
print('Top and at least 1 vertical wall is open or transparent for viewing: ' + c_o + '\n')
if c_o == 'N' or c_o == 'n':
    tier = 'Tier 2'
#Scoring
print('Scoring')
print('The machine operates autonomously.')
c_d = input('Y/n:')
file.write('The machine operates autonomously: ' + c_d + '\n')
if c_d == 'N' or c_d == 'n':
    tier == 'Tier 2'
print('No hazardous spills, leaks, sparks: ')
c_k = input("Y/n:")
file.write('No hazardous spills, leaks, sparks: ' + c_k + '\n')
if c_k == "N" or c_k =="n":
    tier = 'Tier 2'
#ETL Check
sub = input("Submission of Energy Transfer List. Y/n:")
file.write('ETL\n')
file.write('ETL Submitted? ' + sub  + '\n')
if sub == 'Y' or sub == 'y':
    pts = pts + 25
    format = input('Is the ETL in the format specified? Y/n:')
    file.write("Is the ETL in the format specified? " + format + '\n')
    if format == 'Y' or format == 'y':
        pts = pts + 25
    label = input('Are the SCORABLE transfers in the ETL labeled in the device? Y/n:')
    file.write('Are the SCORABLE transfers in the ETL labeled in the device? ' + label + '\n')
    if label == 'Y' or label == 'y':
        pts = pts + 25
    accuracy = input('Is the ETL 100% accurate in intended scorable and non-scorable transfers? Y/n:')
    file.write('Is the ETL 100% accurate in intended scorable and non-scorable transfers? ' + accuracy + '\n')
    if accuracy == 'Y' or accuracy == 'y':
        pts = pts + 25
#Set-up
file.write("Set-up\n")
set_up = input('Does the team take LESS than 30 mins to set up?')
file.write('Does the team take LESS than 30 mins. to set-up? ' + set_up + '\n')
if set_up == 'Y' or set_up == 'y':
    pts = pts + 50
#Energy Transfers/Points Earning Section
file.write('Points Earned')
e_pts = 0
print('Energy Transfer Count\n')
print('Awarded only if time is within 180 seconds.')
f_e = input('Times an Energy was used for the first time: ')
f_e = int(f_e)
if f_e > 5:
    f_e = 5
e_pts = 30*f_e
file.write('First time energy use:' + str(e_pts) + '\n')
s_e = input('Times an Energy was used for the Second time: ')
s_e = int(s_e)
if s_e > 5:
    s_e = 5
e_pts = e_pts + 20*s_e
file.write('Second time energy use:' + str(20*s_e) + '\n')
t_e = input('Times an Energy was used for the Second time: ')
t_e = int(t_e)
if t_e > 5:
    t_e = 5
e_pts = e_pts + 10*t_e
file.write('Third time energy use:' + str(10*t_e) + '\n')
if e_pts > 300:
    e_pts =300
final = ('Does the device switch on the light? Y/n')
file.write('Does the device switch on the light? ' + final + '\n')
if final == 'Y' or final == 'y':
    e_pts = e_pts + 250
file.write('Points earned for this section:' + str(e_pts))
pts = e_pts + pts
#Time
print('Time')
sec = input('Seconds of operation:')
file.write('Seconds of operation: ' + sec + '\n')
sec = float(sec)
if sec > 180:
    pts = pts - sec
#Penalities
file.write('Penalties\n')
p_pts = 0
print('Penalties')
container = input('Number of times original object is sorted into a wrong final container: ')
file.write('Number of times original object is sorted into a wrong final container: ' + container + '\n')
contain = int(container)
p_pts = contain*5
contact = input('Number of times device was touched, sorted, or restarted:')
file.write('Number of times device was touched, sorted, or restarted: ' + contact + '\n')
contact = int(contact)
p_pts = p_pts + contact*15
bounds = input('Did any part or substance of the device leave the boundary? (except smoke, odors, light, radio waves, etc) Y/n:')
file.write('Did any part or substance of the device leave the boundary? (except smoke, odors, light, radio waves, etc) ' + bounds + '\n')
if bounds == 'Y' or bounds == 'y':
    p_pts = p_pts + 50
pts = pts - p_pts
parallel = input('Did the device at any time parallel task? Or hit a dead end? Y/n:')
if parallel == 'Y' or parallel == 'y':
    tier = 'Tier 3'
print('Total points: ' + str(pts))
print('Tier' + tier + '\n')
file.write('Tier: ' + tier + '\n')
file.write('Total points: ' + str(pts))
file.close
