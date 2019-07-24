from configparser import ConfigParser
import piplates.DAQC2plate as DAQC2
import time
parser = ConfigParser()

CONF='/home/pi/Desktop/inserttest-master/inserttest.config'


parser.read(CONF)
if (parser['inserttest_config']['motor'] == 'on') and (parser['inserttest_config']['loadcell'] == 'on'):
    parser.read(CONF)
    if (parser['inserttest_config']['insert_section'] == 'right') or (parser['inserttest_config']['insert_section'] == 'left'):
        if (parser['inserttest_config']['size'] == '5'):
            steps = 100 #4965
        if (parser['inserttest_config']['size'] == '5.5'):
            steps = 4413
        if (parser['inserttest_config']['size'] == '7'):
            steps = 3310
    parser.read(CONF)
    if (parser['inserttest_config']['insert_section'] == 'middle'):
        if (parser['inserttest_config']['size'] == '5'):
            steps = 5241
        if (parser['inserttest_config']['size'] == '5.5'):
            steps = 4689
        if (parser['inserttest_config']['size'] == '7'):
            flag == 1
            steps = 4413
    x=1
    speed=.001
    slowpoint = (steps) *0.75
    #1000ms = 14.5/16ths of an inch on input resolution of 200
        
    DAQC2.toggleDOUTbit(7,0)
    if flag == 1:
    for x in range(steps):
        print(x)
        DAQC2.toggleDOUTbit(7,2)
        x=x+1
        if x==(int(slowpoint)):
            speed=.005
            time.sleep(speed)
        if flag == steps:
            flag == 0
    DAQC2.toggleDOUTbit(7,1)
            
    speed=.001
            
    for x in range(steps):
        DAQC2.toggleDOUTbit(7,2)
        x=x+1
        time.sleep(speed)
        
    DAQC2.setDOUTall(7,0)
else:
    print ("Error")

