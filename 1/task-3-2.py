value = int(input())
row_count = 1
row = []
 
for i in range(value**2 - sum(range(value)), 0, -1):  
    row.append(i)  
    if len(row) == row_count:
        line = ' '.join(map(str, row))
        print (f'{line:>{value * 3}}')
        row = []
        row_count += 1