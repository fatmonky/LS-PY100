"""
Explain why the code below prints different values on lines 3 and 4.

text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29

"""

# my answer
# line 3 first slices text from starting index 21 till 34, creating a new string, and then finds 'f' in the new string. 'f' is then in index 8 of the new string. 
# line 4 searches from the back of string 'text', from index position 21 till 34, and finds 'f' in index 29 of the original string 'text'. 
