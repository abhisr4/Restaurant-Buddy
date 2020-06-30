

#convert lat and long(str) to float to do numerical computations
dataDict={}
for item in range(len(df)):
    lati=float(data[item][1])
    longi=float(data[item][2])

    data[item][1]=lati
    data[item][2]=longi