# crypto-price-get
1. Set parameter init.ini
2. Run 
2.1 Window set Schedule call run.bat
2.2 Linux Set crontab call job.sh
3. Test Run get.py
NOTE
1. If You would like get price of all Tokens at time 
Please set value time at line 29 = "datetime.now()"
2. If you would like get Price last change of Tokens
Please set values time at line 29 ="datetime.fromtimestamp(v['lastTimestamp'])"
REFERENCE
https://www.influxdata.com/
https://github.com/influxdata/influxdb
https://github.com/influxdata/influxdb-python
https://www.tautvidas.com/blog/2017/01/tracking-market-activity-with-influxdb/
