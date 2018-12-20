import requests


def get_llamada_basica(url):
    r = requests.get(url)
    print(r.status_code)
    print(r.json())


def get_llamada_autenticacion_basica(url, user, password):
    r = requests.get(url, auth=(user, password))
    print(r.status_code)
    print(r.json())


def get_llamada_autenticacion_token(url, urltoken, user, password):

    r = requests.post(urltoken, data={'username':user,'password':password})
    print(r.status_code)
    print(r.json())
    json = r.json()
    token = json['token']

    HEADERS = {'Authorization': 'token {0}'.format(token)}
    r2 = requests.get(url, headers=HEADERS)

    print(r2.status_code)
    print(r2.json())


get_llamada_basica('http://127.0.0.1:8000/api/v1/motel/')
get_llamada_autenticacion_basica('http://127.0.0.1:8000/api/v1/distrito/1', 'alumno', 'Demo-1234')
get_llamada_autenticacion_token('http://127.0.0.1:8000/api/v1/motel/1', 'http://127.0.0.1:8000/api-token-auth/', 'alumno', 'Demo-1234')