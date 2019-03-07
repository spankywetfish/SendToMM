#!/usr/bin/python3
import urllib3
import json
import certifi

mmURL = 'https://<yourwebhookURLhere>'

output_data = {}
output_data['text'] = 'text'
output_data['username'] = 'username'
output_data['icon'] = 'icon URL'
output_data['title'] = 'title'
output_data['pretext'] = 'pretext'

attachment_data = {}
attachment_data['attachments'] = [output_data]
output_data_json=json.dumps(attachment_data)

def SendToMM(output_data):
	http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
	req = http.request("POST", mmURL, body=output_data_json, headers={'Content-Type': 'application/json'})
	print (req.data.decode("utf-8"))
	return

SendToMM(output_data)
