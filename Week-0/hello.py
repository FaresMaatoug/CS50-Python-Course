p = input("What is the percentage you want to tip?")

p = (round(float((p.replace('%',''))),2))/100
print(p)