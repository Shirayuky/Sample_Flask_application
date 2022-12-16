from dao.vacancies_dao import VacanciesDAO
import pytest

keys_should_by = {'pk', 'company', 'position', 'salary'}


@pytest.fixture()
def vacancies_dao():
    vacancies_dao_instance = VacanciesDAO('data/vacancies.json')
    return vacancies_dao_instance


class TestVacanciesDAO:
    """Тестируем DAO Вакансий"""

    def test_get_all(self, vacancies_dao):
        """Проверяет верен ли весь список"""
        vacancies = vacancies_dao.get_all()
        assert type(vacancies) == list[dict], "Загруженные данные из файла возвращаются не списком"
        assert len(vacancies) > 0, "Возвращается пустой список"
        assert set(vacancies[0].keys()) == keys_should_by, "Ключи списка кандидатов не совпадают с ожидаемыми"

    def test_get_by_pk(self, vacancies_dao):
        """Проверяет совпадает ли искомая вакансия"""
        vacancies = vacancies_dao.get_by_pk(1)
        assert type(vacancies) == dict, "Загруженная вакансия выводится не в формате словаря"
        assert vacancies['pk'] == 1, "Возвращается неверный кандидат"
        assert set(vacancies.keys()) == keys_should_by, "Ключи кандидата не совпадают с ожидаемыми"

