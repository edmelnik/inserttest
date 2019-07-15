from configparser import ConfigParser

parser = ConfigParser()
CONF='/Users/edmelnik/Library/CloudStorage/iCloud Drive/Documents/GitHub/inserttest/inserttest.config' 
parser.read('/Users/edmelnik/Library/CloudStorage/iCloud Drive/Documents/GitHub/inserttest/inserttest.config')

print(parser.get('inserttest_config', 'loadcell'))
parser.read(CONF)
if parser['inserttest_config']['insert_number'] == '1':
    parser['inserttest_config']['ping'] = 'on'
    with open(CONF, 'w') as updated_conf:
        parser.write(updated_conf)
parser.read(CONF)
if parser['inserttest_config']['ping'] =='off' and parser['inserttest_config']['motor'] == 'on':
    parser['inserttest_config']['ping'] = 'off'
    parser['inserttest_config']['insert_number'] = '6'
    with open(CONF, 'w') as updated_conf:
        parser.write(updated_conf)
