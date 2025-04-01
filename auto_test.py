import pytest
from Shifr1 import code_or_decode, alph, rand_alph

def test_encrypt():
    test_line = "привет"
    expected_result = "тулзкч"  # Для шага 3 в исходном алфавите
    result = code_or_decode(alph, test_line, 3, 0)
    assert result == expected_result

def test_decrypt():
    test_line = "тулзкч"
    expected_result = "привет"
    result = code_or_decode(alph, test_line, 3, 1)
    assert result == expected_result

def test_invalid_char():
    test_line = "hello!"
    result = code_or_decode(alph, test_line, 3, 0)
    assert "!" not in result  # Символ '!' не должен шифроваться