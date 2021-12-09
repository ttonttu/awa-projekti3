"""into requirements.txt
google-cloud-storage>=1.43.0"""

from google.cloud import storage
import json
import os

def create_indexpage(request):
    """picks the interesting bits from the request and saves them into the bucket as index.html"""
    
    # the bucket name shall be set as environmental variable when creating the function
    bucketname = os.getenv("CLOUDBUCKET")
    
    request_json = request.get_json(silent=True)

    # turns the json object into a dictionary (in which the key is a 2-part tuple) and sets the variables
    data = request_json.get("input")
    text = data[0]
    picture = data[1]
    
    indexpage = "<h1>{}</h1>\n<center><img src={} width='600'></center>".format(text, picture)
    print("index.html written")

    # saves the index.html into the cloud bucket
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucketname)
    blob = bucket.blob("index.html")

    blob.upload_from_string(indexpage)