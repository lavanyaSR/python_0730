'''def thing():
    print("Hello")
    print("There")

thing()
print("Zen")
thing()

big = max("Hello world")
print(big)
big = min("Hello world")
print(big)

def greet(lang):
    if lang == "eng":
        print("Hello")
    elif lang == "fran":
        print("Bon")
    elif lang == "hin":
        print("Namaskar")
greet('eng')
greet('hin')

def talk():
    return("Hello")

print(talk(),"Sravi")

def tell(lan):
    if lan == 'en':
        return "Hello"
    elif lan == 'fr':
        return 'Bonjour'
    else:
        return 'Namasthe'
print(tell('en'),'Sravi')
print(tell('et'),'anya')

def yell(a,b):
    addend = a+b
    return addend
print(yell(3,4))'''

'''while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done! ')

while True:
    line = input('> ')
    if line[0] == '#':
        continue
    elif line == 'done':
        break
    print(line)
print("Done!")

#finding maximum number
large = 0
#gen = ['1','45','67']
for i in [1,23,45,65]:
    if i > large:
        large = i
print("max number ",large)

#sum of all variables
zen = 0
for j in [23,34,45,56]:
    zen = zen + j
    print(j,zen)
print(zen)

#loop in a loop
for i in [12,23,34,67]:
    if i > 40:
        print(i)

#finding minimum number - diff between == and is is: will check not only value but type also. 
#use is on boolean and none type
smallest = None
for i in [100,3,5,7,10]:
    if smallest is None:
        smallest = i
    elif i < smallest:
        smallest = i
    #print(smallest)
print(smallest)

biggest = None
for i in [100,3,5,7,10]:
    if biggest == None:
        biggest = i
    elif i > biggest:
        biggest = i
    #print(smallest)
print(biggest)

small = 0
#gen = ['1','45','67']
for i in [-1,23,45,65]:
    if i < small:
        small = i
print("max number ",small)

# Strings
fruit = 'apple'
for i in fruit:
    print(i,end ='')

x = input("Enter char to search for")
fruit = 'apple'
for i in fruit:
    if x in fruit:
        pass
print("success")
#make upper/ lower
print(fruit.upper())
#slicing
print(fruit[1:3])
#find method
fruit = 'Apple'
print(fruit.find('ap'))
print(fruit.find('Ap'))
#replace
rep = fruit.replace('Ap','Ba')
print(rep)
print(fruit)
#white space
veg = '   Tindora   '
print(veg)
rt = veg.rstrip()
print(rt)
rt = veg.lstrip()
print(rt)
rt = veg.strip()
print(rt)
#startswith
there = "once upon a time"
print(there.startswith("once")) 

data = "from stephen.com@claires Sat Jun 5 10:10:10 2008"
test = data.find('@')
print(test)
spos = data.find(" ",test)
print(spos)
print(data[test+1:spos])

fpos = data.find('f')
print(fpos)
sepos = data.find(' ',fpos)
print(sepos)
tpos = data.find('.',sepos)
print(tpos)
print(data[sepos+1:tpos])  

sh = input("enter hours")
sr = input("enter rate")
fh = float(sh)
fr = float(sr)

def computepay(hour, rate):
    if hour > 40:
        reg = hour * rate
        otp = (hour - 40) * (rate * 0.5)
        pay = reg + otp
    else:
        pay = hour * rate
    return pay
xp = computepay(fh,fr)
print(xp)  '''

# finding max and min numbers from user input

num = 0
smallest = None
biggest = -1
while True:
    num = input("enter numbers")
    if num == 'Done':
        break
    try:
        numb = int(num)
    except:
        print("invalid number")
    if smallest is None:
        smallest = numb
    elif numb < smallest:
        smallest = numb
    elif numb > biggest:
        biggest = numb
print("smallest ",smallest)
print("Biggest",biggest)





