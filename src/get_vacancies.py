import requests
from abstract_classes import GetVacancies


class HHVacancies(GetVacancies):

    def __init__(self):
        self.url: str = "https://api.hh.ru/vacancies"
        self.params_dict: dict = {"text": "", "search_field": [], "per_page": 20, "period": 1}
        self.search_fields: list = ["name", "company_name", "description"]
        self.headers: str = ""
        self.params: dict = self.params_dict
        self.response: int = 0
        self.__vacancies: dict = {}
        self.base = "hh"

    def set_params(self, key: str, value: str | int) -> None:
        if key == "text":
            self.params_dict["text"] += value
        elif key == "search_field":
            for i in range(3):
                self.params_dict["search_field"] = []
                if value[i] == "1":
                    self.params_dict["search_field"].append(value)
        elif key == "per_page":
            self.params_dict["per_page"] = value
        elif key == "period":
            self.params_dict["period"] = value
        else:
            print(f"Неверный параметр {key}")

    def reset_params(self):
        self.params_dict = {"text": "", "search_field": [], "per_page": 20, "period": 1}

    def set_headers(self):
        pass

    def get_vacancies(self) -> None:
        response = requests.get(self.url, headers=self.headers, params=self.params)
        self.response = response.status_code
        self.__vacancies = response.json()["items"]

    def display_vacancies(self):
        for item in self.__vacancies:
            print(item)

    def provide_vacancies(self):
        result = []
        if self.response == 200 and self.__vacancies:
            for item in self.__vacancies:
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
        return result


class SJVacancies(GetVacancies):
    def set_params(self):
        pass

    def set_headers(self):
        pass

    def get_vacancies(self):
        pass


if __name__ == '__main__':
    while True:
        hh_vac = HHVacancies()
        print(f"""Текущее значение параметра запроса -
        "Слова для поиска": {hh_vac.params_dict["text"]},
        "Список полей для поиска": {hh_vac.params_dict["search_field"]},
        "Количество вакансий": {hh_vac.params_dict["per_page"]},
        "За сколько дней": {hh_vac.params_dict["period"]}
        """)
        x = input("Введите параметр запроса")
        if x == "":
            break

    hh_vac.get_vacancies()
    if hh_vac.response == 200:
        hh_vac.display_vacancies()
        vacancies = hh_vac.provide_vacancies()
        total_vac = 0

        for vacancy in vacancies:
            total_vac += 1
            for k, v in vacancy.items():
                print(k, v)
            # print(vacancy["id"])
            # print(vacancy["alternate_url"])
            # print(vacancy["employer"]["name"])
            # print(vacancy["name"])
            # print(vacancy["created_at"])

        print(f'Всего вакансий HH: {total_vac}')
    else:
        print(f"Ошибка запроса к {hh_vac.url} - {hh_vac.response}")
