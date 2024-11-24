## Structure that returns True

string = bool("This is a string")
num = bool(1)
list = bool([1, 2, 3])
dict = bool({"a": 1, "b": 2})
tuple = bool((1, 2, 3))
set = bool({1, 2, 3})
bool = bool(True)

print(string, num, list, dict, tuple, set, bool)



## Structure that returns False

string2 = bool("")
""" num2 = bool(0)
list2 = bool([])
dict2 = bool({})
tuple2 = bool(())
set2 = bool(set())
bool2 = bool(False) """

print(string2)