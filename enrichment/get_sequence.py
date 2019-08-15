'''
Quick script to grab an example sequence and scramble it a little
to be used in BLAST.
'''
import random
import os

# Pick a sequence, import
seqnum = random.choice([1, 2, 3, 4, 5])
print("Using sequence example number {}".format(seqnum))
lines = []
folder, _ = os.path.split(__file__)
with open(os.path.join(folder, "sequences", str(seqnum) + '.txt'), 'r') as file:
    for line in file:
        lines.append(line.strip())

sequence = "".join(lines)
sequence_scr = ""

# Scramble
const = 0.05
for i in range(len(sequence)):
    if random.random() < const:
        sequence_scr += random.choice("ACGT")
    else:
        sequence_scr += sequence[i]

# Write to file for copy paste
with open("result.txt", "w+") as file: # allow overwrite
    file.write(sequence_scr)

print("Finished.")