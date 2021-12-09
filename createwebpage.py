from google.cloud import storage


def create_indexpage(blob_text, blob_picture):
    indexpage = f"<h1>{blob_text}</h1>\n<center><img src={blob_picture}></center>"
    print("index.html written")

    bucket_name = 'dev-ampari-1a'
    destination_blob_name = 'index.html'

    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_string(indexpage)

    return f'Success!'