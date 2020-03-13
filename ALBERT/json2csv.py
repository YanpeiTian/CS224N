import csv, json, sys

JSON_FILE='test-3.json'
CSV_FILE='test_submission.csv'

def main():
    fileInput = JSON_FILE
    fileOutput = CSV_FILE
    inputFile = open(fileInput) #open json file
    outputFile = open(fileOutput, 'w') #load csv file
    data = json.load(inputFile) #load json content
    inputFile.close() #close the input file
    output = csv.writer(outputFile) #create a csv.write
    output.writerow(['Id','Predicted'])  # header row

    for uuid in sorted(data):
        output.writerow([uuid, data[uuid]])


if __name__ == "__main__":
    main()
