#convert kilometer to mile 
def convert(km):
    mile = km * 1.6
    print(km, "Kilometer is equal to %.2f" %mile , "mile")

km = float(input("Please enter kilometer: "))
convert(km)
