import os
from datetime import datetime

import requests

from abstract_classes import GetVacancies


class HHVacancies(GetVacancies):

    def __init__(self):
        self.url: str = "https://api.hh.ru/vacancies"
        self.params: dict = {"text": "", "search_field": [], "per_page": 20, "period": 1}
        self.search_fields: list = ["name", "company_name", "description"]
        self.headers: str = ""
        self.response: int = 0
        self.__vacancies: list = []
        self.base = "hh"

    def set_params(self, key: str, value: str | int) -> None:
        if key == "text":
            self.params["text"] = value
        # key search_field должен приходить в виде трёхсимвольной строки из цифр 1 или ноль - "101"
        # позиции единиц добавляют соответсвующее поле поиска из словаря self.search_fields:
        # ["name", "company_name", "description"]
        elif key == "search_field":
            for i in range(3):
                self.params["search_field"] = []
                if value[i] == "1":
                    self.params["search_field"].append(self.search_fields[i])
        elif key == "per_page":
            self.params["per_page"] = value
        elif key == "period":
            self.params["period"] = value
        else:
            print(f"Неверный параметр {key}")

    def reset_params(self):
        self.params = {"text": "", "search_field": [], "per_page": 20, "period": 1}

    def set_headers(self):
        pass

    def get_vacancies(self) -> None:
        response = requests.get(self.url, headers=self.headers, params=self.params)
        self.response = response.status_code
        self.__vacancies = response.json()["items"]

    def display_vacancies(self):
        for item in self.__vacancies:
            print(item)

    def provide_vacancies(self) -> list:
        result = []

        if self.response == 200 and self.__vacancies:
            for vac in self.__vacancies:

                for item in vac:
                    if item["salary"]:
                        salary_from = item["salary"]["from"]
                        salary_to = item["salary"]["to"]
                    else:
                        salary_from = None
                        salary_to = None
                    result.append({
                        "id_vac": "hh_" + item["id"],
                        "name_vac": item["name"],
                        "created_at": item["created_at"][:10],
                        "salary_from": salary_from,
                        "salary_to": salary_to,
                        "place": item["area"]["name"],
                        "url_vac": item["alternate_url"],
                        "employer": item["employer"]["name"],
                        "skills": item["snippet"]["requirement"],
                        "charge": item["snippet"]["responsibility"]
                    })
        else:
            print("Нет вакансий по результатам запроса")
        return result


class SJVacancies(GetVacancies):
    secret_key = {os.environ.get('API_KEY_SJ').split(": ")[0]: os.environ.get('API_KEY_SJ').split(": ")[1]}

    def __init__(self):
        self.url: str = "https://api.superjob.ru/2.0/vacancies/"
        self.params: list = []
        self.search_fields: list = [1, 2, 3]
        self.headers: dict = self.secret_key
        self.response: int = 0  #
        self.__vacancies: list = []  #
        self.base = "sj"  #

    def set_params(self, key: str, value: str | int):
        if key == "period" or key == "count":
            self.params.append((key, value))

        # value для key "keywords" должна приходить в виде строки "1=Инженер-программист",
        # где цифра означает поле для поиска
        # 1 — должность, 2 — название компании, 3 — должностные обязанности
        elif key == "keywords":
            if value.split("=")[0] in ("1", "2", "3"):
                self.params.append(("keywords", [("srws", value.split("=")[0]), ("skwc", "particular"),
                                                 ("keys", value.split("=")[1])]))

        else:
            print(f"Неверный параметр {key}")

    def reset_params(self):
        self.params = []

    def set_headers(self):
        self.headers = self.secret_key

    def get_vacancies(self):
        response = requests.get(self.url, headers=self.headers, params=self.params)
        self.response = response.status_code
        self.__vacancies = response.json()['objects']

    def display_vacancies(self):
        for item in self.__vacancies:
            print(item)

    def provide_vacancies(self) -> list:
        result = []

        if self.response == 200 and self.__vacancies:
            for vac in self.__vacancies:

                for item in vac:
                    if item["payment_from"]:
                        salary_from = item["payment_from"]
                    else:
                        salary_from = None
                    if item["payment_to"]:
                        salary_to = item["salary"]
                    else:
                        salary_to = None
                    result.append({
                        "id_vac": "sj_" + item["id"],
                        "name_vac": item["profession"],
                        "created_at": datetime.fromtimestamp(item["date_published"]).isoformat()[:10],
                        "salary_from": salary_from,
                        "salary_to": salary_to,
                        "place": item["town"]["title"],
                        "url_vac": item["link"],
                        "employer": item["firm_name"],
                        "skills": item["candidat"],
                        "charge": ""
                    })
        else:
            print("Нет вакансий по результатам запроса")
        return result


if __name__ == '__main__':
    pass
