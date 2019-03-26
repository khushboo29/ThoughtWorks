import requests
import json
import datetime

class RestTemplate:
    host_url = 'https://http-hunt.thoughtworks-labs.net/'
    get_headers = {'userId': '9p7rYUAQs'}
    post_headers = {'userId': '9p7rYUAQs','content-type':'application/json'}
    
    def getRequest(self,url, isUrlFull=False):
        uri = self.makeUrl(url, isUrlFull)
        response = requests.get(uri, headers=self.get_headers)
        response_json = response.json()
        return response_json

    def postRequest(self,url, payload, isUrlFull=False):
        uri = self.makeUrl(url, isUrlFull)
        response = requests.post(uri, headers=self.post_headers, data=payload)
        response_json = response.json()
        return response_json

    def makeUrl(self,url, isUrlFull):
        return url if isUrlFull else self.getDefaultUrl(url)
    
    def getDefaultUrl(self,suffix):
        return self.host_url + suffix

    def activeProduct(self,startDate,endDate):
        todaysDate = '2019-03-27'
        if startDate <= todaysDate:
            if (endDate == None or endDate >= todaysDate):
                return True
        else:
            return False

#res = RestTemplate().getRequest('challenge')
#print(res)

res = RestTemplate().getRequest('challenge/input')
print(res)

'''
#challemge 1
#count = len(res['sampleInput']['input']) #for testing
count = len(res)

output_obj = dict()
output_obj['output'] = {'count':count}
output_json = json.dumps(output_obj)

resp = RestTemplate().postRequest('challenge/output',output_json)
print(resp)
'''

'''
#challenge 2
count=0
for item in res:
    isActive = RestTemplate().activeProduct(item['startDate'],item['endDate'])
    if isActive :
        count +=1
        
#print(count)

output_obj = dict()
output_obj['output'] = {'count':count}
output_json = json.dumps(output_obj)

resp = RestTemplate().postRequest('challenge/output',output_json)
print(resp)
'''   
''' 
#challenge 3
activeCategories = {}
for item in res:
    isActive = RestTemplate().activeProduct(item['startDate'],item['endDate'])
    if isActive :
        cat = item['category']
        if cat in activeCategories:
            activeCategories[cat] +=1
        else:
            activeCategories[cat]=1

output_obj = dict()
output_obj['output'] = activeCategories
output_json = json.dumps(output_obj)
print(output_json)

resp = RestTemplate().postRequest('challenge/output',output_json)
print(resp)

'''
#challenge 4
total=0
for item in res:
    isActive = RestTemplate().activeProduct(item['startDate'],item['endDate'])
    if isActive :
        total +=item['price']

#print(total)

output_obj = dict()
output_obj['output'] = {'totalValue':total}
output_json = json.dumps(output_obj)

resp = RestTemplate().postRequest('challenge/output',output_json)
print(resp)
