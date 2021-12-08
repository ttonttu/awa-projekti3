from google.cloud import storage

def create_indexpage(request):
    """picks the interesting bits from the request and saves them into the bucket as index.html"""
    text = request["teksti"]
    picture = request["kuva"]
    
    indexpage = "<h1>{}</h1>\n<center><img src={}></center>".format(text, picture)
    print("index.html written")

    storage_client = storage.Client()
    bucket = storage_client.bucket("pyyttonitesti")
    blob = bucket.blob("index.html")

    blob.upload_from_string(indexpage)
    return f'Success!'

if __name__ == "__main__":
    hep={"teksti": "Dogs sleep for an average of 10 hours per day.", "kuva": "https://random.dog/6edac66e-c0de-4e69-a9d6-b2e6f6f9001b.jpg"}
    create_indexpage(hep)
