def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()  #ничего не возвращает

#inner_function()   #не работает, выдает ошибку

test_function()  #работает

