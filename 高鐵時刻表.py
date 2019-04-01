import requests
import json

url = 'http://www.thsrc.com.tw/tw/TimeTable/Search'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)                         Chrome/73.0.3683.86 Safari/537.36'
}

form_data = {
    'StartStationName':'南港站',
    'EndStationName':'台南站',
    'SearchType':'S',
    'StartStation':'2f940836-cedc-41ef-8e28-c2336ac8fe68',
    'EndStation':'9c5ac6ca-ec89-48f8-aab0-41b738cb1814',
    'DepartueSearchDate':'2019/04/02',
    'DepartueSearchTime':'09:00',
    'DepartueTrainCode':'',
    'DestinationSearchDate':'',
    'DestinationSearchTime':'',
    'DiscountType':''
}

res = requests.post(url, headers=headers, data=form_data)

jsdata = res.json()

#print(jsdata['data'])

