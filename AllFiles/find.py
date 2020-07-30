text = "X-DSPAM-Confidence:    0.8475";
place1 = text.find("0")
place2 = text.find("5")
whole = text[place1:place2+1]
con = float(whole)
print(con)