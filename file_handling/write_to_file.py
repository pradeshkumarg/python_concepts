import csv

data = [['Name', 'Age', 'City'], ['John', 32, 'New York'], ['Jane', 28, 'London']]

with open('data.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(data)