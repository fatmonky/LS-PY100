def change_to_upper(string):
    if (len(string) > 10):
        return string.upper() # correction: should be return string.upper(), 
                             # rather than origin al print
    else:
        return string

change_to_upper('hello world')
change_to_upper('goodbye')
print(change_to_upper("Sue Smith"))     # Sue Smith
print(change_to_upper("Sue Roberts"))   # SUE ROBERTS
print(change_to_upper("Joe Shea"))      # Joe Shea
print(change_to_upper("Joe Stevens"))   # JOE STEVENS
