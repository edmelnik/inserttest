from influxdb import InfluxDBClient
from configparser import ConfigParser
parser = ConfigParser()
client = InfluxDBClient(host='localhost', port=8086)
client.switch_database('insert_testing')
CONF='/Users/edmelnik/Library/CloudStorage/iCloud Drive/Documents/GitHub/inserttest/inserttest.config' 

parser.read(CONF)

    
json_body = [
    {
        "measurement":"break-force",
        "tags": {
            "Machine": "test-unit-2",
            "Insert number": parser.get('inserttest_config', 'insert_number'),
            "Size": parser.get('inserttest_config', 'size'),
            "Insert_Section": parser.get('inserttest_config', 'insert_section')   
            },
            "fields":{
                "Weight": parser.get('inserttest_config', 'weight'),
                "Frequency": parser.get('inserttest_config','frequency')
                
                }
      
            }
        ]
    client.write_points(json_body)