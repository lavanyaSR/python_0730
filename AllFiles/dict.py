#key value pair
# dict = {'mehek':1,'Anya':2,'shera':3}
# print(dict['mehek'])
# dict['stef'] = 4
# print(dict['stef'])
# dict['stef']=5
# print(dict['stef'])

#histogram - count the word number of times it appeared
# counts = dict()
# names = ['anya','stef','rina','rina','rina','stef']
# for name in names:
#     if name not in counts:
#         counts[name]=1
#     else:
#         counts[name] = counts[name]+1
# print(counts)

#with get word
# counts = dict()
# names = ['anya','stef','rina','rina','rina','stef']
# for name in names:
#     counts[name]=counts.get(name,0)+1
# print(counts)

# # count the words in given text
# counts = dict()
# line = input("Enter a text")
# words = line.split()
# for word in words:
#     counts[word] = counts.get(word,0)+1
# print(counts)

#get the keys and values
dict = {'mehek':1,'Anya':2,'shera':3}
print(dict.keys())
print(dict.values())

for a,b in dict.items():
    print(a,b)

lis = [1,2.3,'anya']
print(lis)