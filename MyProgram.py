import sys

#executes the dfa, printing the trace and the vailidty of the input text
def executeDFA(text, states, acceptStates, startState, transition):
	currentState = startState;

	for i in range(len(text)):
		letter = text[i]
		#Prints the trace
		print("%s\t%s -- %s --> %s\t%s" %(text[0:i], currentState, letter,transition[currentState][letter], text[i+1:]))
		currentState = transition[currentState][letter] #reassigns the new currentState

	#consults whether text is accepted or rejected
	if currentState in acceptStates:
		print("accepted")
	else:
		print("rejected")


#Instantiates the default DFA to be executed if no DFA is given
if len(sys.argv) == 2:
	text = sys.argv[1]

	states = ["AG","B","D","EC","F"]
	acceptStates = ["AG", "B", "EC"]
	startState = "AG";
	#assigning each state with their corresponding transition
	transition = {"AG": {"a":"B", "b":"EC"},
	 			  "B": {"a":"EC", "b":"D"},
				  "EC": {"a":"EC", "b":"F"},
				  "D": {"a":"AG", "b":"F"},
				  "F": {"a":"EC", "b":"F"},
	 };

	executeDFA(text, states, acceptStates, startState, transition)


#Instantiates the DFA to be executed within the text file given
if len(sys.argv) == 3:
	text = sys.argv[1]
	dfaDef = open("%s" %(sys.argv[2]))

	transition = {}
	states = dfaDef.readline().strip().split(",")
	for state in states:
		#inititating dictionary of states for corresponding transitions
		transition[state] = {}
	alphabet = dfaDef.readline().strip().split(",")
	startState = dfaDef.readline().strip()
	acceptStates = dfaDef.readline().strip().split(",")

	#allows for the dictionary of transitions to be fully established
	for state in states:
		line = dfaDef.readline().strip().split(",")
		countertrans = 0
		for i in alphabet:
			transition[state][i] = line[countertrans]
			countertrans += 1

	currentState = startState;

	executeDFA(text, states, acceptStates, startState, transition)
