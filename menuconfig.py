from configparser import ConfigParser
parser = ConfigParser()
CONF='/Users/edmelnik/Library/CloudStorage/iCloud Drive/Documents/GitHub/inserttest/inserttest.config' 

parser.read(CONF)

print("PSNERGY BREAK TEST")
print("PSNERGY INSERT TESTING")
print("Select the default insert size")
print("1. 5 inches")
print("2. 5.5 inches")
print("3. 7 inches")
print("Enter Insert Number")
g = input()
while True:
    
    if int(g) != 0:
            insert = str(g)
            parser.read(CONF)
            parser['inserttest_config']['insert_number'] = g
            with open(CONF, 'w') as updated_conf:
                parser.write(updated_conf)
            print("Insert Number "+g+"")
            print("Enter the weight")
            weight = input()
            parser.read(CONF)
            parser['inserttest_config']['weight'] = weight
            with open(CONF, 'w') as updated_conf:
                parser.write(updated_conf)
            print("Press 1 for ping test")
            print("Press 2 for break test")
            print("Press 3 for calibration")
            print("Press 4 to change the insert size")
            print("To test next Insert type next")
            
            c =input()
           
            if c == '1':
                parser['inserttest_config']['ping'] = 'on'
                parser['inserttest_config']['motor'] = 'off'
                parser['inserttest_config']['loadcell'] = 'off'
                with open(CONF, 'w') as updated_conf:
                    parser.write(updated_conf)
                print("Ping test Selected")
                print("press button to ping")
                print("2 will take you to break test")
                c = input()
            if c == '2':
                parser['inserttest_config']['ping'] = 'off'
                parser['inserttest_config']['motor'] = 'on'
                parser['inserttest_config']['loadcell'] = 'on'
                
                with open(CONF, 'w') as updated_conf:
                    parser.write(updated_conf)
                print('Break left wing')
                parser['inserttest_config']['insert_section'] = 'left'
                with open(CONF, 'w') as updated_conf:
                    parser.write(updated_conf)
                input('Press enter to continue: ')
                print('Break right wing')
                parser['inserttest_config']['insert_section'] = 'right'
                with open(CONF, 'w') as updated_conf:
                    parser.write(updated_conf)
                input('Press enter to continue: ')
                print('break middle')
                parser['inserttest_config']['insert_section'] = 'middle'
                with open(CONF, 'w') as updated_conf:
                    parser.write(updated_conf)
                input('Press enter to continue: ')
                print('To test next part Type next')
                c = input()
            if c == '3':
                print("not done yet, come back later")
            if c == '4':
                print("1. 5 inches")
                print("2. 5.5 inches")
                print("3. 7 inches")
                insertsize = input()
                if insertsize =='1': 
                    parser['inserttest_config']['size'] = '5'
                    with open(CONF, 'w') as updated_conf:
                        parser.write(updated_conf)
                if insertsize =='2': 
                    parser['inserttest_config']['size'] = '5.5'
                    with open(CONF, 'w') as updated_conf:
                        parser.write(updated_conf)
                if insertsize =='3': 
                    parser['inserttest_config']['size'] = '7'
                    with open(CONF, 'w') as updated_conf:
                        parser.write(updated_conf)
                print("To test next insert type next")
                input(c)
            if c == 'next':
                parser['inserttest_config']['ping'] = 'off'
                parser['inserttest_config']['motor'] = 'off'
                parser['inserttest_config']['loadcell'] = 'off'
                parser['inserttest_config']['insert_section'] = 'none'
                with open(CONF, 'w') as updated_conf:
                    parser.write(updated_conf)
                print("Insert Number:")
                g = input()
                