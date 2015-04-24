"""
Модель описывает процесс передачи пакетов данных по каналу с
вероятностью ошибки, которую задает исследователь млдели.
"""

from pyparsing import *
import random
from sender.sender import Sender


class Channel:
    def __init__(self, mistake, send):
        self.mistake_of_channel = mistake
        self.sender = send
        pack = generate_mistake_to_package(send.forming_encoded_massage(), mistake)
        self.packages = pack
        self.phasing_combinate = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]

    def set_package(self, value):
        #print('set')
        self.packages = value

    def get_package(self):
        #print('get')
        self.packages = generate_mistake_to_package(self.sender.forming_encoded_massage(), self.mistake_of_channel)
        return self.packages

    #packages = property(get_package, set_package)

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



    # self.set_package(pa)


    #TODO change discrete channel model


def generate_mistake_to_package(packages, mistake):
    mistake = checking_mistake(mistake)
    #print('error', 1 / mistake)
    rand_max = len(packages)

    mistake_polynomial = []

    if len(packages) <= 1 / mistake:
        number_of_mistake = random.randint(0, 1 / mistake - 1)
     #   print('number of mistake', number_of_mistake)
        for x in range(0, len(packages)):
            if x == number_of_mistake:
                mistake_polynomial.append(1)
            else:
                mistake_polynomial.append(0)
    else:
        bits_for_mistake = 1 / mistake
      #  print('bits', bits_for_mistake)
        count_mistake_of_package = len(packages) / bits_for_mistake
       # print('count', count_mistake_of_package)
        count = 0
        for x in range(0, len(packages)):
            mistake_polynomial.append(0)

        while (count < count_mistake_of_package):
            number_of_mistake = random.randint(0, len(packages) - 1)
            mistake_polynomial[number_of_mistake] = 1
        #    print('number of mistake', number_of_mistake)

            count += 1

    # print('mistake', mistake_polynomial)
    #print('package before error', packages)
    #print('before', packages)
    for x in range(0, len(packages)):
        packages[x] = (packages[x] + mistake_polynomial[x]) % 2
    #print('after', packages)

    return packages


if __name__ == '__main__':
    mis = '10^-1'
    s = Sender(1544)
    c = Channel(mis, s)
    packages = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0]
    print('rec0', c.get_package())
    print('rec1', c.get_package())

