from influxdb import InfluxDBClient
from datetime import datetime
import requests 
import json
import configparser
config = configparser.ConfigParser()
config.read('Init.ini')
host =config['InfluxDB']['host'] 
password= config['InfluxDB']['password'] 
user= config['InfluxDB']['user'] 
dbname =config['InfluxDB']['dbname'] 
port=config['InfluxDB']['port']
source=config['InfluxDB']['source']

def main():
    query = 'select * from '+ dbname
    client = InfluxDBClient(host, port, user, password, dbname)
    client.create_database(dbname)
    client.create_retention_policy('awesome_policy', '3d', 3, default=True)
    r = requests.get(source)
    content = r.json()
    measurements = []
    for c, v in content.items():
        measurements.append({
            "measurement": "TokenPrice",
            "tags": {               
                "TokenCode": v['symbol']
            },
            "time": datetime.now(),
            "fields": {             
                "value": v['currentPrice']
               
            }
        }) 
    client.write_points(measurements)
    
    result = client.query(query)

    print("Result: {0}".format(result))

main()