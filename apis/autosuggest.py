# -*- coding: utf-8 -*-

import http.client, urllib.parse, json

# **********************************************
# *** Update or verify the following values. ***
# **********************************************

# Replace the subscriptionKey string value with your valid subscription key.


def get_suggestions (query):
	"Gets Autosuggest results for a query and returns the information."
	subscriptionKey = '3583eb4841914f149ebcd7176b0c5f3e'
	host = 'api.cognitive.microsoft.com'
	path = '/bing/v7.0/Suggestions'
	mkt = 'en-US'
	params = '?mkt=' + mkt + '&q=' + query
	headers = {'Ocp-Apim-Subscription-Key': subscriptionKey}
	conn = http.client.HTTPSConnection(host)
	conn.request ("GET", path + params, None, headers)
	response = conn.getresponse ()
	result=response.read()
	res=json.dumps(json.loads(result), indent=4)
	res=json.loads(res)
	autoo_suggest=res["suggestionGroups"][0]["searchSuggestions"][0]["displayText"]
	return(auto_suggest)
