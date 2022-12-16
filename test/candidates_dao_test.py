from dao.candidates_dao import CandidatesDAO
import pytest


@pytest.fixture()
def candidates_dao():
    candidates_dao_instance = CandidatesDAO('./data/candidates.json')
    return candidates_dao_instance


# Задаем ожидаемые ключи
keys_should_by = {'pk', 'name', 'position'}

class TestCandidateDAO:
    """Тестируем функциональность Кандидатов"""
    def test_get_all(self, candidates_dao):
        """Проверяет верен ли весь список"""
        candidates = candidates_dao.get_all()
        assert type(candidates) == list[dict], "Загруженные данные из файла возвращаются не списком"
        assert len(candidates) > 0, "Возвращается пустой список"
        assert set(candidates[0].keys()) == keys_should_by, "Ключи списка кандидатов не совпадают с ожидаемыми"

    def test_get_by_pk(self, candidates_dao):
        """Проверяет совпадает ли искомый кандидат"""
        candidate = candidates_dao.get_by_pk(1)
        assert candidate['pk'] == 1, "Возвращается неверный кандидат"
        assert set(candidate.keys()) == keys_should_by, "Ключи кандидата не совпадают с ожидаемыми"
