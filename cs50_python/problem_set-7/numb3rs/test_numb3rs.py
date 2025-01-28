import numb3rs


def test_borders():
    assert numb3rs.validate("0.0.0.0") == True
    assert numb3rs.validate("255.255.255.255") == True
    assert numb3rs.validate("255.0.255.0") == True


def test_anyip():
    assert numb3rs.validate("192.168.1.1") == True
    assert numb3rs.validate("256.256.256.256") == False
    assert numb3rs.validate("256") == False


# def test_anyip():
#     test_ips = [
#         ("192.168.1.1", True),
#         ("256.256.256.256", False),
#         ("127.0.0.1", True),
#         ("0.0.0.0", True),
#         ("255.255.255.255", True),
#         ("01.1.1.1", False),
#         ("192.168.01.1", False),
#         ("300.168.1.1", False),
#         ("10.0.0.256", False),
#     ]
#     for ip, check in test_ips:
#         assert numb3rs.validate(ip) == check
