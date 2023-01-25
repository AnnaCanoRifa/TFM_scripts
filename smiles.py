import requests

from urllib.request import urlopen
from urllib.parse import quote


def CIRconvert(ids):
    try:
        url = 'http://cactus.nci.nih.gov/chemical/structure/' + quote(ids) + '/smiles'
        ans = urlopen(url).read().decode('utf8')
        return ans
    except:
        return 'Did not work'


QUERY_URL = 'http://sabiork.h-its.org/sabioRestWebServices/searchReactionParticipants'


# input: SabioReactionID
# valid output fields: "fields[]":["Name","Role","SabioCompoundID","ChebiID","PubChemID","KeggCompoundID", "InChI","Smiles"]

# example
query = {"SabioReactionID":"1", "fields[]":["Name", "Role", "Smiles", "ECNumber]}

# note that you can also retrieve the data for ALL reaction participants by performing a wildcard search
# for this wildcard query, the output field 'SabioReactionID' is added by default
# query = {"SabioReactionID":"*", "fields[]":["SabioCompoundID","Name","Role"]}

request = requests.get(QUERY_URL, params = query)
request.raise_for_status()

# results


fh=open("fitxerssmiles.csv", "w")

fh.write(request.text)


quit()
print(request.text)
identifiers = request.text.split('\n')
print(identifiers)
quit()
for ids in identifiers :
    print(ids, CIRconvert(ids))