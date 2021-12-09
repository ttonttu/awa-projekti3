import json
import urllib.request
from  google.cloud import storage
from flask import jsonify

def avaa_tiedostot():
    
    tiedosto = urllib.request.urlopen("https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number=1")
    tiedot_data = json.loads(tiedosto.read())
    parametri_data_teksti = []
    for d in sorted(tiedot_data, key=lambda x: x['fact']):
        parametri_data_teksti.append(d["fact"])
    
    
    tiedosto = urllib.request.urlopen("https://random.dog/woof.json")
    tiedot_data = json.loads(tiedosto.read())
    parametri_data_kuva = tiedot_data['url']
    output = {"teksti":parametri_data_teksti, "kuva":parametri_data_kuva}
    return jsonify(output)

if __name__ == "__main__":
    tulos = avaa_tiedostot()
    print(tulos)