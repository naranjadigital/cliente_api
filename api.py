import requests


def get_llamada_basica(url):
    r = requests.get(url)
    print(r.status_code)
    print(r.json())


def get_llamada_autenticacion_basica(url, user, password):
    r = requests.get(url, auth=(user, password))
    print(r.status_code)
    print(r.json())


def post_insertar_distrito(url, nombre):
    r = requests.post(url, data={'nombre':nombre, 'id':3})
    print(r.status_code)
    print(r.json())


def put_update_distrito(url, nombre, user, password):
    r = requests.put(url, data={'nombre':nombre}, auth=(user, password))
    print(r.status_code)
    print(r.json())


def del_eliminar_distrito(url, user, password):
    r = requests.delete(url, auth=(user, password))
    print(r.status_code)


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


post_insertar_distrito('http://127.0.0.1:8000/api/v1/distrito/', 'Lima')
post_insertar_distrito('http://127.0.0.1:8000/api/v1/distrito/', 'Los Olivos')
post_insertar_distrito('http://127.0.0.1:8000/api/v1/distrito/', 'Lince')
put_update_distrito('http://127.0.0.1:8000/api/v1/distrito/2', 'Cambio', 'alumno', 'Demo-1234')
del_eliminar_distrito('http://127.0.0.1:8000/api/v1/distrito/1', 'alumno', 'Demo-1234')

get_llamada_basica('http://127.0.0.1:8000/api/v1/distrito/')



#get_llamada_basica('http://127.0.0.1:8000/api/v1/motel/')
#get_llamada_autenticacion_basica('http://127.0.0.1:8000/api/v1/distrito/1', 'alumno', 'Demo-1234')
#get_llamada_autenticacion_token('http://127.0.0.1:8000/api/v1/motel/1', 'http://127.0.0.1:8000/api-token-auth/', 'alumno', 'Demo-1234')