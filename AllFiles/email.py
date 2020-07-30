#fname = input("Enter file name: ")
#fh = open(fname)
fh = open("/Users/lavanyamallikharjuna/Downloads/mbox-short.txt")
count = 0
for line in fh:
    list = line.rstrip().split()
    if len(list)<1:
        continue
    if list[0]!='From ':
        continue
    print(list[1])
print("There were", count, "lines in the file with From as the first word")

