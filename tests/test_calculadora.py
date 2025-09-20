# tests/test_calculadora.py
import pytest
from src.calculadora import somar, dividir, subtrair, multiplicar

def test_somar():
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0

def test_subtrair():
    assert subtrair(10, 1) == 9
    assert subtrair(-1, -1) == 0

def test_dividir():
    assert dividir(10, 2) == 5
    with pytest.raises(ValueError):
        dividir(10, 0)

def test_multiplicar():
    assert multiplicar(10, 2) == 20
    assert multiplicar(5, 0) == 0
    assert multiplicar(5, -1) == -5