from states import State
from modelinput import ModelInput

# Row-Column state transition table
# Columns -> Input
# Rows -> States
# 6 x 7 table
transition_table = [
    [State.MAIN,State.INVALID,State.INVALID,State.INVALID,State.INVALID,State.INVALID,State.INVALID],
    [State.INVALID,State.INVALID,State.WITHDRAW,State.DEPOSIT,State.BALANCE,State.RECEIPT,State.IDLE],
    [State.INVALID,State.MAIN,State.INVALID,State.INVALID,State.INVALID,State.INVALID,State.IDLE],
    [State.INVALID,State.MAIN,State.INVALID,State.INVALID,State.INVALID,State.INVALID,State.IDLE],
    [State.INVALID,State.MAIN,State.INVALID,State.INVALID,State.INVALID,State.INVALID,State.IDLE],
    [State.INVALID,State.MAIN,State.INVALID,State.INVALID,State.INVALID,State.INVALID,State.IDLE]
]

def is_valid_transition(current_state,input):
    if transition_table[current_state][input] == State.INVALID:
        return False
    else:
        return True
        
def transition(current_state,input):
    return transition_table[current_state][input]
    
