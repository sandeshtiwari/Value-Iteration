is_bad_side = [0, 1, 1, 1, 0, 0, 0]
is_bad_side = [0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0]
# is_bad_side = [0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0]

states = {}

N = len(is_bad_side) - 1
# value_of_states = {}

for i in range(0, N+1):
	if is_bad_side[i] == 0:
		states[i] = i
		# value_of_states[i] = i
# print(states)


updates = -1

while updates != 0:
	updates = 0
	temp_states = dict(states)
	for state, current_value in temp_states.items():
		# print("STATE", state)
		new_value = 0
		for i in range(1, N+1):
			if is_bad_side[i] == 0:
				new_state = i + state
				if new_state not in temp_states:
					states[new_state] = new_state
					# value_of_states[new_state] = new_state
				new_value += (1/N)* states[new_state]
		if current_value < new_value:
			# print("UPDATING ", state, current_value," Value to ", new_value)
			updates = 1
			states[state] = new_value

print(states,"\n")
# print(value_of_states)
	