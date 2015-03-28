"""
Модель приемника. Выполняется декодирование сообщения и если обнаружена ошибка,
производиться переспрос
"""
from sender.sender import Sender
from channel.channel import generate_mistake_to_package


class Receiver():
    def __init__(self, packages, polynomial):
        self.package = packages[8:len(packages)-8]
        self.polynom = polynomial


    def set_package(self, packages):
        print('SET')
        self.package = packages[8:len(packages)-8]

    def set_package_old(self, package):
        self.package = package

    def decode_received_message(self, package):
        msg = list(package)
        div = list(self.polynom)
        for i in range(len(msg) - len(self.polynom)):
            # If that messsage bit is 1, perform modulo 2 multiplication
            if msg[i] == 1:
                for j in range(len(div)):
                    # Perform modulo 2 multiplication on each index of the divisor
                    msg[i + j] = (int(msg[i + j]) + int(div[j])) % 2
        # Output the last error-checking code portion of the message generated
        print('decode')
        return msg[-len(div):]

    def checking_received(self):
        count = 0
        result = False
        decode = self.decode_received_message(self.package)
        print('decode_pol', decode)
        for x in decode:
            if x == 0:
                count += 1

        if count == len(decode):
            return True
        else:
            return result

    def get_message(self):
        return self.package[16:len(self.package)-len(self.polynom)]

    def convert_to_int(self):
        mes = ''
        for x in self.get_message():
            mes += str(x)
        received_message = int(mes, 2)
        return received_message

    def checking_new_pack(self, packages):
        count = 0
        result = False
        decode = self.decode_received_message(packages)
        print('decode_pol', decode)
        for x in decode:
            if x == 0:
                count += 1

        if count == len(decode):
            return True
        else:
            return result




if __name__ == '__main__':
    s = Sender(1533)

    r = Receiver(generate_mistake_to_package(s.forming_encoded_massage(), '10^-3'), s.choice_polynomial())
    print('decode', r.decode_received_message())
    print('checking', r.checking_received())
    print('package', r.package)
    s.convert_to_binary()
    print('enter_message', r.get_message())
    r.convert_to_int()