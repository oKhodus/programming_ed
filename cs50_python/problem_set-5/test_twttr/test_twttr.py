import pytest
import twttr


def test_conversion():
    assert twttr.shorten("hello") == "hll"
    assert twttr.shorten("hEllO") == "hll"
    assert twttr.shorten("Twitter") == "Twttr"
    assert twttr.shorten("") == ""
    assert twttr.shorten("AEIOU") == ""
    assert twttr.shorten("12345") == "12345"

