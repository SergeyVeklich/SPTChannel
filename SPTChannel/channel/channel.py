"""
Модель описывает процесс передачи пакетов данных по каналу с
вероятностью ошибки, которую задает исследователь млдели.
"""

from pyparsing import *
import random

"""
Парсер для вероятности ошибки в канале, введенной исследователем
"""
def checking_mistake(mistake_of_channel):
    int_num = Word(nums)
    pm_sign = Optional(Suppress("+") | Literal("-"))
    float_num = Combine(pm_sign + int_num + Optional('.' + int_num)
                        + Optional('e' + pm_sign + int_num)).setParseAction(
        lambda t: float(t.asList()[0]))
    single_unit = int_num + Optional('^' + float_num)
    base = int(single_unit.parseString(mistake_of_channel).asList()[0])
    power = float(single_unit.parseString(mistake_of_channel).asList()[2])
    return base ** power


def generate_mistake_to_package(packages, mistake_of_channel):
    mistake = checking_mistake(mistake_of_channel)
    print('error', 1 / mistake)
    rand_max = len(packages)


    mistake_polynomial = []

    if len(packages) <= 1 / mistake:
        number_of_mistake = random.randint(0, 1 / mistake - 1)
        print('number of mistake', number_of_mistake)
        for x in range(0, len(packages)):
            if x == number_of_mistake:
                mistake_polynomial.append(1)
            else:
                mistake_polynomial.append(0)
    else:
        bits_for_mistake = 1 / mistake
        print('bits', bits_for_mistake)
        count_mistake_of_package = len(packages) / bits_for_mistake
        print('count', count_mistake_of_package)
        count = 0
        for x in range(0, len(packages)):
            mistake_polynomial.append(0)

        while(count < count_mistake_of_package):
            number_of_mistake = random.randint(0, len(packages) - 1)
            mistake_polynomial[number_of_mistake] = 1
            print('number of mistake', number_of_mistake)

            count += 1

    #print('mistake', mistake_polynomial)
    #print('package before error', packages)

    for x in range(0, len(packages)):
        packages[x] = (packages[x] + mistake_polynomial[x]) % 2

    return packages

#TODO change discrete channel model



if __name__ == '__main__':
    mis = '10^-1'
    print(checking_mistake(mis))
    packales =[1,1,1,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0,1,1,1,0,1,0]
    print(generate_mistake_to_package(packales, mis))