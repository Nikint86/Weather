import requests


def weather(city):
    payload = {"n": "",
           "T": "",
           "q": "",
           "m": "",
           "M": "",
           "lang": "ru"}
    adress_global = 'https://wttr.in/{}'
    url = adress_global.format(city)
    response = requests.get(url, params=payload)
    return response.text
if __name__ == '__main__':
    adress_local = ['svo','Париж','Череповец']
    for city in adress_local:
        print(weather(city))
