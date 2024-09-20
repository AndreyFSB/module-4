value = int(input())
count = 1
rows = []
 
for i in range(value, 0, -1):
    row = []  
    for _ in range(i):        
        row.append(count)
        count += 1
    rows.append(reversed(row))    
       
for row in reversed(rows):    
    r = ' '.join(map(str, row))      
    print(f"{r:>{value * 3}}")