from enum import Enum

class paymentMethod(Enum):
        De = 'DEBX'
        Xx = 'XXHB'



if __name__ == '__main__':
    print(paymentMethod.De.value)