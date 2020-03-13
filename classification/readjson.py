import csv, json, sys

JSON_FILE='data/train-v2.0.json'
OUT_FILE='data/train-v2.0_short.json'

def main():
    fileInput = JSON_FILE
    inputFile = open(fileInput) #open json file
    data = json.load(inputFile) #load json content
    inputFile.close() #close the input file

    data['data'] = data['data'][:1]

    with open(OUT_FILE, 'w') as f:
        json.dump(data, f)

if __name__ == "__main__":
    main()
