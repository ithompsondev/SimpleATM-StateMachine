from enum import IntEnum

class State(IntEnum):
    INVALID = -1
    IDLE = 0
    MAIN = 1
    WITHDRAW = 2
    DEPOSIT = 3
    BALANCE = 4
    RECEIPT = 5