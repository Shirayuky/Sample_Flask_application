import json
from typing import List


class CandidatesDAO:
    """Вся деятельность кандидатов"""

    def __init__(self, path):
        self.path = path

    def load_data(self) -> List[dict]:
        """
        Загружает данные из файла
        return: Список со словарем
        """
        with open(self.path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data

    def get_all(self) -> List[dict]:
        """
        Возвращает список со всеми данными
        return: Список со словарем
        """
        candidates = self.load_data()
        return candidates

    def get_by_pk(self, pk) -> dict:
        """
        Возвращает кандидата по id/pk
        return: Список
        """
        candidates = self.load_data()
        for candidate in candidates:
            if candidate['pk'] == pk:
                return candidate
