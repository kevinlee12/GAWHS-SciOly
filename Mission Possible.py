#Mission Possible
file = write('Mission Possible.txt','r')
print("2014 LA Regionals")
print("Mission Possible")
#Safety Test
name = input('Name:')
file.write('Mission Possible\n')
file.write('Name:' + name + '\n')
pts = 0
safety = input("Is the device safe? Y/n:")
file.write('Safe to operate' + safety + '\n')
if safety == 'N' or safety == 'n':
    print('Not eligible to compete, team will be granted participation points only.')
    file.write('Not eligible to compete, team will be granted participation points only.')
    pts = 1
    quit()
#Construction Test Pt. 1
tier = 'Tier 1'
print("All parts of the device must fit and stay within a 60.0 cm x 60.0 cm x 60.0 cm box before, during, and after operation.")
c_a = input("Y/n:")
if c_a == "N" or c_a == "n":
    tier = 'Tier 2'
if c_a == 'Y' or c_a == 'y':
    length = input('Length (cm):')
    pts = pts + (60-length)*0.1
    width = input('Width (cm):')
    pts = pts + (60-length)*0.1
    height = input('Height(cm):')
    pts = pts + (60-length)*0.1
print("The device must be designed and constructed to use forms of energy, list in 3.e., to complete a sequence of transfers that all contribute to the completion of the Final Task.")
c_b = input('Y/n:')
if c_b == 'N' or c_b == 'n':
    tier == 'Tier 2'
print('The device must begin with the Start Task and end with the Final Task as listed in Section 4 and there are Five Basic Energy Forms availible.')
c_c = input('Y/n:')
if c_c == 'N' or c_c == 'n':
    tier == 'Tier 2'
print('The machine operates autonomously.')
c_d = input('Y/n:')
if c_d == 'N' or c_d == 'n':
    tier == 'Tier 2'
print('All scorable actions are visible with the exception of radio and infared electromagnetic spectrum transfers.')
c_g = input('Y/n:')
if c_g == 'N' or c_g == 'n':
    tier = 'Tier 2'
print('No hazardous spills, leaks, sparks')
c_k = input("Y/n:")
if c_k == "N" or c_k =="n":
    tier = 'Tier 2'
print("Power to any circuit must not exceed 10 volts, all batteries must be factory sealed and voltage labeled by the manufacturer.")
c_m = input("Y/n:")
if c_m == 'N' or c_m == "n":
    tier = 'Tier 2'
print('Top and at least 1 vertical wall is open or transparent for viewing')
c_o = input('Y/n:')
if c_o == 'N' or c_o == 'n':
    tier = 'Tier 2'
#Scoring
print('Scoring')
#ETL
sub = input("Submission of Energy Transfer List. Y/n")
if sub == 'Y' or sub == 'y':
    pts = pts + 25
    format = input('Is the ETL in the format specified? Y/n')
    if format == 'Y' or format == 'y':
        pts = pts + 25
    label = input('Are the SCORABLE transfers in the ETL labeled in the device? Y/n')
    if label == 'Y' or label == 'y':
        pts = pts + 25
    accuracy = input('Is the ETL 100% accurate in intended scorable and non-scorable transfers? Y/n')
    if accuracy == 'Y' or accuracy == 'y':
        pts = pts + 25
#Set-up
set_up = input('Does the team take LESS than 30 mins to set up?')
if set_up == 'Y' or set_up == 'y':
    pts = pts + 50
#Energy Transfers/Points Earning Section
e_pts = 0
print('Energy Transfer Count\n')
print('Awarded only if time is within 180 seconds.')
f_e = input('Times an Energy was used for the first time:')
f_e = int(f_e)
if f_e > 5:
    f_e = 5
e_pts = 30*f_e
s_e = input('Times an Energy was used for the Second time:')
s_e = int(s_e)
if s_e > 5:
    s_e = 5
e_pts = e_pts + 20*s_e
t_e = input('Times an Energy was used for the Second time:')
t_e = int(t_e)
if t_e > 5:
    t_e = 5
e_pts = e_pts + 10*t_e
if e_pts > 300:
    e_pts =300
final = ('Does the device switch on the light? Y/n')
if final == 'Y' or final == 'y':
    pts = pts + 50
pts = e_pts + pts
#Time
print('Time')
sec = input('Seconds of operation:')
sec = float(sec)
if sec > 180:
    pts = pts - sec
#Penalities
p_pts = 0
print('Penalties')
containter = input('Number of times original object is sorted into a wrong final container:')
contain = int(container)
p_pts = contain*5
contact = input('Number of times device was touched, sorted, or restarted:')
contact = int(contact)
p_pts = p_pts + contact*15
bounds = input('Did any part or substance of the device leave the boundary? (except smoke, odors, light, radio waves, etc) Y/n')
if bounds == 'Y' or bounds == 'y':
    p_pts = p_pts + 50
pts = pts - p_pts
