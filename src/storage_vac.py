import os
import json


DATA_PATH = os.path.abspath("..\data")


class StorageJson:
    marked_delete = []
    data_buffer = []

    def __init__(self, file_name="storage_vac.json"):
        self.id = None
        self.file_name = file_name
        self.path = os.path.join(DATA_PATH, self.file_name)
        if not os.path.exists(self.path):
            self.del_all()

    @staticmethod
    def to_dict(vac_obj):
        result = {"id_vac": vac_obj.id_vac, "name_vac": vac_obj.name_vac, "created_at": vac_obj.created_at,
                  "salary_from": vac_obj.salary_from, "salary_to": vac_obj.salary_to, "place": vac_obj.place,
                  "url_vac": vac_obj.url_vac, "employer": vac_obj.employer, "skills": vac_obj.skills,
                  "charge": vac_obj.charge, "salary": vac_obj.salary}
        return result

    def update(self, new_data: list):
        # self.data_buffer = []
        missed = 0
        written = 0
        data_for_add = [self.to_dict(item) for item in new_data]
        self.data_buffer = self.load_vac()

        for vac in data_for_add:
            if vac["id_vac"] not in [x["id_vac"] for x in self.data_buffer]:
                self.data_buffer.append(vac)
                written += 1
            else:
                missed += 1

        with open(self.path, 'w', encoding='utf-8') as data_file:
            json.dump(self.data_buffer, data_file, ensure_ascii=False, indent=4)
        print(f"Записано вакансий - {written}, пропущено (уже есть в файле) - {missed}")

    def load_vac(self, keywords: str = "") -> list:

        """
        Функция получает данные из файла operations.json в корне проекта и отбрасывает пустые словари
        :return: Список операций в виде списка словарей
        """
        result = []
        if keywords:
            with open(self.path, 'rt', encoding='utf-8') as data_file:
                for item in json.load(data_file):
                    for keyword in keywords.split():
                        for item_val in item.values():
                            if keyword.isdigit() and str(item_val).isdigit():
                                if int(keyword) <= item_val:
                                    result.append(item)
                                    break
                            elif keyword.isalpha() and not str(item_val).isdigit() and item_val is not None:
                                if keyword.lower() in item_val.lower():
                                    result.append(item)
        else:
            with open(self.path, 'rt', encoding='utf-8') as data_file:
                result = json.load(data_file)

        return result

    def mark_del(self, id_vac: str):
        for item in id_vac.split():
            self.marked_delete.append(item)

    def clear_marks(self):
        self.marked_delete = []

    def del_marked(self):
        self.data_buffer = []
        file_data = self.load_vac()
        for vac in file_data:
            if vac["id_vac"] not in self.marked_delete:
                self.data_buffer.append(vac)

        with open(self.path, 'w', encoding='utf-8') as data_file:
            json.dump(self.data_buffer, data_file, ensure_ascii=False, sort_keys=False, indent=4)
        self.clear_marks()

    def del_all(self):
        empty_list = []
        with open(self.path, 'w', encoding='utf-8') as data_file:
            json.dump(empty_list, data_file, ensure_ascii=False, sort_keys=False, indent=4)

    @staticmethod
    def display_vac(data: list):
        if data:
            for v in data:
                for key, value in v.items():
                    print(key, value)
                print("+" * 30)
        else:
            print("Нет данных для вывода")
