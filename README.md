# Get-Total-TestCases
Sample Project for skunk Work

parseLog.py

Script to parse the log files for a microservice to identify the specifc entities needed for sequence mining.


testcases.py
Script to identify the total number of testcases that should be written. This reads the swagger file, looks at the HTTP protoco;s supported by an API, 
and the response codes supported by each API. Possible enum values of the POST/PATCH load will generate more automation testcases.


getDuplicates.py
Script to identy the duplicate file locations for the messgaes that have be localised. 
