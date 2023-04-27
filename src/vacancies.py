class Vacancies:
    """Данный класс инициализируется данными вакансий из класса, который унаследован от класса GetVacancies.
    Объекты класса хранятся в списке класса, который при помощи методов класса можно выводить на экран,
    сортировать по зарплате и выводить TOP N вакансий по зарплате с произвольным числом N."""

    __slots__ = ('id_vac', 'name_vac', 'created_at', 'salary_from', 'salary_to', 'place', 'url_vac', 'employer',
                 'skills', 'charge', 'salary',)
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
        """Метод сравнивает объекты по зарплате"""

        return self.salary < other.salary

    @classmethod
    def top_n(cls, n: int):
        """Метод возвращает TOP N вакансий по зарплате"""
        cls.all.sort(reverse=True)
        return cls.all[:n]

    def __str__(self):
        """Метод переопределяет строковое представление объекта класса"""

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

    def display_vac(self):
        """Метод выводит список вакансий класса на экран"""

        for vac in self.all:
            print(vac)
        print(f"Всего вакансий - {len(Vacancies.all)}")
