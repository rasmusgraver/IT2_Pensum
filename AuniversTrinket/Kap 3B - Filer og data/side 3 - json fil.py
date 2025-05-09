import json

filnavn = "skandinavia.json"

with open(filnavn, encoding="utf-8") as fil:
  data = json.load(fil)

print(data)


########################

import json

filnavn = "lonnstabell.json"

with open(filnavn, encoding="utf-8") as f:
  data = json.load(f)

print(data)

########################


