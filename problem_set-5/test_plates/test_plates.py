import plates

def test_len():
    assert plates.is_valid("H") == False
    assert plates.is_valid("GOODBYE") == False

    assert plates.is_valid("HI") == True
    assert plates.is_valid("LOLO") == True

def test_alpha():
    assert plates.is_valid("C1I1") == False

    assert plates.is_valid("CS50") == True

def test_alphanumeric():
    assert plates.is_valid("##@@#") == False
    assert plates.is_valid("CS 50") == False

    assert plates.is_valid("HELLO") == True
    assert plates.is_valid("MM69") == True
    
def test_start_letters():
    assert plates.is_valid("1A") == False
    assert plates.is_valid("12") == False
    assert plates.is_valid("12345") == False

    assert plates.is_valid("AB123") == True
    assert plates.is_valid("MF666") == True


def test_num_rule():
    assert plates.is_valid("CS05") == False
    assert plates.is_valid("CS50A") == False

    assert plates.is_valid("ABC10") == True
