"""Функции для работы с массивами"""


def get(array, index, default=None):
    """
    Извлекает из списка значение по указанному индексу, если индекс существует.
    Если индекс не существует, возвращает значение по умолчанию.
    Функция работает только с неотрицательными индексами.
    :param array: исходный список.
    :param index: индекс извлекаемого элемента.
    :param default: значение по-умолчанию.
    :return: значение по индексу или значение по-умолчанию.
    """
    if index < 0:
        return default
    elif array == []:
        return default

    return array[index]


def my_slice(coll, start=0, end=None):
    """
    Возвращает новый массив, содержащий копию части исходного массива.
    :param coll: исходный список.
    :param start: индекс, по которому начинается извлечение. Если индекс отрицательный,
    start указывает смещение от конца списка. По умолчанию равен нулю.
    :param end: индекс, по которому заканчивается извлечение (не включая элемент с индексом end).
    Если индекс отрицательный, end указывает смещение от конца списка. По умолчанию равен длине исходного списка.
    :return: массив элементов
    """
    length = len (coll)

    if length == 0 :
        return []

    normalized_end = end

    if end is None :
        normalized_end = length
    elif end < 0 :
        if end < -length :
            return []
        if end <= start :
            return []
        normalized_end += length
    elif end < start :
        return []

    normalized_start = start

    if start < 0 :
        normalized_start += length
        if end is None :
            return "Ошибка, необходимо задать числовое значение для end"
        if start < end :
            normalized_end += length
        if start < -length :
            normalized_start = 0

    return coll[normalized_start :normalized_end]


#print (my_slice ([1, 2, 3, 4], -2, -1))
