from enum import IntEnum

class ModelInput(IntEnum):
    INVALID = -2
    CLOSE = -1
    CORRECT_PIN = 0
    RETURN = 1
    WITHDRAW_FUNDS = 2
    DEPOSIT_FUNDS = 3
    BALANCE_CHECK = 4
    RECEIPT_PRINT = 5
    END_SERVICE = 6