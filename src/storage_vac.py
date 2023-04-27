import json
import os

DATA_PATH = os.path.abspath("../data")


class StorageJson:
    """Данный класс сохраняет объекты класса Vacancies в файле storage_vac.json.
    Методы класса:
     - преобразуют объекты класса Vacancies в JSON формат;
     - сохраняют вакансии файл;
     - загружают вакансии из файла (целиком или согласно данным фильтра по ключевым словам или минимальной зарплате)
     и выводят их на экран;
     - обновляют вакансии в файле (в файле хранятся вакансии только с оригинальными id);
     - создают и обновляют список id вакансий для удаления из файла;
     - удаляют помеченные вакансии из файла"""

    __slots__ = ('file_name', 'path', 'marked_delete', 'data_buffer',)

    def __init__(self, file_name="storage_vac.json"):
        self.file_name: str = file_name
        self.path: str = os.path.join(DATA_PATH, self.file_name)
        self.marked_delete: list = []
        self.data_buffer: list = []
        if not os.path.exists(self.path):
            self.del_all()

    @staticmethod
    def to_dict(vac_obj) -> dict:
        """Метод преобразует объект Vacancies в JSON словарь"""

        result = {"id_vac": vac_obj.id_vac, "name_vac": vac_obj.name_vac, "created_at": vac_obj.created_at,
                  "salary_from": vac_obj.salary_from, "salary_to": vac_obj.salary_to, "place": vac_obj.place,
                  "url_vac": vac_obj.url_vac, "employer": vac_obj.employer, "skills": vac_obj.skills,
                  "charge": vac_obj.charge, "salary": vac_obj.salary}
        return result

    def update(self, new_data: list) -> None:
        """Метод обновляет вакансии в файле"""

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
        """Метод загружает вакансии данные из файла фильтруя их по параметру keywords b возвращает их в виде списка."""

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

    def mark_del(self, id_vac: str) -> None:
        """Метод добавляет id вакансии в список для удаления из файла"""

        for item in id_vac.split():
            self.marked_delete.append(item)

    def clear_marks(self) -> None:
        """Метод очищает список вакансий для удаления из файла"""

        self.marked_delete = []

    def del_marked(self) -> None:
        """Метод удаляет вакансии из файла согласно списку id для удаления"""

        self.data_buffer = []
        file_data = self.load_vac()
        for vac in file_data:
            if vac["id_vac"] not in self.marked_delete:
                self.data_buffer.append(vac)

        with open(self.path, 'w', encoding='utf-8') as data_file:
            json.dump(self.data_buffer, data_file, ensure_ascii=False, sort_keys=False, indent=4)
        self.clear_marks()

    def del_all(self) -> None:
        """Метод удаляет все вакансии из файла"""

        empty_list = []
        with open(self.path, 'w', encoding='utf-8') as data_file:
            json.dump(empty_list, data_file, ensure_ascii=False, sort_keys=False, indent=4)

    @staticmethod
    def display_vac(data: list) -> None:
        """Метод выводит список вакансий на экран"""

        if data:
            for v in data:
                for key, value in v.items():
                    print(key, value)
                print("+" * 30)
        else:
            print("Нет данных для вывода")
