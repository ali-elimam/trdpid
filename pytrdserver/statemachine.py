class Command:
	state1 = None
	state2 = None
	
	command = ""

	def __init__(self, state1, state2, command):
		self.state1=state1
		self.state2 = state2
		self.command = command
		
		self.state1.cmds.append(self)

	def __str__(self):
		return "Command (%s, %s)" % (self.state1, self.state2)

class State:
	def __init__(self, name):
		self.name = name
		self.cmds = []

	def __str__(self):
		return "State (%s)" % self.name

class FSM:
	state = None
	def __init__(self, states, istate, name):
		self.state = istate
		self.all_states = states
		self.name = name

	def get_cmds(self):
		return self.state.cmds
	
	def run_cmd(self, cmd):
		print(cmd.command)
		self.state = cmd.state2
		return self.get_cmds()

	def __str__(self):
		return "FSM %s (%s)" % (self.name, str(self.state))