###################################################################################
#Dictionaries
###################################################################################

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    line = line.rstrip()
    if line == '': continue
    words = line.split()
    if words[0] != 'From': continue
    
    counts[words[1]] = counts.get(words[1], 0) + 1

bigcount = None
bigword = None

for word, count in counts.items():
    if bigcount == None or count > bigcount:
        bigcount = count
        bigword = word
print bigword, bigcount