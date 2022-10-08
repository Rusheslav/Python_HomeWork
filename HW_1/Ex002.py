values = [0, 1]

count = 0
for X in values:
    for Y in values:
        for Z in values:
            if not (X or Y or Z) == ((not X) and (not Y) and (not Z)):
                print(f'Утверждение верно при X = {X}, Y = {Y}, Z = {Z}')
                count += 1

if count == 8:
    print('Утверждение истинно')
else:
    print('Утверждение ложно')
