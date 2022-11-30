from django import template

register = template.Library()


@register.filter()
def rating(value):
    if value == 1:
        return f'{value} балл'
    elif 2 <= value <= 4:
        return f'{value} балла'
    else:
        return f'{value} баллов'


@register.filter()
def censor(value):
    censor_list = ['bitcoin', 'биткоин']
    for i in censor_list:
        value = value.lower()
        value = value.replace(i[1:], '*' * (len(i)-1))
    return value
