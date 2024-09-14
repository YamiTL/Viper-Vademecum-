def repeat_str(repeat:int, string:str)-> str:
    return repeat*string

def test_repeat_str():
    assert repeat_str(4, 'a') == 'aaaa'
    assert repeat_str(3, 'hello ') == 'hello hello hello '
    assert repeat_str(2, 'abc') == 'abcabc'

def blabla():
    pass