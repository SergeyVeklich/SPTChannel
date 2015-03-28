from sender.sender import Sender
from receiver.receiver import Receiver
from channel.channel import generate_mistake_to_package


def modeling_without_method():
    s = Sender(1533)
    mistake = '10^-3'
    channel1 = generate_mistake_to_package(s.forming_encoded_massage(), mistake)
    channel2 = generate_mistake_to_package(s.forming_encoded_massage(), mistake)
    r1 = Receiver(channel1, s.gener_polynomial)
    r2 = Receiver(channel2, s.gener_polynomial)

    count_asked = 0

    while(not r1.checking_received() or not r2.checking_received()):
        count_asked += 1
        r1.set_package(generate_mistake_to_package(s.forming_encoded_massage(), mistake))
        r2.set_package(generate_mistake_to_package(s.forming_encoded_massage(), mistake))

    print('count', count_asked)
    print('recev_message1', r1.convert_to_int())
    print('recev_message2', r2.convert_to_int())


def modeling_with_method():
    s = Sender(1533)
    mistake = '10^-3'
    channel1 = generate_mistake_to_package(s.forming_encoded_massage(), mistake)
    channel2 = generate_mistake_to_package(s.forming_encoded_massage(), mistake)
    r1 = Receiver(channel1, s.gener_polynomial)
    r2 = Receiver(channel2, s.gener_polynomial)

    count_asked = 0

    while(not r1.checking_received() or not r2.checking_received()):
        m1 = int(len(r1.package) / 2)
        K1 = int(len(r2.package) - (len(r2.package) / 2))
        print('-----m1--------', m1)
        print('-----K1--------', K1)
        print(len(r1.package[0:m1]))
        print(len(r2.package[K1:]))
        pack1 = list(r1.package[0:m1] + r2.package[K1:])
        print('--------PACK1-----------', pack1)
        pack2 = list(r2.package[0:m1] + r1.package[K1:])
        print('--------PACK2-----------', pack2)

        if r1.checking_new_pack(pack1):
            print('IIIIIIIIIIIII')
            r1.set_package_old(pack1)
            r2.set_package_old(pack1)
        elif r1.checking_new_pack(pack2):
            print('22222222222222')
            r1.set_package_old(pack2)
            r2.set_package_old(pack2)
        else:
            count_asked += 1
            r1.set_package(generate_mistake_to_package(s.forming_encoded_massage(), mistake))
            r2.set_package(generate_mistake_to_package(s.forming_encoded_massage(), mistake))

    print('count', count_asked)
    print('recev_message1', r1.convert_to_int())
    print('recev_message2', r2.convert_to_int())


if __name__ == '__main__':
    modeling_without_method()
    #modeling_with_method()