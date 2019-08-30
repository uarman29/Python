#!/usr/bin/python # vim: set fileencoding=utf-8 :
#iSIGHT Partners utility script (SRv0.1)

import argparse
import hashlib
import hmac
import http.client
import urllib.parse
import time
import json
import xml
import email
import sys

# API KEYS HERE
public_key = 'bd91d6dfd1956f4041c346524039fda70a024d4bbae694eb97c73b124b61ad1f'
private_key = 'd2759dd0ac5f9cb039f341a90b73895643e36fa8bb2809a1215e3352e14d5368'

# Command Line Arguments Parsing
parser = argparse.ArgumentParser(description='iSIGHT utility IoC / InW download script.')
requiredNamed = parser.add_argument_group('required arguments')
requiredNamed.add_argument('-t', metavar='indicatorType', required=True,
					dest='indicatorType', action='store',
					help='IoC or InW')

requiredNamed.add_argument('-d',metavar='daysRequested', required=True,
					dest='daysRequested', action='store',
					help='# of days IoCs / InWs to obtain ie 1, 7, 30, 90.')

requiredNamed.add_argument('-f',metavar='format', required=True,
					dest='format', action='store',
					help='csv, xml, json, snort.')

parser.add_argument('-o', action='store_true',
					help='write to file instead of screen')
args = parser.parse_args()

# Command Line Arguments Error Checking
if args.o is not False:
	args.o = args.daysRequested + '.' + args.indicatorType + '.' + args.format
if args.format not in ('json', 'xml', 'csv', 'snort'): sys.exit("\nRequest format (-f) is not correct. csv, xml, json, snort only.")
if args.indicatorType not in ('IoC', 'InW'): sys.exit("\nRequest indicator type (-t) must be IoC or InW only.")

data = ''

# indicator type Setup
if args.indicatorType == 'IoC':
	queryType = '/view/iocs?'
else:
	queryType = '/view/indicators?'

# days Requested Setup
timeVal = int(args.daysRequested) * 86400

# 4 hours is 14400 seconds
# 7 days is 604800 seconds
# 14 days is 1209600 seconds
# 30 days is 2592000 seconds
# 90 days is 7776000 seconds
#Time range - Epoch time - required as int
query = {
    'startDate' : int(time.time()) - timeVal,
    'endDate' : int(time.time())
}
time_stamp = email.utils.formatdate(localtime=True)

#Create Query
enc_q = queryType + urllib.parse.urlencode(query) + '&format=' + args.format

#Generate proper accept_header for requested indicator type
accept_header = ''
if args.format == 'xml':
	accept_header = 'text/xml'
elif args.format == 'json':
	accept_header = 'application/json'
elif args.format == 'csv':
	accept_header = 'text/csv'
elif args.format == 'snort':
	accept_header = 'application/snort'
else:
	sys.exit("\nAccept-Header not right.")

#Generate Hash for Auth
data = enc_q + '2.6' + accept_header + time_stamp
hashed = hmac.new(bytes(private_key,'utf-8'), data.encode('utf-8'), hashlib.sha256)

headers = {
	'Accept': accept_header,
	'Accept-Version': '2.6',
	'X-Auth': public_key,
	'X-Auth-Hash': hashed.hexdigest(),
	'X-App-Name': 'mysight-api',
	'Date': time_stamp
}

#Get dataset
conn = http.client.HTTPSConnection('api.isightpartners.com')
conn.request('GET', enc_q, '', headers)

response = conn.getresponse()

#print response.status, response.reason
status = response.status
if status == 200 :
	print ('\nAPI Authentication good!')
if status == 204 :
	sys.exit('\nAPI Error 204: search Result not found.')
	print('\n')
if status == 404 :
    sys.exit("\nAPI Error 404.")
if status == 401 :
	sys.exit("\nAPI Error 401: Check keys, auth-hash headers, or timezone of workstation.")
if status != 200 :
	print(status)
	sys.exit("API Error. See iSIGHT API documentation.")

#Test for whether the user wanted file output or not
if args.o is False:
	print("Screen Output requested")
	print(response.read() )
else:
	filestatus = 'File output requested.\n'
	print(filestatus)
	data = response.read()
	filename = time_stamp.replace(":", ".")
	filename = filename[0:25] + ".xml"
	try:
		with open(filename, 'wb') as f:
			f.write(data)
			f.close()
			filewritten = filename + ' written to disk.'
			print(filewritten)
	except:
			import traceback
			traceback.print_exc()
			sys.exit('File not written.')

#Notify enduser what was requested.
TotalRequest = '\nYou requested: ' + args.daysRequested + ' day(s) of ' + args.indicatorType + ' indicators in ' + args.format
print(TotalRequest)
