import requests
import json


header = {'content-type': 'application/json'}
params = {'firstname': 'Ryan', 'lastname': 'Mitchell'}
r = requests.post("http://pythonscraping.com/files/processing.php",
                  datajson.dumps(params), headers=header)
print(r)
