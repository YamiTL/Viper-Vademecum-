def boolean_to_string(b):
    if b == True:
        return 'True'
    else:
        return 'False'


def test_boolean_to_string():
    assert boolean_to_string(True) == 'True'
    assert boolean_to_string(False) == 'False'

boolean_to_string(True)