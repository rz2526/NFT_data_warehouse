#!/usr/bin/python3
import json
import requests
import sys

query_text="""query MyQuery
{
	collections(first: 5)
	{
		id
	}
}
"""

class tester:
	def __init__(self,url:str)->None:
		self._url=url
		
	def query(self,query_statement:str)->dict:
		req_dict={"operationName":"MyQuery","query":query_statement,"variables":None}
		req_text=json.dumps(req_dict,indent='\t')
		print(req_text)
		resp=requests.post(self._url,req_text,headers={"content-type":"application/json"})
		print(resp.text)
		return resp.json()

# This program tests the availability of our deployed server.
if __name__=="__main__":
	test_url="https://api.studio.thegraph.com/proxy/45684/opensea-subgraph-dcab1/v0.0.9"
	i=1
	while i<len(sys.argv):
		match sys.argv[i]:
			case "--url":
				i+=1
				test_url=sys.argv[i]
			case "--statement":
				i+=1
			case other:
				print("Warning: ignoring unknown option {}!".format(sys.argv[i]))
		i+=1
	t=tester(test_url)
	resp=t.query(query_text)
	print(resp)