import os
# file = open("/Users/lavanyamallikharjuna/Downloads/SampleCSVFile_556kb.txt",'r')
# print(file.readline())
# file.close()

# file = open("/Users/lavanyamallikharjuna/Downloads/SampleCSVFile_556kb.txt",'r')
# print(file.readlines())
# file.close()

#appending mode
file = open("/Users/lavanyamallikharjuna/Downloads/SampleCSVFile_556kb.txt",'a+')
file.write("love amazon")
print(file.readlines())
file.close()

#
# file = open("/Users/lavanyamallikharjuna/Downloads/SampleCSVFile_556kb.txt",'a')
# file.write("love amazon")
# print(file.readlines())