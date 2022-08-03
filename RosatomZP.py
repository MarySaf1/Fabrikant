from xml.etree import ElementTree as ET
import random
import uuid
import requests

url = 'https://demo-api.fabrikant.ru/multi-integration/common/fz223_smbo_rosatom'
# headers = {'content-type': 'application/soap+xml'}
headers = {'content-type': 'text/xml'}
body = 'ZP.xml'

PurchaseId = str(random.randint(1 ** 11, 10 ** 11))
EIS_GUID = str(uuid.uuid4())
PurchaseName ='ROSATOM №' + str(random.randint(100, 999))

randomValue = [EIS_GUID, PurchaseId, PurchaseName]

tree = ET.parse('ZP.xml')
root = tree.getroot()
changeElements = ['.//EIS_GUID', './/PurchaseId', './/PurchaseName']


def tag_parsing():
    n = 0
    for i in changeElements:
        for elm in root.findall(i):
            elm.text = randomValue[n]
            tag = elm.text
            # print(elm.text)
        n += 1


tag_parsing()
tree.write('ZP.xml')