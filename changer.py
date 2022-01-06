
# def change(to_change, change_to, file):
#     import csv
#     with open(file, 'r') as f:
#         reader = csv.reader(f)
#         data = list(reader)
#         for row in data:
#             if(str(row[3]).endswith(to_change)):
#                 row[3] = row[3].replace(to_change, change_to)

#     with open(file, 'w') as f:
#         import csv
#         writer = csv.writer(f)
#         writer.writerows(data)


# to_change = "@helpinghands.cm"
# change_to = "@handinhands.cm"
# file = 'data/employees_database.csv'
# change(to_change, change_to, file)

name = "John Doe Loremson ipsum"

print(''.join(i.lower() for i in name.split()))
