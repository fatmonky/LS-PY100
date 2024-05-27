obj = 'ABcd' #reassigns
obj.upper() #neither
obj = obj.lower() #reassign
print(len(obj)) #neither
obj = list(obj) #reassign & mutates obj
obj.pop() #mutates value of obj that obj now references
obj[2] = 'X'#reassigns obj element and mutates obj
obj.sort() #mutates obj
set(obj) #neither
obj = tuple(obj) #reassign and mutates obj
