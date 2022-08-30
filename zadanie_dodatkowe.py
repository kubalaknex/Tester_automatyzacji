import json

with open("json.txt") as JsonFile:
    data=json.load(JsonFile)


def get_value():
    jsonData = data["rates"]
    for jasonValue in jsonData:
        EValue = jasonValue["mid"]
        save_data.append(EValue)

save_data = []
get_value()
#print(save_data)
rev_save_data = []

for x in reversed(save_data):
    rev_save_data.append(x)

#print(rev_save_data)

i = 99
z = 0

while z<i:
    if rev_save_data[z]>= 4.7 or rev_save_data[z]<=4.5:
        print(rev_save_data[z])
    z += 1
