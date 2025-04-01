import pytest
import allure
from Shifr1 import code_or_decode, alph, rand_alph


@allure.feature("Шифрование Цезаря")
class TestCaesarCipher:
    @allure.story("Тест шифрования")
    @allure.title("Шифрование слова 'привет' с шагом 3")
    def test_encrypt(self):
        with allure.step("Подготовка данных"):
            test_line = "привет"
            expected_result = "тулезх"
        
        with allure.step("Выполнение шифрования"):
            result = code_or_decode(alph, test_line, 3, 0)
        
        with allure.step("Проверка результата"):
            assert result == expected_result
    @allure.story("Тест дешифрования")
    @allure.title("Дешифрование слова 'тулезх' с шагом 3")
    def test_decrypt(self):
        test_line = "тулезх"
        expected_result = "привеп"
        result = code_or_decode(alph, test_line, 3, 1)
        assert result == expected_result

    @allure.story("Тест обработки невалидных символов")
    def test_invalid_char(self):
        test_line = "hello!"
        result = code_or_decode(alph, test_line, 3, 0)
        assert "!" not in result