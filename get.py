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
    result = client.query(query)

    print("Result: {0}".format(result))

main()