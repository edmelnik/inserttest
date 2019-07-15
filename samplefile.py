from configparser import ConfigParser
parser = ConfigParser()
CONF='/Users/edmelnik/Library/CloudStorage/iCloud Drive/Documents/GitHub/inserttest/inserttest.config' 

parser.read(CONF)

insertnum = parser['inserttest_config']['insert_number']
if insertnum == '6':
    print(insertnum)
    