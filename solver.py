# pip install requests
import requests

response = requests.get('http://51.89.151.134/crapi/viewstats?token=%20Q1FXNEVBgmBJf5Bzd2aEW0qWUV1_VWRHZYdxa0l2YIR7l3VTVnI=&record=200&filternum=261381320168')
print(response.text)