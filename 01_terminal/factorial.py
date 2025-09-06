def factorial(n:int):
    assert isinstance(n, int)
    assert n>=0
    if n <= 1:
        return 1
    return n * factorial(n-1)


def test_nominal():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(5) == 2*3*4*5
    print("Tous les tests OK")


def test_exception():
    try:
        factorial(3.2)
    except Exception as e:
        pass
    else:
        raise Exception("Aucune exception n'a été levée")

    try:
        factorial(-1)
    except Exception as e:
        pass
    else:
        raise Exception("Aucune exception n'a été levée")

    print("Exception bien levées")


test_nominal()
test_exception()

print(__name__)