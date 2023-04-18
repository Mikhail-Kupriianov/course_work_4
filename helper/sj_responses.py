import requests
from datetime import datetime

"""Модуль демонстрирует доступ к вакансиям на SuperJob"""

# Переменная с url адресом сервиса для списка вакансий
url_sj = "	https://api.superjob.ru/2.0/vacancies/"

# Параметр "count" - Количество результатов поиска. Может быть от 1 до 100. По умолчанию значение - 20
# "keyword": "python программист",
# "keywords": [{"srws": 1, "skwc": "or", "keys": "python"},
#                  {"srws": 3, "skwc": "or", "keys": " программист"}],
# srws	int	Да	Что искать (в каком текстовом блоке вакансии искать).
# Список возможных значений:
#   1 — должность
#   2 — название компании
#   3 — должностные обязанности
#   4 — требования к квалификации
#   5 — условия работы
#   10 — весь текст вакансии
sj_params = [
    ("keywords", [("srws", 1), ("skwc", "particular"), ("keys", "Инженер-программист")]),
    ("keywords", [("srws", 1), ("skwc", "particular"), ("keys", "АСУ")]),
    ("keywords", [("srws", 2), ("skwc", "particular"), ("keys", "Мираторг")]),
    ("period", 0),
    ("count", 10)
]

key = {
    "X-Api-App-Id": "v3.r.137477023.b5c750054712a5efe77fcd597e716d270b064aed.7a86819e391d1c559f0c04057a3da02a467b68c9"}

sj_response = requests.get(url_sj, headers=key, params=sj_params)

# print(sj_response.status_code)

if sj_response.status_code == 200:

    vacancies = sj_response.json()  # ['objects']

    # print(vacancies)

    total_vac = 0

    # for key, val in vacancies.items():
    #     print(f"Ключ - {key} : Значение {val}")

    for sj_object in vacancies['objects']:
        total_vac += 1
        print(sj_object['firm_name'], sj_object['profession'], sj_object['town']['title'], sj_object['link'])
        print('*' * 25)
        print("Вакансия", sj_object['id'])
        print("Закрыта", sj_object['is_closed'])
        print(datetime.fromtimestamp(int(sj_object['date_published'])))
        print(sj_object['link'])
        print(sj_object['firm_name'])
        print(sj_object['profession'])
        print(sj_object['town']['title'])
        print(f"Зарплата от {sj_object['payment_from']} до {sj_object['payment_to']} "
              f"{sj_object['currency']}")
        print(sj_object['candidat'])
        print('=' * 25)
    print(f'Всего вакансий SupeJob: {total_vac}')

    # print("Вакансия", vacancies['objects'][0]['id'])
    # print("Закрыта", vacancies['objects'][0]['is_closed'])
    # print(vacancies['objects'][0]['link'])
    # print(vacancies['objects'][0]['firm_name'])
    # print(vacancies['objects'][0]['profession'])
    # print(vacancies['objects'][0]['town']['title'])
    # print(f"Зарплата от {vacancies['objects'][0]['payment_from']} до {vacancies['objects'][0]['payment_to']} "
    #       f"{vacancies['objects'][0]['currency']}")
    # print(vacancies['objects'][0]['candidat'])

else:
    print("Error:", sj_response.status_code)
