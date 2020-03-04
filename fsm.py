#Trevor Seyller
#CSC 344 Assignment 5

#fsm.txt - file describing the fsm
fsmfile = open("fsm.txt", "r")

#list of characters in alphabet
alphabet = fsmfile.readline().split()

#number of states
numstates = int(fsmfile.readline())

#list of accepting states
accepting = fsmfile.readline().split()

#initialize list of transitions
#each state has dictionary of input characters 
transitions = []
for i in range(numstates) :
    transitions.append({})
    for char in alphabet:
        transitions[i][char] = 0

#fill dictionaries with correct transitions
for line in fsmfile:
    line = line.split()
    transitions[int(line[0])][line[1]] = line[2]

fsmfile.close()

stringsfile = open("strings.txt", "r")

for line in stringsfile:
    line = line.rstrip("\n")
    print("'" + line + "' - ", end='')
    
    #create list of characters in string
    chars = [char for char in line]

    #begin at state 0
    currstate = 0

    #run string through fsm
    for char in chars:
        currstate = int(transitions[currstate][char])

    if str(currstate) in accepting :
        print ("Accepted")
    else:
        print ("Not Accepted")

stringsfile.close()

    
    





