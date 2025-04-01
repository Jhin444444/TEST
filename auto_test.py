import pytest
from your_script_name import code_or_decode, alph, rand_alph  # Замените `your_script_name` на имя вашего файла

def test_encrypt():
    """Проверка шифрования (direct=0)."""
    test_line = "привет"
    expected_result = "тулзкч"  # Предполагаемый результат для шага 3
    result = code_or_decode(rand_alph(alph), test_line, 3, 0)
    assert result == expected_result

def test_decrypt():
    """Проверка дешифрования (direct=1)."""
    test_line = "тулзкч"
    expected_result = "привет"  # Должно вернуть исходный текст
    result = code_or_decode(rand_alph(alph), test_line, 3, 1)
    assert result == expected_result

def test_invalid_char():
    """Проверка на символы вне алфавита."""
    test_line = "hello!"
    result = code_or_decode(rand_alph(alph), test_line, 3, 0)
    assert "!" not in result  # Или другой ожидаемый результат