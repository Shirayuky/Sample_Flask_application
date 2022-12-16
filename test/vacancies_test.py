class TestVacancies:
    """Класс тестирует блюпринт Вакансий"""
    def test_all_status(self, test_client):
        """Проверяет статус-код всех вакансий"""
        response = test_client.get('/vacancies', follow_redirects=True)
        assert response.status_code == 200, "Неверный статус-код при запросе всех вакансий"

    def test_by_pk_status(self, test_client):
        """Проверяет статус-код всех вакансий"""
        response = test_client.get('/vacancies/1', follow_redirects=True)
        assert response.status_code == 200, "Неверный статус-код при поиске одной вакансии"
