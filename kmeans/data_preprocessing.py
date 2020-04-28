import csv

csvReader = open("/Users/apple/Downloads/THEFT.csv", "r")
reader = csv.reader(csvReader)

csvWriter = open("/Users/apple/Downloads/THEFT_cleaned.csv", "w")
reader_w = csv.writer(csvWriter)

x = []
y = []
i = 1
for item in reader:
    if reader.line_num == 1:
        continue
    if item[15] == '':
        continue
    x = float(item[14])-41.0
    y = float(item[15])+87.0
    if (x<0.5):
        continue
    i += 1
    # print(x,y)
    tmp = [x, y]
    reader_w.writerow(tmp)
    # if(i >1000
print(i-1)

csvReader.close()
csvWriter.close()