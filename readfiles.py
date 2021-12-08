"""into requirements.txt 
pytest==5.4.2
python-dotenv==0.17.1
google-cloud-storage==1.43.0
flask>=2.0.0"""

import json
import urllib.request
from  google.cloud import storage
from flask import jsonify

def avaa_tiedostot(request):
    tiedosto = urllib.request.urlopen("https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number=1")
    tiedot_data = json.loads(tiedosto.read())
    parametri_data_teksti = ""
    for d in sorted(tiedot_data, key=lambda x: x['fact']):
        parametri_data_teksti += d['fact']
        
    tiedosto = urllib.request.urlopen("https://random.dog/woof.json")
    tiedot_data = json.loads(tiedosto.read())
    parametri_data_kuva = tiedot_data['url']
    output = {"teksti":parametri_data_teksti, "kuva":parametri_data_kuva}
    json_object = jsonify(output)
    return json_object