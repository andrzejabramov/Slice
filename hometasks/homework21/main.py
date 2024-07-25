def test_function():
    def inner_function():
        return 'Я в области видимости функции test_function'
    res = inner_function()
    return res


print(inner_function())
