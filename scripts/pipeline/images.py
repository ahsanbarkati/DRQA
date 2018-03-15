def images(query):
    import requests
    import json
    subscription_key = "367bf4f21c3a4e8c86bf2eaff473ae8b"
    assert subscription_key
    search_url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"
    search_term = query
    headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
    params  = {"q": search_term, "license": "public", "imageType": "photo"}
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()
    thumbnail_urls = [img["thumbnailUrl"] for img in search_results["value"][:16]]
   # thumbnail_urls=json.dumps(thumbnail_urls)
   
    return thumbnail_urls

