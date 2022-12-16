import json
from typing import List


class VacanciesDAO:
    """Вся деятельность кандидатов"""

    def __init__(self, path):
        self.path = path

    def load_data(self) -> List[dict]:
        with open(self.path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data

    def get_all(self) -> List[dict]:
        vacancies = self.load_data()
        return vacancies

    def get_by_pk(self, pk) -> dict:
        vacancies = self.load_data()
        for vacancy in vacancies:
            if vacancy['pk'] == pk:
                return vacancy
