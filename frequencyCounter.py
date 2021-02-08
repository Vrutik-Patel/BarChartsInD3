import csv

# Create frequency dictionary

myDict = {}
with open('dataset_2_with_urls.csv') as csv_file: # Choose which dataset to read from
    csv_reader = csv.reader(csv_file, delimiter=',')
    # The line counts verify that the entire file is being read
    line_count = 0
    count = 1
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        elif(row[10].strip(" ") == "True"):  # Change what value of row you're looking for (In this case True or False)
            print(row[10].strip(" ") + str(line_count))
            line_count += 1
            if(not (row[12] in myDict)): # If not in row and True
                myDict[row[12]] = 1
                print(row[10].strip(" ") + " " + str(count))
                count += 1
            else:
                print(row[10].strip(" ") + " " + str(count))
                count += 1
                myDict[row[12]] += 1
    

# Write Frequency dictionary to separate .csv
# Choose the Output file based on inputs
with open('TRUE_Dataset2.csv', mode='w' , newline='') as csv_file1: 
    fieldnames = ['URLs', 'Frequency']
    writer = csv.DictWriter(csv_file1, fieldnames=fieldnames)

    writer.writeheader()
    for x,y in myDict.items():
        writer.writerow({fieldnames[0]: x, fieldnames[1]: y})
