'''sh = input ("Enter hours")
sr = input("enter rate")

fh = float(sh)
fr = float(sr)
if fh > 40:
    reg = fh * fr
    otp = (fh-40) * (fr*0.5)
    xp = reg + otp
else:
    xp = reg
print(xp)'''

score = input("Enter a score between 0.0 to 1.0")
try:
    fs = float(score)
    if fs > 1.0:
        print("out of range")
    elif fs >= 0.9:
        print("A")
    elif fs >= 0.8:
        print("B")
    elif fs >= 0.7:
        print("C")
    elif fs >= 0.6:
        print("D")
    else:
        print("F")
except ValueError:
    print("invalid number")
    


