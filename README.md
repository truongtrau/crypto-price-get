# crypto-price-get
1. Set parameter init.ini
2. Run 
	2.1 Window set Schedule call run.bat
	2.2 Linux Set crontab call job.sh
NOTE
	1. If You would like get price of all Tokens at time 
	Please set value time at line 29 = "datetime.now()"
	2. If you would like get Price last change of Tokens
	Please set values time at line 29 ="datetime.fromtimestamp(v['lastTimestamp'])"
