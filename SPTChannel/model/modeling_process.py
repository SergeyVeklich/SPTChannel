from sender.sender import Sender
from receiver.receiver import Receiver
from channel.channel import Channel, generate_mistake_to_package, checking_mistake
import sqlite3


def modeling_without_method(message, mistake):
    s = Sender(message)


    channel1 = Channel(mistake, s)
    channel2 = Channel(mistake, s)
    r1 = Receiver(channel1.packages, s.gener_polynomial)
    r2 = Receiver(channel2.packages, s.gener_polynomial)

    count_asked = 0
    count = 0
    while((not r1.checking_received() or not r2.checking_received()) or r2.polynom != r1.polynom):
        count_asked += 1
        count += 1
        r1.set_package(channel1.get_package())
        r2.set_package(channel2.get_package())
        if count > 7:
            phasing_channels(s, channel1, r1)
            phasing_channels(s, channel2, r2)
            count = 0

    print('WITHOUT METHOD')
    print('count', count_asked)
    if r1.polynom == r2.polynom:
        print('recev_message1', r1.convert_to_int())
        print('recev_message2', r2.convert_to_int())
        return count_asked, r1.convert_to_int()
    else:

        print('recev_message1', r1.convert_to_int())
        print('recev_message2', r2.convert_to_int())
        return count_asked, r1.convert_to_int()


#check flag on package
def check_flag_on_package(chan, rec, flag):
    print('flag', flag)
    fl = list(chan.phasing_combinate)
    print('flqq', fl)
    if flag == fl:
        print('TRUE')
        return True
    else:
        print('FALSE')
        return False

#function for phasing channel
def phasing_channels(sen, chan, rec):
    result = 0
    flag = list(generate_mistake_to_package(list(chan.phasing_combinate), chan.mistake_of_channel))
    print('Phasing')
    if check_flag_on_package(chan, rec, flag):
        return True
    else:
        while not check_flag_on_package(chan, rec, flag):
            print('while')
            result += 1
            if result > 100:
                break
            else:
                return True


def modeling_with_method(message, mistake):
    s = Sender(message)

    channel1 = Channel(mistake, s)
    channel2 = Channel(mistake, s)
    r1 = Receiver(channel1.packages, s.gener_polynomial)
    r2 = Receiver(channel2.packages, s.gener_polynomial)

    count_asked = 0
    count = 0

    if phasing_channels(s, channel1, r1) and phasing_channels(s, channel2, r2):
        print('It is phasing  ')
        while((not r1.checking_received() or not r2.checking_received()) or r1.polynom != r2.polynom):
            m1 = int(len(r1.package) / 2)
            K1 = int(len(r2.package) - (len(r2.package) / 2))
       # print('-----m1--------', m1)
       # print('-----K1--------', K1)
       # print(len(r1.package[0:m1]))
       # print(len(r2.package[K1:]))
            pack1 = list(r1.package[0:m1] + r2.package[K1:])
        #print('--------PACK1-----------', pack1)
            pack2 = list(r2.package[0:m1] + r1.package[K1:])
        #print('--------PACK2-----------', pack2)

            if count > 7:
                print('phasing', count_asked)
                phasing_channels(s, channel1, r1)
                phasing_channels(s, channel2, r2)
                count = 0

            if checking_new_pack(pack1, s):
                print('IIIIIIIIIIIII')
                r1.set_package_old(pack1)
                r2.set_package_old(pack1)
            elif checking_new_pack(pack2, s):
                print('22222222222222')
                r1.set_package_old(pack2)
                r2.set_package_old(pack2)
            else:
                print('3333333333333')
                count_asked += 1
                count += 1
                r1.set_package(channel1.get_package())
                r2.set_package(channel2.get_package())
    #phasing_channels(s, channel1, r1)
        print('WITH METHOD')
        print('count', count_asked)
        print('recev_message11', r1.convert_to_int())
        print('recev_message22', r2.convert_to_int())
    else:
        phasing_channels(s, channel1, r1)
        phasing_channels(s, channel2, r2)
    return count_asked, r1.convert_to_int()


def checking_new_pack(pack, s):
    count = 0
    r = Receiver(pack, s.gener_polynomial)
    r.set_package_old(pack)
    decode = r.decode_received_message()
    print('decode_pol_pack', decode)
    for x in decode:
        if x == 0:
            count += 1

    if count == len(decode):
        return True
    else:
        return False

if __name__ == '__main__':
    '''conn = sqlite3.connect('test.db')
    print("Opened database successfully")

    conn.execute(''''''CREATE TABLE EXPERIMENTS
       (ID INT PRIMARY KEY     NOT NULL,
       PROBABILITY1           REAL    NOT NULL,
       ASKED1            INT     NOT NULL,
       PROBABILITY2           REAL    NOT NULL,
       ASKED2            INT     NOT NULL);'''#)

    #print("Table created successfully")
    mistake = '10^-2'

    message = 123
    modeling_without_method(message, mistake)
    modeling_with_method(message, mistake)