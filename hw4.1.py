
# File: hw4.1.py
# Author(s): Abhijit Nimbalkar and Sriman

# hw3.1.b
# print("\n1.b:")
records2 = []
with open('expenses.txt', 'rt', encoding='utf-8') as fin:
    for line in fin:
        columns = line[:-1].split(':')
        records2.append(columns)

# for row in records2:
#     print(row)

# hw3.1.d
# print("\n1.d:")
header = records2[0].copy()
data = records2[1:].copy()

# print(header)
# for d in data:
#     print(d)

# hw3.1.e
# print("\n1.e:")

for d in data:
    d[0] = float(d[0])  # change str to float
    
# print(header)
# for d in data:
#     print(d)

# hw3.1.f
# print("\n1.f")
data.sort()
print("{:>8s}  {:8s}  {:10s} {:s}".format(header[0],header[1],header[2],header[3]))
for din in data:
    print("{:8.2f}  {:8s}  {:10s} {:s}".format(din[0],din[1],din[2],din[3]))



# hw3.1.g

categories = set()
for d in data:
    categories.add(d[1])  # column sub-1 contains the categories

print('\nThere are', len(categories), 'expense categories:')
for c in categories:
    print(c)

# hw3.1.h

# dictionary of month number to 3-letter month name string

n2s = { '01': 'Jan',
        '02': 'Feb',
        '03': 'Mar',
        '04': 'Apr',
        '05': 'May',
        '06': 'Jun',
        '07': 'Jul',
        '08': 'Aug',
        '09': 'Sep',
        '10': 'Oct',
        '11': 'Nov',
        '12': 'Dec' }

print("\nKey\tValue")
for i in n2s.items():
    print(i[0] + "\t" + i[1])

# hw4.1.a

# hw4.1.b

# hw4.1.c

# hw4.1.d

# hw4.1.e

# hw4.1.f
