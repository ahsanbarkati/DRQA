
# coding: utf-8

# In[129]:


subscription_key = "367bf4f21c3a4e8c86bf2eaff473ae8b"
assert subscription_key


# In[130]:


search_url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"


# In[131]:


search_term = "Rajeev Gandhi"


# In[132]:


import requests

headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
params  = {"q": search_term, "license": "public", "imageType": "photo"}
response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()
search_results = response.json()


# In[133]:


thumbnail_urls = [img["thumbnailUrl"] for img in search_results["value"][:16]]


# In[134]:


get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

f, axes = plt.subplots(4, 4)
for i in range(4):
    for j in range(4):
        image_data = requests.get(thumbnail_urls[i+4*j])
        image_data.raise_for_status()
        image = Image.open(BytesIO(image_data.content))        
        axes[i][j].imshow(image)
        axes[i][j].axis("off")


# In[ ]:





# In[ ]:




