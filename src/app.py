from satm import SimpleATM
import logic
from modelinput import ModelInput
import sys    
    
def transition_options():
    # Present the user with all possible transition options even if invalid
    print('[1] Enter PIN')
    print('[2] Withdraw funds')
    print('[3] Deposit funds')
    print('[4] Check balance')
    print('[5] Print receipt')
    print('[6] Return')
    print('[7] Remove card')
    print('[x] Close operation')
    
def get_input():
    try:
        choice = input('>> ')
        if choice == 'x':
            return ModelInput.CLOSE
        else:
            if choice == '1':
                choice = ModelInput.CORRECT_PIN
            elif choice == '2':
                choice = ModelInput.WITHDRAW_FUNDS
            elif choice == '3':
                choice = ModelInput.DEPOSIT_FUNDS
            elif choice == '4':
                choice = ModelInput.BALANCE_CHECK
            elif choice == '5':
                choice = ModelInput.RECEIPT_PRINT
            elif choice == '6':
                choice = ModelInput.RETURN
            elif choice == '7':
                choice = ModelInput.END_SERVICE
            else:
                choice = ModelInput.INVALID
            return choice
    except Exception as e:
        print('Invalid option selected.')
        
def main():
    bname = 'Simple Bank Branch'
    bcode = 'SBB001'
    new_atm = SimpleATM(bname,bcode)
    print(new_atm)
    while True:
        transition_options()
        choice = get_input()
        new_atm.transition(choice)
        
if __name__ == '__main__':
    main()