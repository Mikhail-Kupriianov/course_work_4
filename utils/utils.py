import os

from src.get_vacancies import HHVacancies, SJVacancies
from src.storage_vac import StorageJson
from src.vacancies import Vacancies


def main_menu() -> None:
    """Функция главного меню"""

    while True:
        option = input("Главное меню> \n[Парсинг вакансий]-1 [Сохранённые вакансии]-2 [Выход]-0 \n"
                       "(выбери число, нажми Enter)\n")
        if option == "1":
            menu_looking_vac()
        elif option == "2":
            saved_vac()
        elif option == "0":
            stop = input("Подтвердите завершение работы (Y) ")
            if stop.lower() == "y":
                exit()
        else:
            print("Неверный ввод, попробуйте ещё\n")


def display_vac(vac_list: list) -> None:
    """Функция выводит список вакансий на экран"""

    for item in vac_list:
        print(item)
        print("\n", "*" * 30, "\n", sep="")
    print("=" * 30)


def menu_looking_vac() -> None:
    """Функция опции главного меню [Парсинг вакансий]"""

    is_sort_revers = True
    vac_count = 0
    while True:
        option = input(f"Главное меню > Парсинг вакансий (Получено вакансий: {vac_count})> \n"
                       "[Получить]-1 [Сортировать]-2 [ТОП N по З/П]-3 [Запись в файл]-4 [Назад]-0\n"
                       "(выбери число, нажми Enter)\n")

        if option == "1":
            Vacancies.all = []
            [Vacancies(vac) for vac in load_vac()]
            vac_count = len(Vacancies.all)
            display_vac(Vacancies.all)
            print(f"Получено вакансий: {vac_count}")

        elif option == "2":
            if Vacancies.all:
                if is_sort_revers:
                    Vacancies.all.sort(reverse=is_sort_revers)
                    is_sort_revers = not is_sort_revers
                    display_vac(Vacancies.all)
                    print("Сортировка вакансий - зарплата по убыванию")
                else:
                    Vacancies.all.sort(reverse=is_sort_revers)
                    is_sort_revers = not is_sort_revers
                    display_vac(Vacancies.all)
                    print("Сортировка вакансий - зарплата по возрастанию")

        elif option == "3":
            if Vacancies.all:
                n = input("Введите количество вакансий для ТОП ")
                if n.isdigit():
                    display_vac(Vacancies.top_n(int(n)))
                else:
                    print("Неверный ввод")

        elif option == "4":
            if Vacancies.all:
                store_vac = StorageJson()
                store_vac.update(Vacancies.all)

        elif option == "0":
            break

        else:
            print("Неверный ввод, попробуйте ещё\n")


def load_vac() -> list:
    """Функция загрузки вакансий из файла"""

    base = "hh"
    keywords = []
    search_field = ""
    per_page = 20
    period = 1

    option = input("Выберите ресурс: 1-HeadHunter (default) 2-SuperJob\n")
    if option == "2":
        base = "sj"

    option = input("Введите слова для поиска через пробел\n")
    if option:
        keywords = option.split()

    print("Укажите поля (введите '1') для поиска (если ни одно поле не указано - поиск по всем полям")
    field_1 = input("Искать в поле 'Название вакансии': 1-yes ")
    field_2 = input("Искать в поле 'Название компании': 1-yes ")
    field_3 = input("Искать в поле 'Описание вакансии': 1-yes ")
    search_field = search_field + "1" if field_1 == "1" else search_field + "0"
    search_field = search_field + "1" if field_2 == "1" else search_field + "0"
    search_field = search_field + "1" if field_3 == "1" else search_field + "0"

    option = input("Введите количество вакансий: 20 default\n")
    if option.isdigit():
        if int(option) < 1:
            per_page = 1
        elif int(option) > 100:
            per_page = 100
        else:
            per_page = int(option)

    if base == "hh":
        option = input("Введите количество дней для поиска: 1 default\n")
        if option.isdigit():
            period = 1 if int(option) < 1 else int(option)
    else:
        option = input("Введите количество дней для поиска - 1, 3, 7 или 0 (за всё время): 1 default\n")
        if option.isdigit():
            if int(option) in (0, 1, 3, 7):
                period = int(option)

    input(f"Параметры запроса:\n"
          f"ресурс =           {base}\n"
          f"слова для поиска = {keywords}\n"
          f"поля для поиска ['вакансия', 'компания', 'описание'] = {[x for x in search_field]}\n"
          f"количество вакансий = {per_page}\n"
          f"количество дней = {period}\n"
          f"Нажмите Enter ")
    if base == "hh":
        hh_vac = HHVacancies()
        hh_vac.set_params("period", period)
        hh_vac.set_params("per_page", per_page)
        hh_vac.set_params("text", " ".join(keywords))
        hh_vac.set_params("search_field", search_field)
        hh_vac.get_vacancies()
        if hh_vac.response == 200:
            print(f"Успешно, вакансий {len(hh_vac.vacancies)}")
        return hh_vac.provide_vacancies()
    else:
        sj_vac = SJVacancies()

        for keyword in keywords:
            index = 1
            for item in search_field:
                if int(item):
                    sj_vac.set_params("keywords", str(index) + '=' + keyword)
                index += 1

        sj_vac.set_params("period", period)
        sj_vac.set_params("count", per_page)
        return sj_vac.provide_vacancies()


def saved_vac() -> None:
    """Функция сохранения вакансий в файл"""

    store_vac = StorageJson()
    if not os.path.exists(store_vac.path) or not store_vac.load_vac():
        print("Файл 'storage_vac.json' не существует или пуст - загрузите вакансии")
        return
    else:
        while True:
            option = input(f"Главное меню > Сохранённые вакансии > (Помечены к удалению {store_vac.marked_delete})\n"
                           "[Загрузить]-1 [Пометить к удалению]-2 [Удалить помеченные]-3 [очистить файл]-4 [Назад]-0\n"
                           "(выбери число, нажми Enter)\n")

            if option == "1":
                load_filter = input("Введите слово для фильтра или минимальную зарплату\n"
                                    "Enter - загрузить все вакансии из файла\n")
                data = store_vac.load_vac(load_filter)
                if data:
                    for vac in data:
                        for key, value in vac.items():
                            print(key, value)
                        print("+" * 30)
                    print(f"Загружено вакансий {len(data)}")
                    print("=" * 30)
                else:
                    print("Нет данных для вывода")

            elif option == "2":
                del_id = input("Введите id вакансий через пробел для удаления из файла\n0 - для сброса всех пометок\n")
                if del_id == "0":
                    store_vac.clear_marks()
                else:
                    store_vac.mark_del(del_id)

            elif option == "3":
                answer = input(f"Будут удалены вакансии {store_vac.marked_delete}\n"
                               f"Enter для удаления или 0 - для отмены операции\n")
                if answer != "0":
                    store_vac.del_marked()

            elif option == "4":
                answer = input(f"Файл 'storage_vac.json' будет очищен\n"
                               f"Enter для очистки или 0 - для отмены операции\n")
                if answer != "0":
                    store_vac.del_all()

            elif option == "0":
                break

            else:
                print("Неверный ввод, попробуйте ещё\n")
