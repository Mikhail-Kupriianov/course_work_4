import requests
"""Модуль демонстрирует доступ к вакансиям на HeadHaunter и SuperJob сервисах"""

# Переменные с url адресами сервисов для списка вакансий
url_hh = "https://api.hh.ru/vacancies"
url_sj = "	https://api.superjob.ru/2.0/vacancies/"

# Параметры для запроса
# "text" - фильтр для отбора вакансий
# "per_page" - количество возвращаемых вакансий
hh_params = {
    "text": "python",
    "per_page": 1
}

# Параметр "page" - Номер страницы результата поиска. Может быть от 0 до 500.	По умолчанию значение - 0.
# Параметр "count" - Количество результатов на страницу поиска. Может быть от 1 до 100. По умолчанию значение - 20.
# Максимальное количество сущностей, выдаваемых API равно 500.
# Это значит, например, при поиске резюме по 100 резюме на страницу, всего можно просмотреть 5 страниц.
sj_params = {
    "page": 0,
    "count": 1
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

    vacancies = sj_response.json()  # ['objects']

    print(vacancies)

    total_vac = 0

    for key, val in vacancies.items():
        print(f"Ключ - {key} : Значение {val}")

    for sj_object in vacancies['objects']:
        total_vac += 1
        print(sj_object['firm_name'], sj_object['profession'], sj_object['town']['title'])
    print(f'Всего вакансий: {total_vac}')

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
