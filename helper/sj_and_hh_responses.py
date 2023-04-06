import requests

url_hh = "https://api.hh.ru/vacancies"
url_sj = "	https://api.superjob.ru/2.0/vacancies/"

hh_params = {
    "text": "python",
    "per_page": 1
}
sj_params = {
    "count": 0
}

key = {
    "X-Api-App-Id": "v3.r.137477023.b5c750054712a5efe77fcd597e716d270b064aed.7a86819e391d1c559f0c04057a3da02a467b68c9"}

response = requests.get(url_hh, params=hh_params)

if response.status_code == 200:
    vacancies = response.json()["items"]
    for vacancy in vacancies:
        # print(vacancy)
        print(vacancy["id"])
        print(vacancy["type"]["name"])
        print(vacancy["alternate_url"])
        print(vacancy["employer"]["name"])
        print(vacancy["name"])
        print(vacancy["area"]["name"])
        print(f'Зарплата от {vacancy["salary"]["from"]} до {vacancy["salary"]["to"]} {vacancy["salary"]["currency"]}'
              f' на руки - {vacancy["salary"]["gross"]}')
        print(vacancy["snippet"]["responsibility"])
        print(vacancy["snippet"]["requirement"])
else:
    print("Error:", response.status_code)

sj_response = requests.get(url_sj, headers=key, params=sj_params)

print(sj_response.status_code)

if sj_response.status_code == 200:
    print("успешно")
    vacancies = sj_response.json()
    print("Вакансия", vacancies['objects'][0]['id'])
    print("Закрыта", vacancies['objects'][0]['is_closed'])
    print(vacancies['objects'][0]['link'])
    print(vacancies['objects'][0]['firm_name'])
    print(vacancies['objects'][0]['profession'])
    print(vacancies['objects'][0]['town']['title'])
    print(f"Зарплата от {vacancies['objects'][0]['payment_from']} до {vacancies['objects'][0]['payment_to']} "
          f"{vacancies['objects'][0]['currency']}")
    print(vacancies['objects'][0]['candidat'])

else:
    print("Error:", sj_response.status_code)
