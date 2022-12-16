class TestMain:
    """Класс тестирует блюпринт Главной страницы"""

    def test_root_status(self):
        """Проверка статус-кода"""
        response = test_client.get('/', follow_redirects=True)
        assert response.status_code == 200, "Неверный статус-код всех постов"

    def test_root_content(self):
        """Проверка кодировки"""
        response = test_client.get('/', follow_redirects=True)
        assert "Это главная страница" in response.data.decode('utf-8'), "Кодировка страницы не верна"
