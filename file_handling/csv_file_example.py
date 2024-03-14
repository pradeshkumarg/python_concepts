import csv

# read as a normal file
# with open("occupations.csv") as file:
#     a = file.read()
#     print(a)


# use of csv reader
with open("occupations.csv") as csvfile:
    reader = csv.reader(csvfile)
    next(reader) # to ignore the header
    for row in reader:
        print(row[0])