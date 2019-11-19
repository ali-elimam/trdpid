from statemachine import *

states = [State('Standby'), State('Initialized'), State('Configured'), State('Error')]

Command(states[0], states[1], '10')
Command(states[1], states[0], '30')
Command(states[1], states[0], '90')
Command(states[1], states[2], '100')
Command(states[1], states[2], '101')
Command(states[2], states[0], '90')
Command(states[2], states[1], '20')

dcs = FSM(states, states[0], 'dcs')