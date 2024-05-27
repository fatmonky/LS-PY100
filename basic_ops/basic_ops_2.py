given = 4936
# thousands place
given // 1000 #4

# hundreds place
(given // 100) % 40 #9

# tens place
((given % 4900) - (given % 4930)) // 10 #3

# one place
given % 4930 # 6

#Completely didn't understand the question until seeing the solution. 
# Problem is to extract the individual digits of 4936, without using any other number (other than 10). 

>>> given = 4936
>>> ones = given % 10
>>> ones
6
>>> given
4936
>>> given = given // 10
>>> given
493
>>> tens = given % 10
>>> tens
3
>>> given = given // 10
>>> given
49
>>> hundreds = given % 10
>>> hundreds
9
>>> given = given // 10
>>> given
4
