import fuel
import pytest

def test_conversion():
    assert fuel.gauge(fuel.convert("2/2")) == "F"
    assert fuel.gauge(fuel.convert("1/100")) == "E"
    assert fuel.gauge(fuel.convert("38/100")) == "38%"

def test_gauge():
    assert fuel.gauge(99 or 100) == "F"
    assert fuel.gauge(0 or 1) == "E"
    assert fuel.gauge(25) == "25%"

def test_convert():
    assert fuel.convert("2/2") == 100
    assert fuel.convert("1/2") == 50
    assert fuel.convert("1/4") == 25

def test_errors():
    with pytest.raises(ValueError):
        fuel.convert("3 0")
    with pytest.raises(ZeroDivisionError):
        fuel.convert("3/0")
    with pytest.raises(ValueError):
        fuel.convert("999/1")
    with pytest.raises(ValueError):
        fuel.convert("a/b")