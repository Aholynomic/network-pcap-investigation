# Program to get Latitude and Longitude 
# from the URLs

file = open("locationData.txt","r")
file = file.read()
file = file.splitlines()
fields = ["Latitude", "Longitude"]
location = []
for i in file:
    a = i[-17:]
    a = i.replace(a, " ")
    b = a.replace("%2C",",")
    c = b.replace("HTTP/1.1"," ")
    split_data = c.split("location=")
    location.append(split_data[1])
    
for i in range(len(location)):
    print(location[i])
