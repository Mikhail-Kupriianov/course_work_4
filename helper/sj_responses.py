import os

import requests
from datetime import datetime

"""Модуль демонстрирует доступ к вакансиям на SuperJob"""

# Переменная с url адресом сервиса для списка вакансий
url_sj = "	https://api.superjob.ru/2.0/vacancies/"

# Параметры передаются в виде списка кортежей
# ("count", 12) - количество результатов поиска. Может быть от 1 до 100. По умолчанию значение - 20
# ("period", 0) int - период публикации
# Список возможных значений:
#   1 — 24 часа
#   3 — 3 дня
#   7 — неделя
#   0 — за всё время
# ("keyword", "python программист") слово(а) для поиска по всем полям вакансии
# ("keywords", [("srws", 1), ("skwc", "particular"), ("keys", "Инженер-программист")])

# srws	int	- в каком поле вакансии искать
# Список возможных значений:
#   1 — должность !!!
#   2 — название компании !!!
#   3 — должностные обязанности !!!
#   4 — требования к квалификации
#   5 — условия работы
#   10 — весь текст вакансии
#
# skwc	string - как искать
# Список возможных значений:
#   and — все слова
#   or — хотя бы одно слово
#   particular — точную фразу
#   nein — слова-исключения
#
# keys str - ключевое слово
sj_params = [
    ("keywords", [("srws", 1), ("skwc", "particular"), ("keys", "Сервисный инженер направления по поддержке, ремонту печатающей и организационной техники")]),
    # ("keywords", [("srws", 1), ("skwc", "particular"), ("keys", "АСУ")]),
    #  ("keywords", [("srws", 2), ("skwc", "particular"), ("keys", "Мираторг")]),
    # ("period", 1),
    ("count", 5),
    ("count", 50),
    ("count", 100)
]

key = {os.environ.get('API_KEY_SJ').split(": ")[0]: os.environ.get('API_KEY_SJ').split(": ")[1]}

sj_response = requests.get(url_sj, headers=key, params=sj_params)

# print(sj_response.status_code)

if sj_response.status_code == 200:

    vacancies = sj_response.json()  # ['objects']

    print(vacancies)
    input("pause")

    total_vac = 0

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

else:
    print("Error:", sj_response.status_code)
