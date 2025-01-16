import pytest
import bank

def test_hello():
    assert bank.value("hello") == 0
    assert bank.value("Hello") == 0
    assert bank.value("HELLO") == 0

def test_startswithH():
    assert bank.value("Hey") == 20
    assert bank.value("hi") == 20
    assert bank.value("HOWDY") == 20

def test_else():
    assert bank.value("What's up doc") == 100
    assert bank.value("Good morning") == 100
    assert bank.value("Bye-bye") == 100
