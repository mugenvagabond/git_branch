def get_title(stroke):
    """
    :param stroke: функция принимает на вход строку
    :return: возвращает строку со всеми заглавными буквами
    """
    new_stroke = stroke.upper()
    return new_stroke


def first_letter_title(value):
    """
    :param value: функция принимает на вход строку
    :return: возвращает строку с первой заглавной буквой
    """
    title_stroke = value.title()
    return title_stroke
