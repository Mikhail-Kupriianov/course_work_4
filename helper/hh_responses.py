import requests

"""Модуль демонстрирует доступ к вакансиям на HeadHaunter"""

# Переменная с url адресом сервиса для списка вакансий
url_hh = "https://api.hh.ru/vacancies"

# Параметры для запроса HH
# Параметр "text" - lst, фильтр для отбора вакансий, каждое поле ищется по всем полям вакансии,
#                                                                                           регистр не имеет значения.
# Параметр "search_field" - если параметр не пустой поиск идет по указанным в нём полям:
#       - "name" в названии вакансии;
#       - "company_name" в названии компании;
#       - "description" в описании вакансии.
# Параметр "per_page" - количество возвращаемых вакансий, по умолчанию 20, максимум 100
# Параметр "period" - период публикации. Если None - все даты.
# "search_field": ["name", "company_name", "description"]
# API запрос по номеру вакансии в браузере https://api.hh.ru/vacancies/79285897/  - 79285897 id вакансии
hh_params = {
    "text": "Python Developer",
    "search_field": ["name"],
    "per_page": 100,
    "period": 200
}

response = requests.get(url_hh, params=hh_params)

if response.status_code == 200:
    vacancies = response.json()["items"]

    total_vac = 0

    for vacancy in vacancies:
        total_vac += 1
        # print(vacancy)
        print(vacancy["id"])
        print(vacancy["type"]["name"])
        print(vacancy["alternate_url"])
        print(vacancy["employer"]["name"])
        print(vacancy["name"])
        print(vacancy["created_at"])
        print(vacancy["area"]["name"])

        if vacancy["salary"]:
            print(
                f'Зарплата от {vacancy["salary"]["from"]} до {vacancy["salary"]["to"]} {vacancy["salary"]["currency"]}')
        else:
            print('з/п не указана')

        print(vacancy["snippet"]["responsibility"])
        print(vacancy["snippet"]["requirement"])
    print(f'Всего вакансий HH: {total_vac}')
else:
    print("Error:", response.status_code)

print(response)


