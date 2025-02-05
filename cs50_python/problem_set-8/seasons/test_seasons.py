from seasons import *
from datetime import date
import inflect
import pytest

def test_date():
    today = date.today().isoformat()
    p = inflect.engine()
    assert p.number_to_words(calc("2005-04-01", today)).capitalize() == "Ten million, four hundred and thirty thousand, one hundred and sixty"
    assert p.number_to_words(calc("2024-02-05", today)).capitalize() == "Five hundred and twenty-five thousand, six hundred"

    with pytest.raises(ValueError):
        calc("January 1, 1999", today)
    