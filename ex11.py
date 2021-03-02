import json
file = open("dictionary.txt", "r")
cont = file.read()
dicti = json.loads(cont)
file.close()
freq={}

def get_all_keys(dictio):
    for z, value in dictio.items():
        if type(value) is dict:
            get_all_keys(value)
            if (z in freq):
                freq[z] += 1
            else:
                freq[z]=1
        elif (z in freq):
            freq[z] += 1
        else:
            freq[z]=1
        if type(value) is list:
            for j in range(len(value)):
                if type(value[j]) is dict:
                    get_all_keys(value[j])

get_all_keys(dicti)
keyWithMaxValue = max(freq.items(), key=lambda x: x[1])
KeysWithMaxFreq = list()
for key, value in freq.items():
    if value == keyWithMaxValue[1]:
        KeysWithMaxFreq.append(key)

print(KeysWithMaxFreq)
