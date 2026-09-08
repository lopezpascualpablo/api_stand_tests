import configuration
import requests
import data
import json

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)
response = get_docs()
print(response.status_code)

def ger_reibir_sabores():
    return requests.get(configuration.URL_SERVICE + configuration.PRODUCTS_SAB_PATH,
                        params={"name": "Sabores de París"})
response = ger_reibir_sabores()
print("URL enviada:", response.url)
print("Status code:", response.status_code)
print(json.dumps(response.json(),
    indent=4,
    ensure_ascii=False
))

def get_logs():

    return (requests.get
            (configuration.URL_SERVICE +
             configuration.LOG_MAIN_PATH,
             params={"count": 20}))
respose = get_logs()
print(respose.status_code)
print(response.headers)

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)
response = get_users_table()
print(response.status_code)

def post_new_user(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json = body,
                         headers= data.headers)
if __name__ == "__main__":
    response = post_new_user(data.user_body)
    print("URL enviada:", response.url)
    print("Status code:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type"))
    print("Respuesta:")
    print(response.text)
try:
    print(response.json())
except requests.exceptions.JSONDecodeError:
    print("La respuesta no contiene JSON válido.")

def post_products_kits(body):
    return  requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                          json=body,
                          headers= data.headers)
response = post_products_kits(data.product_ids)
print("URL enviada:", response.url)
print("Content-Type:", response.headers.get("Content-Type"))
print("Status code:", response.status_code)
#print(response.json())

print(json.dumps(
    response.json(),
    indent=4,
    ensure_ascii=False
))



