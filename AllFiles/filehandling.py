# to make file upper case
# f = open('mbox-short.txt')
# for line in f:
#     print(line.upper(),end = '')

# fname = input("enter a file name")
# #f = open('mbox-short.txt')
# try:
#     f = open(fname)
# except:
#     print("Entered invalid file name: ",fname)
#     quit()
# count = 0
# for line in f:
#     count += 1
# print("number of lines",count)
#try except block

#searching for some pattern
# for line in f:
#     #if line.startswith("From:"):
#     if not line.startswith("From:"):
#         continue
#     print(line,end='')

#using in
# for line in f:
#     if not '@uct.ac' in line:
#         continue
#     print(line,end = '')

#reading the whole file:
'''inp = f.read()
print(len(inp))
print(inp[:20])
'''
#printing number of lines:
'''count = 0
for line in f:
    count += 1
print("number of lines",count)
'''

#print(f) - prints file mode and all
''' another way to open a file here no need to mention f.close()
with open('mbox-short.txt') as f:
    for line in f:
        print(line,end=' ')
#    print(f.name)
    #fread = f.readlines()
   fread = f.readline()
    print(fread,end='')
    fread = f.readline()
    print(fread,end='') '''

#print the number
# text = "xadsddsd-345sdsaffdf:     0.8475"
# text = text.replace(" ","")
# print(text)
# fpos = text.find(":")
# print(fpos)
# print(text[21:])


fhandle = open ("mbox-short.txt")
for line in fhandle:
    line = line.rstrip()
    wds = line.split()
    #guardian len(wds) < 3 checking for 3 string is there or not..if not then it will skip
    if len(wds)<3 or wds[0]!= 'From':
        continue
    print(wds[2])