import csv, json, sys

REFERENCE_FILE='dev_reference_full.csv'
CLASS_FILE='albert-base-v2-labels.csv'

def main():

    # Reference
    with open(REFERENCE_FILE, newline='') as csvfile:
        reference = list(csv.reader(csvfile, delimiter=','))

    uuid2index=dict()
    for i in range(1,len(reference)):
        uuid=reference[i][0]
        uuid2index[uuid]=i

    # Class
    with open(CLASS_FILE, newline='') as csvfile:
        Class = list(csv.reader(csvfile, delimiter=','))

    outputFile = open('dev_submission.csv', 'w') #load csv file
    output = csv.writer(outputFile) #create a csv.write
    output.writerow(['Id','Predicted'])  # header row

    for i in range(1, len(Class)):
        uuid=Class[i][0]
        index=uuid2index[uuid]
        if Class[i][1]=='0':
            output.writerow([uuid, reference[index][1]])
        elif Class[i][1]=='1':
            output.writerow([uuid, ''])

if __name__ == "__main__":
    main()
