# It takes a word and returns the corrected word or the same word if the word in correct

import http.client, urllib.parse, json

def spellcheck(text):
    params = {'mkt': 'en-US', 'mode': 'proof', 'text': text}

    # NOTE: Replace this example key with a valid subscription key.
    key = '57fb7a0dd47d44008f68e027b09b30e4'

    host = 'api.cognitive.microsoft.com'
    path = '/bing/v7.0/spellcheck'

    headers = {'Ocp-Apim-Subscription-Key': key,
            'Content-Type': 'application/x-www-form-urlencoded'}

    # The headers in the following example 
    # are optional but should be considered as required:
    #
    # X-MSEdge-ClientIP: 999.999.999.999  
    # X-Search-Location: lat: +90.0000000000000;long: 00.0000000000000;re:100.000000000000
    # X-MSEdge-ClientID: <Client ID from Previous Response Goes Here>

    conn = http.client.HTTPSConnection(host)
    params = urllib.parse.urlencode (params)
    conn.request ("POST", path, params, headers)
    response = conn.getresponse ()
    a=response.read()
    
    a=a.decode()
    p = json.loads(a)
    if(p["flaggedTokens"]!=[]):
        p=p["flaggedTokens"][0]['suggestions'][0]['suggestion']
    else:
        p=text
    return(p)




