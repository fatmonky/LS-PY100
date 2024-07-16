forenames = ['Ken', 'Lynn', 'Pat', 'Nancy']
surnames = ['Camp', 'Blake', 'Flanagan', 'Short']
'''
index = 0
while index < len(forenames):
    if index >= len(surnames): # surnames might be shorter.
        break

    forename = forenames[index]
    surname = surnames[index]
    print(f'{forename} {surname}')

    index += 1
'''
# using zip

joined_names = zip(forenames, surnames)
for forename, surname in joined_names:
    print(f'{forename} {surname}')
