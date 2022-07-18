

print("Welcome to tip calculator")
a = input("What was your total bill? $")
a=float(a)
b =input("What percentage tip you would like give? 10, 12, or 15? ")
b=int(b)
c = input("How many people to split the bill? ")
c=int(c)
b =round(float(a*(b/100)),2)
a =a+b
c =a/7
print(f"Each person should pay: ${c} ")