#1. Tried .count but didn't work. 
#model answer: len(people)

#2. short answer is no, because tuples are immutable. 
#model answer: convert to list, mutate, then convert back to tuple.

#3. 2 differences: lists are mutable, tuples are immutable. 
# model answer: lists are [], tuples are () #!! 
# 2 similarities: both are sequences. both can be heterogeneous. 

#4. strings are indexed, and chars can be accessed through indexes

#5. sets are not ordered

#6. 
#pi = 3.141592
#str_pi = str(pi)

#7. 
#range(7) #0,1,2,3,4,5,6
#range(1,6) #1,2,3,4,5
#range(3,15,4) #3,7,11
#range(3,8,-1) #3, 2, 1,0) #wrong: will be a []
#range(8, 3, -1) #8,7,6,5,4

#8. 
#print(list(range(3, 17, 4)))

#9. 
#9.1. they should be equal.
#9.2. they should be different objects.
#9.3. equal
#9.4. different objects #WRONG. "The two nested lists are the same object: the list constructor creates a shallow copy of the iterable passed as an argument. Shallow copies don't create new nested lists. Instead, only a reference to the nested list gets copied."

#10. No it won't necessarily, since names is a set and sets are not ordered. 

#11. 
name_ctry = {
        "Alice":"USA",
        "Francois": "Canada",
        "Inti": "Peru",
        "Monika": "Germany",
        "Sanyu": "Uganda",
        "Yoshitaka": "Japan",
        }
print("OK" if name_ctry["Alice"] == "USA" else "Uh oh!")
