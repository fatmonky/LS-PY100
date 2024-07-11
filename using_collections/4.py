pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

# Part 1: write some code to print Bark by accessing element associated with key Dog
print(pets.get('Dog', "Dog not found!"))

# Part 2: Write some code to print None when you try to print the value associated with the non-existent key, Lizard.
print(pets.get("Lizard", "None"))
# model answer: print(pets.get("Lizard"))
# model answer doesn't have a default value.

# Part 3: Write some code to print <silence> when you try to print the value associated with the non-existent key, Lizard.
print(pets.get("Lizard", "<silence>"))
