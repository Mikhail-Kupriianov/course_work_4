from abc import ABC, abstractmethod


class GetVacancies(ABC):

    @abstractmethod
    def set_params(self, key: str, value: str | int):
        pass

    @abstractmethod
    def reset_params(self):
        pass

    @abstractmethod
    def set_headers(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def display_vacancies(self):
        pass

    @abstractmethod
    def provide_vacancies(self):
        pass
