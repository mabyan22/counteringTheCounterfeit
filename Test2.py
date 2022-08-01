import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = "397e47df3ec6469e9f6244f8453ed6c7"
service_url = "https://www.newsapi.org/v2/everything?"

# Ignore SSL certificate errors
#ssl._create_default_https_context=ssl._create_unverified_context

search_str=str(input("Enter search string: "))
parms = dict()
parms["q"]= search_str
parms['key']=api_key
url = service_url + urllib.parse.urlencode(parms)
def main():
    context = ssl._create_unverified_context()
    r = urllib.request.urlopen(url, context=context)
    print(r.status)
    print(r)


if __name__ == '__main__':
    main()

#print('Retrieving', url)
#uh = urllib.request.urlopen(url)
data = uh.read().decode()
Print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(data)
else:
    print("Total results: ", js["totalResults"])
    number1=[]*7
    #number1=[name,author,title,description,url,urlToImage,publishedAt]
    number1[0]=js["articles"][0]["source"]["name"]
    number1[1]=js["articles"][0]["author"]
    number1[2]=js["articles"][0]["title"]
    number1[3]=js["articles"][0]["description"]
    number1[4]=js["articles"][0]["url"]
    number1[5]=js["articles"][0]["urlToImage"]
    number1[6]=js["articles"][0]["publishedAt"]

print(number1)
