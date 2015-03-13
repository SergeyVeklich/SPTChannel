__author__ = 'sergey'

"""
This module describes process of enter input data from user
and calculate of information and verification bits,
generating generator polynomial,
formation of a data package,
its cyclic encoding,
modeling channel with given probability of error.
"""

from math import sqrt, pow, log2
import random


class Sender:
    mistake = 0.001  # error of measurements
    fromParam = 0
    toParam = 32448  # length data field of package HDLC  = 4056 byte => 4056 * 8 = 32448 bits
    Ti = 2  # multiplicity of detection of an error
    coeff = 1.1

    def __init__(self, value, polynom):
        self.value = value
        self.polymon = polynom

    def get_information_bits(self):
        deltaX = 2 * sqrt(3) * self.mistake * sqrt(pow(self.coeff, 2) - 1)
        number_of_level = self.toParam // deltaX
        information_bits = int(log2(number_of_level + 1)) + 1
        return information_bits

    def get_verification_bits(self):
        verification_bits = 0
        while pow(2, verification_bits) <= (self.get_information_bits() + verification_bits + 1):
            verification_bits += 1
        return verification_bits

    def get_number_of_bits(self):
        return self.get_information_bits() + self.get_verification_bits()

    def generation_polynomial(self):
        length_cycle = pow(2, self.get_verification_bits()) + 1

        pass


    """
        Cyclic Redundancy Check

    Generates an error detecting code based on an inputted message
    and divisor in the form of a polynomial representation.

    Arguments:
        msg: The input message of which to generate the output code.
        div: The divisor in polynomial form. For example, if the polynomial
            of x^3 + x + 1 is given, this should be represented as '1011' in
            the div argument.
        code: This is an option argument where a previously generated code may
            be passed in. This can be used to check validity. If the inputted
            code produces an outputted code of all zeros, then the message has
            no errors.

    Returns:
        An error-detecting code generated by the message and the given divisor.
    """

    def crc(self, msg, div, code='000'):
        # Append the code to the message. If no code is given, default to '000'

        msg = msg + code

        # Convert msg and div into list form for easier handling

        msg = list(msg)
        div = list(div)

    # Loop over every message bit (minus the appended code)
        for i in range(len(msg) - len(code)):
            # If that messsage bit is 1, perform modulo 2 multiplication
            if msg[i] == '1':
                for j in range(len(div)):
                    # Perform modulo 2 multiplication on each index of the divisor
                    msg[i + j] = str((int(msg[i + j]) + int(div[j])) % 2)
        # Output the last error-checking code portion of the message generated
        return ''.join(msg[-len(code):])

    """
    the method for choose generator polynomial of cyclic coding
    """

    def choose_polynomial(self):
        select_polynomials = [[100101], [101001], [101111], [110111], [111011], [111101]]
        return select_polynomials[random.randint(0, len(select_polynomials)-1)]



if __name__ == '__main__':
    s = Sender(33, 34)
    print('inform', s.get_information_bits())
    print('verific', s.get_verification_bits())
    print('number: ', s.get_number_of_bits())
# TEST 1 ####################################################################
    print('Test 1 ---------------------------')
# Use a divisor that simulates: x^3 + x + 1
    div = '1011'
    msg = '11010011101100'

    print('Input message:', msg)
    print('Divisor:', div)

# Enter the message and divisor to calculate the error-checking code
    code = s.crc(msg, div)

    print('Output code:', code)

# Perform a test to check that the code, when run back through, returns an
# output code of '000' proving that the function worked correctly
    print('Success:', s.crc(msg, div, code) == '000')


# TEST 2 ####################################################################
    print('Test 2 ---------------------------')
# Use a divisor that simulates: x^2 + 1
    div = '0101'
    msg = '00101111011101'

    print('Input message:', msg)
    print('Divisor:', div)

# Enter the message and divisor to calculate the error-checking code
    code = s.crc(msg, div)

    print('Output code:', code)

# Perform a test to check that the code, when run back through, returns an
# output code of '000' proving that the function worked correctly
    print('Success:', s.crc(msg, div, code) == '000')
    s.choose_polynomial()