# Qn 1: should get an error, as foo is internal to set_foo's scope.
# Qn 2: program should print "bar"
foo = "bar"

def set_foo():
    foo = "qux"

set_foo()
print(foo)
