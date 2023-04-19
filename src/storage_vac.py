import os
from src.vacancies import Vacancies


class StorageJson:
    marked_delete = []

    def __init__(self, file_name="storage_vac.json"):
        self.id = None
        self.file_name = file_name
        self.path = os.path.join('data', self.file_name)

    def update(self, new_data: list):
        pass

    def load(self, keywords: str):
        pass

    def mark_del(self):
        pass

    def del_marked(self):
        pass

    def del_all(self):
        pass


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
