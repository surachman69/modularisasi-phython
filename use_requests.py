import requests

url='https://detik.com'
try :
     response =requests .get(url)
     print(f'sukses {response}')
     print(f'content{response.text}')
except Exception as e:
    print('there is an error',e)
print('program ended')