from xml.etree import ElementTree as ET
import random
import uuid
import requests
import datetime as dt
from datetime import timedelta

url = 'https://demo-api.fabrikant.ru/multi-integration/common/fz223_smbo_rosatom'

# генерация рандомных данных и занесение в список
PurchaseId = str(random.randint(1 ** 11, 10 ** 11))
EIS_GUID = str(uuid.uuid4())
PurchaseName = 'ROSATOM №' + str(random.randint(100, 999))
randomValue = [EIS_GUID, PurchaseId, PurchaseName]

# парсинг xml и занесение в список изменяемых тегов
tree = ET.parse('EA.xml')
root = tree.getroot()
changeElements = ['.//EIS_GUID', './/PurchaseId', './/PurchaseName']
forEIStag = []


# Замена значение тегов на уникальные
def tag_parsing():
    n = 0
    for i in changeElements:
        for elm in root.findall(i):
            elm.text = randomValue[n]
            forEIStag.append(elm.text)
        n += 1


tag_parsing()

# Запись нового извещения в xml-файл и занесение в переменную для отправки на шлюз
tree.write('EA.xml')

with open('EA.xml') as inputFile:
    xml_file = inputFile.read()
response = requests.post(url, data=xml_file)
print(response.content.decode('utf-8'))

# генерация дат для пакета в ЕИС и занесение в список
dateNow = (dt.datetime.now())
dateNowFormat = dateNow.replace(microsecond=0).isoformat(sep='T')
dateFirst = (dateNow + timedelta(days=5)).replace(microsecond=0).isoformat(sep='T')
dateSecond = (dateNow + timedelta(days=8)).replace(microsecond=0).isoformat(sep='T')
dateThird = (dateNow + timedelta(days=10)).replace(microsecond=0).isoformat(sep='T')

valueEIS = [forEIStag[0], forEIStag[0], forEIStag[1], forEIStag[2], dateNowFormat, dateNowFormat, dateNowFormat,
            dateThird, dateFirst, dateNowFormat, dateSecond]

# парсинг xml для ручного импорта  и занесение в список изменяемых тегов
treeEIS = ET.parse('EAEIS.xml')
rootEIS = treeEIS.getroot()

changeElementsEIS = ['.//{http://zakupki.gov.ru/223fz/types/1}guid',
                     './/{http://zakupki.gov.ru/223fz/purchase/1}guid',
                     './/{http://zakupki.gov.ru/223fz/purchase/1}registrationNumber',
                     './/{http://zakupki.gov.ru/223fz/purchase/1}name',
                     './/{http://zakupki.gov.ru/223fz/purchase/1}createDateTime',
                     './/{http://zakupki.gov.ru/223fz/purchase/1}publicationDateTime',
                     './/{http://zakupki.gov.ru/223fz/purchase/1}applSubmisionStartDate',
                     './/{http://zakupki.gov.ru/223fz/purchase/1}summingupDateTime',
                     './/{http://zakupki.gov.ru/223fz/purchase/1}submissionCloseDateTime',
                     './/{http://zakupki.gov.ru/223fz/purchase/1}publicationPlannedDate',
                     './/{http://zakupki.gov.ru/223fz/types/1}date']


def tag_parsingEIS():
    n = 0
    for m in changeElementsEIS:
        for elem in rootEIS.findall(m):
            elem.text = valueEIS[n]
        n += 1


tag_parsingEIS()

# Запись нового извещения в xml-файл и занесение в переменную для отправки на в ЕИС
treeEIS.write('EAEIS.xml')
