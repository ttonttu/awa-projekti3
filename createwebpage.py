"""into requirements.txt
google-cloud-storage>=1.43.0"""

from google.cloud import storage
import json

def create_indexpage(request):
    """picks the interesting bits from the request and saves them into the bucket as index.html"""
    request_json = request.get_json(silent=True)
    
    text = request_json.get("teksti")
    picture = request_json.get("kuva")
    
    indexpage = "<h1>{}</h1>\n<center><img src={}></center>".format(text, picture)
    print("index.html written")

    storage_client = storage.Client()
    bucket = storage_client.bucket("pyyttonitesti")
    blob = bucket.blob("index.html")

    blob.upload_from_string(indexpage)
    return f'Success!'