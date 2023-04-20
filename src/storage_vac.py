import os
import json
from src.vacancies import Vacancies


class StorageJson:
    marked_delete = []
    data_buffer = []

    def __init__(self, file_name="storage_vac.json"):
        self.id = None
        self.file_name = file_name
        self.path = os.path.join('data', self.file_name)

    @staticmethod
    def to_json(vac_obj):
        result = {"id_vac": vac_obj.id_vac, "name_vac": vac_obj.name_vac, "created_at": vac_obj.created_at,
                  "salary_from": vac_obj.salary_from, "salary_to": vac_obj.salary_to, "place": vac_obj.place,
                  "url_vac": vac_obj.url_vac, "employer": vac_obj.employer, "skills": vac_obj.skills,
                  "charge": vac_obj.charge, "salary": vac_obj.salary}
        return result

    def update(self, new_data: list):
        pass

    def load_vac(self, keywords: str):

        """
        Функция получает данные из файла operations.json в корне проекта и отбрасывает пустые словари
        :return: Список операций в виде списка словарей
        """
        result = []
        with open(self.path, 'rt', encoding='utf-8') as data_file:
            for item in json.loads("".join(data_file.readlines())):
                if item:
                    result.append(item)

        return result

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

    # Data to be written
    dictionary = [StorageJson.to_json(item) for item in Vacancies.all]

    # Serializing json
    json_object = json.dumps(dictionary, ensure_ascii=False, indent=4)
    print('Данные в JSON формате')
    print(json_object)

    with open('Serializing_json.json', 'w', encoding="utf-8") as file:
        json.dump(json_object, file, ensure_ascii=False, sort_keys=False, indent=2)

    with open('Serializing_json.json', 'rt', encoding="utf-8") as file:
        loaded_data = json.load(file)
        print(loaded_data)
