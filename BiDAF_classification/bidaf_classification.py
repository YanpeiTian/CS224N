import json

INPUT_FILE='predictions_.json'

def main():
    inputFile = open(INPUT_FILE) #open json file
    data = json.load(inputFile) #load json content
    for key in data.keys():
        if len(data[key])<2:
            print(key)

if __name__ == "__main__":
    main()
