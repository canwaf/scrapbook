def fetchroll( rollnumber ):
	while True:
		roll = raw_input("Input roll " + str(rollnumber) + " (5 x d6s): ")
		if len(roll)!=5:
			print "A valid roll requires a five digit long numbers in base 5+1 (e.g. 43561)"
			return 0;
		else:
			for bit in roll:
				if int(bit)>0 and int(bit)<7:
					continue
				else:
					print "The number you provided " + roll + " is invalid."
					print " "*(24 + roll.find(bit)) + "^ should be a number between 1 and 6."
					return 0;
			return roll;
			
def fetchnumber():
	while True:
		try:
			return int(raw_input("How many words do you want: "));
		except ValueError:
			print "Opps! Input a valid integer."
			
num = fetchnumber()

rolls = [];
for x in range(1, num + 1):
	while True:
		tmp = fetchroll(x);
		if tmp == 0:
			continue
		else:
			rolls.append(tmp)
			break
words = [];
with open('./diceware.txt', 'r') as diceware:
	for dice in rolls:
		for line in diceware:
			if line.startswith(dice):
				words.append(line[5:].strip())
				diceware.seek(0)
				break
print "\n\nROLL\tVALUE\tRESULT"
for x in range(0, num):
	print str(x + 1) + "\t" + rolls[x] + "\t" + words[x]

	