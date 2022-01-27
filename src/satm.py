from states import State
from modelinput import ModelInput
import logic
import sys

class SimpleATM:
    def __init__(self,branch_name,branch_code):
        self.branch_name = branch_name
        self.branch_code = branch_code
        self.state = State.IDLE # Enum states
		
    def __str__(self):
        return f'Thank you for using this ATM from {self.branch_name} | {self.branch_code}'
        
    def get_current_state(self):
        print(f'The ATM is currently: {self.state.value}')
        
    def transition(self,input):
        if input == ModelInput.CLOSE:
            print('SimpleATM closing...')
            sys.exit(1)
        elif input == ModelInput.INVALID:
            print(f'Invalid choice selected. Cannot transition from {self.state.name}')
        elif logic.is_valid_transition(self.state,input):
            prev_state = self.state
            self.state = logic.transition(self.state,input)
            print(f'Successful transition. Transitioned from {prev_state.name} to {self.state.name} given the input: {input.name}')
        else:
            print(f'Unsuccessful transition. Cannot transition from {self.state.name} given the input: {input.name}')
        
        