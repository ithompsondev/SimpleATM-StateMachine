# SimpleATM State Machine
Modelling the bare minimum of an ATMs operation using a Finite State Machine.

### Python Version
Coded using Python 3.9.9

### Running SimpleATM
`python app.py`

### Files
+ satm.py: SimpleATM Class
+ states.py: All implemented states as integer enumerations
+ modelinput.py: All implemented inputs as integer enumerations
+ logic.py: Contains the state transition table and checks whether a transition is valid given the current state of the ATM and given input
+ app.py: Run the SimpleATM State Machine Simulation 

### States and Inputs
States and Model Inputs were coded using `IntEnums` so that a *State Transition Table* can be implemented using a `list` where the integer enumerations can be used as list indices

### State Transition Table
The state transition table is represented by an M - by - N list where each row is represented by a state in which the ATM can occupy and each column is represented by a possible input that governs the ATMs operation

### States
The following states were implemented:
+ IDLE
+ MAIN MENU
+ WITHDRAW OPTION
+ DEPOSIT OPTION
+ BALANCE CHECK OPTION
+ RECIEPT PRINT OPTION
+ END SERVICE OPTION (Return to IDLE state)

An `INVALID` state was included for use in the state transition table

### Model Inputs
The following model inputs were implemented:
+ CORRECT PIN INPUT
+ RETURN INPUT
+ WITHDRAW FUNDS INPUT
+ DEPOSIT FUNDS INPUT
+ BALANCE CHECK INPUT
+ RECEIPT PRINT INPUT
+ END SERVICE INPUT

A `CLOSE` input was included to exit the SimpleATM Application at any time 