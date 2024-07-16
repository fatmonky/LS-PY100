cats_colors = {
    'Tess':   'brown',
    'Leo':    'orange',
    'Fluffy': 'gray',
    'Ben':    'black',
    'Kat':    'orange',
}

names = [ name.upper() for name, color in cats_colors.items() if color == 'orange' ]
print(names)
names2 = [ name.upper() for name in cats_colors 
          if cats_colors.get(name, "nil") == 'orange'
          if name[0] == "L"]
print(names2)
