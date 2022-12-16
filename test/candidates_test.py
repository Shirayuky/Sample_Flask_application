class TestCandidates:
    """Класс тестирует блюпринт Кандидатов """
    def test_all_candidates_status(self, test_client):
        """Проверяет статус-код при запросе всех кандидатов"""
        response = test_client.get('/candidates', follow_redirect=True)
        assert response.status_code == 200, "Неверный статус-код при запросе всех кандидатов"

    def test_by_pk_candidates_status(self, test_client):
        """Проверяет статус-код при запросе одного кандидата"""
        response = test_client.get('/candidates/1', follow_redirect=True)
        assert response.status_code == 200, "Неверный статус-код при поиске одного кандидата"
