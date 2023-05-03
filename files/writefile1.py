#this program creates a new file called output.txt#

fout = open('output.txt', 'w')
print(fout)
line1 = "This is a new text file."
fout.write(line1)

