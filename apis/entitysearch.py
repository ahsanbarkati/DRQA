
import http.client, urllib.parse
import json

# **********************************************
# *** Update or verify the following values. ***
# **********************************************

# Replace the subscriptionKey string value with your valid subscription key.


def get_suggestions ():
	subscriptionKey = '517b1aeb605140d28aaaa6d7a5ab4512'

	host = 'api.cognitive.microsoft.com'
	path = '/bing/v7.0/entities'

	mkt = 'en-US'
	query = input()

	params = '?mkt=' + mkt + '&q=' + urllib.parse.quote (query)
	headers = {'Ocp-Apim-Subscription-Key': subscriptionKey}
	conn = http.client.HTTPSConnection (host)
	conn.request ("GET", path + params, None, headers)
	response = conn.getresponse ()
	result= response.read ()
	return (json.dumps(json.loads(result), indent=4))
