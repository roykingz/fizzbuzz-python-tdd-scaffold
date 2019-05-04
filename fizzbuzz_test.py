from fizzbuzz import fizzbuzz


def test_fizzbuzz():
    assert fizzbuzz("15") == ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8',
                              'fizz', 'buzz', '11', 'fizz', '13', '14',
                              'fizz buzz']
    assert fizzbuzz("daf") is None
    assert fizzbuzz("-14") is None
