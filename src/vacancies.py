class Vacancies:
    all = []

    def __init__(self, data: dict):
        self.id_vac = data["id_vac"]
        self.name_vac = data["name_vac"]
        self.created_at = data["created_at"]
        self.salary_from = data["salary_from"]
        self.salary_to = data["salary_to"]
        self.place = data["place"]
        self.url_vac = data["url_vac"]
        self.employer = data["employer"]
        self.skills = data["skills"]
        self.charge = data["charge"]
        if self.salary_from is None and self.salary_to is None:
            self.salary = 0
        elif self.salary_from and self.salary_to:
            self.salary = max(self.salary_from, self.salary_to)
        elif self.salary_from is None:
            self.salary = self.salary_to
        elif self.salary_to is None:
            self.salary = self.salary_from
        self.all.append(self)

    def __lt__(self, other):
        return self.salary < other.salary

    @classmethod
    def top_n(cls, n: int):
        cls.all.sort(reverse=True)
        return cls.all[:n]

    def __str__(self):
        give_str = f"Вакансия {self.id_vac}\n{self.created_at}\n{self.name_vac}\n{self.url_vac}\n"
        if not self.salary:
            give_str += "З\\П не указана\n"
        elif self.salary_from and self.salary_to:
            give_str += f"зарплата от {self.salary_from} до {self.salary_to}\n"
        elif self.salary_from:
            give_str += f"зарплата от {self.salary_from}\n"
        elif self.salary_to:
            give_str += f"зарплата до {self.salary_to}\n"
        give_str += f"{self.employer}\n{self.place}\n{self.skills}\n{self.charge}"
        return give_str

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.id_vac}')"


if __name__ == '__main__':
    dict_data1 = {'id_vac': 'hh_77236116',
                  'name_vac': 'Junior Python Backend Developer',
                  'created_at': '2023-04-03',
                  'salary_from': 65000,
                  'salary_to': None,
                  'place': 'Санкт-Петербург',
                  'url_vac': 'https://hh.ru/vacancy/77236116',
                  'employer': 'АпТрейдер (UpTrader)',
                  'skills': 'Уверенное знание <highlighttext>python</highlighttext>. Уверенное знание django и DRF. Опыт работы с git. Опыт работы с PostgreSQL и умение писать SQL...',
                  'charge': 'Поддерживать и дополнять функционал CRM.'
                  }
    dict_data2 = {'id_vac': 'hh_77236126',
                  'name_vac': 'Junior Python Backend Developer',
                  'created_at': '2023-04-03',
                  'salary_from': None,
                  'salary_to': 70000,
                  'place': 'Санкт-Петербург',
                  'url_vac': 'https://hh.ru/vacancy/77236116',
                  'employer': 'АпТрейдер (UpTrader)',
                  'skills': 'Уверенное знание <highlighttext>python</highlighttext>. Уверенное знание django и DRF. Опыт работы с git. Опыт работы с PostgreSQL и умение писать SQL...',
                  'charge': 'Поддерживать и дополнять функционал CRM.'
                  }
    dict_data3 = {'id_vac': 'hh_77236136',
                  'name_vac': 'Junior Python Backend Developer',
                  'created_at': '2023-04-03',
                  'salary_from': None,
                  'salary_to': None,
                  'place': 'Санкт-Петербург',
                  'url_vac': 'https://hh.ru/vacancy/77236116',
                  'employer': 'АпТрейдер (UpTrader)',
                  'skills': 'Уверенное знание <highlighttext>python</highlighttext>. Уверенное знание django и DRF. Опыт работы с git. Опыт работы с PostgreSQL и умение писать SQL...',
                  'charge': 'Поддерживать и дополнять функционал CRM.'
                  }
    dict_data4 = {'id_vac': 'hh_77236146',
                  'name_vac': 'Junior Python Backend Developer',
                  'created_at': '2023-04-03',
                  'salary_from': 50000,
                  'salary_to': 60000,
                  'place': 'Санкт-Петербург',
                  'url_vac': 'https://hh.ru/vacancy/77236116',
                  'employer': 'АпТрейдер (UpTrader)',
                  'skills': 'Уверенное знание <highlighttext>python</highlighttext>. Уверенное знание django и DRF. Опыт работы с git. Опыт работы с PostgreSQL и умение писать SQL...',
                  'charge': 'Поддерживать и дополнять функционал CRM.'
                  }
    vac1 = Vacancies(dict_data1)
    vac2 = Vacancies(dict_data2)
    vac3 = Vacancies(dict_data3)
    vac4 = Vacancies(dict_data4)

    vac_list = Vacancies.all
    print(vac_list)
    for item in vac_list:
        print(item, "\n")
    vac_list.sort()
    print("Сортировка по возрастанию \n")
    for item in vac_list:
        print(item, "\n")
    vac_list.sort(reverse=True)
    print("Сортировка по убыванию \n")
    for item in vac_list:
        print(item, "\n")
    print("ТОП 2 по зарплате \n")
    for item in Vacancies.top_n(2):
        print(item, "\n")

