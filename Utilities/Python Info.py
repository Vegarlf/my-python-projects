#---- Utilities for Python--------

#----------------------------------------Learning----------------------------------
#list commands:

#lst.append(x)        # add to end
#lst.extend(iterable) # add many
#lst.insert(i, x)     # add at index
#lst.remove(x)        # remove first matching value
#lst.pop()            # remove & return last
#lst.pop(i)           # remove & return at index
#lst.clear()          # empty list
#lst.index(x)         # index of value (crashes if not found)
#lst.count(x)         # count occurrences
#lst.sort()           # sort in place
#sort(Reverse = True) -- descending
#sort(key = str.lower) -- case insensitive
#lst.reverse()        # reverse in place
#del lst[x]/del lst   # delete list, delete at index

#len(lst)             # length
#sum(lst)             # sum numbers
#min(lst), max(lst)   # min/max
#x in lst             # membership


#SETS---
# .update() adds iterable item to other iterable item, changes original set, excludes duplicate items
# .union() joins sets with other data types as well as sets, and returns set, excludes duplicate items, returns new set
# | -- union  -- cant use with other data types, or *
# .intersection() or & -- keep only duplicates ( & cant be used with different data types), returns new set
# .intersection_update() changes original set
# .difference() or - -- keep everything except duplicates (- cant be used with different data types), returns new set
# .difference_update() changes original set
# symmetric_difference() same as difference but applies to both sets, or ^, but not usable with diff data types
# symmetric_difference_update() changes original set
# isdisjoint() returns wether sets have intersection
# issubset() returns wheter set is a proper subset of another or < /<=
# issuperset() returns wheter set is proper superset of another or >/>=




#dictionaries:

#dct = {
#    "name": "Daivik",
#    "age": 14,
#    "scores": [88, 91]
#}
#dct["name"] = "D"     # change key
#age = dct["age"]      # access key

#dct["city"] = "Delhi"   # add new key
#safe accesss - avoid keyerror:
#dct.get("grade")            # None if missing
#dct.get("grade", "N/A")     # default if missing set to N/A
#d.keys()      # view of keys
#d.values()    # view of values
#d.items()     # (key, value) pairs
#d.update({"a": 1, "b": 2})   # merge/update
#d.pop("a")                   # remove key, return value
#d.popitem()                  # remove last inserted pair
#d.clear()                    # empty dict
#"k" in d                     # membership checks keys
#len(d)                        # number of keys

'''
Escape Characters:
\'
\\
\n
\r -- cariage return
\t -- tab
\b -- backspace
Format Strings:
capitalize() -- first letter --> uppercase
casefold() -- lowercase
center()
count() -- no of times a specified value occurs
encode() -- encoded version of string
endswith()
expandtabs()
find() -- returns index
index() -- returns index
isalnum()
isascii()
isdecimal()
isdigit()
islower()
isnumeric()
isprintable()
isspace()
istitle()
isupper()
join() -- join elements of iterable to end of string
ljust() -- left justified
lstrip() -- left trim
maketrans() -- returns translation table
partition() -- returns tuple where string is partitioned into 3 parts
replace()
rfind(), rindex() -- last position
rstrip()
split()
splitlines()
startswith()
strip()
swapcase()
title()
translate()
upper()
zfill() -- fills string with specified number of 0 values at beginning
'''

'''
Operators:
** -- exponent
// -- floor division
:= -- assigns variable in larger function
and -- True if both statements are true
or -- True if one statement is true
not -- False if statement is true, not(x and y)
is, is not
in, not in 

Binary Operators:
& -- AND
| -- OR
^ -- XOR
~ -- NOT
<< , >> -- shift

Operator Precedence:
* before + , () first
(),  -->  **,  -->  * / // %,  --> + -  --> & ^ |  --> comparison, identity, and membership  --> not  --> and  --> or
evaluated left to right 
'''

'''
dunder methods -- auto applied if defined:
__str__(self): auto applied if defined, used to print meaningful info
__repr__(self): prints string useful for debugging, as the form : class(attributes)
__add__(left side value(self), right side value): auto method for '+' between class objects. can be coded to return new class object, etc. 
__sub__(left, right)
__mul__(left, right)
__truediv__(left, right) -- /
__floordiv__(left,right) -- //
__mod__(left, right) -- %
__pow__(left, right) -- **
__abs__(self) -- abs
__gt__(leftside, rightside) -- magic method for greater than (>)
__eq__(leftsidem rightside) -- magic method for ==
__ne__(left, right) -- !=
__lt__(left,right) -- magic method for < 
__ge__(left,right) -- >=
__le__(left,right) -- <=
__bool__(self): controls "if x:"
__len__(self): magic method for len(classobject)
__getitem__(self, index): get item like list "item[index]"
__setitem__(self, index, value): swap item at index, like "item[index] = value"
__contains__(self, name): "in" keyword
__call__(self, functionparameters): make class callable as function
__delitem__(self, index): del item[index]
#NOTE: __new__, __del__ -- research
__iter__(self): initalises for loop
__next__(self): function for next item in loop.
super()- call function on parent class
'''

# Abstract Classes -ABC, abstractclass
# from abc import ABC, abstractmethod
# class name(ABC)
#   @abstractmethod
#   def func(*args, **kwargs

'''from enum import Enum, auto
class name(Enum)
ATTACK = auto()
HEAL = auto()
RUN = auto()
'''

#--------------------FILE I/O COMMANDS------------------------
#open("filename", "mode")
#mode indicators:
# 'r'  --- read ---- opens file to read, error if doesnt exist
# 'w'  --- write ---- opens file to write NOTE: WIPES THE FILE CLEAN FIRST
# 'a'  --- append ---- opens file to write. adds content to the end
# 'x'  --- create ---- creates a new file. error if already exists
# 'r+' ---- reading and writing --- research later
# use with to not have to close()
# read(), write()


'''
NUMPY--------------:
1.. ARRAY FUNCTIONS:
        2d:
            axis = 0: vert
            axis = 1: hor
        3d:
            axis = 0: layer
            axis = 1: vert
            axis = 2: hor
        np.array() : constructor
        np.ndarray(): allocates memory for array
        slicing: normal, (row, col,) , [:] means all
        np.mean
        np.sum --: axis = None : all, axis = 0: down, axis = 1: left-right
        np.reshape: reshapes array to dimensional format, (-1): wildcard: adjust as neccessary
        np.cumsum -- : shows steps to reach x sum
        array.astype(type) -- casts entire array to data type (truncates float points)
        dot product: np.dot() or @ operator: multiplies and sums in one go, inner dimensions must match
        np.vstack((a,b))-- stacks a on top of b. number of columns must match
        np.hstack((a,b)) -- stacks b to the right of a. number of rows must match
        np.conctatenate() -- master function. lets u choose axes. axis 0 - vstack, axis 1 - hstack. 
        np.split(arr, splitsize, axis) -- strict. errors if size doesnt fully divide array size
        np.array_split(arr,splitsize, axis) -- adjusts split arr size accordingly
        np.where(condition) -- returns tuple of indices
        np.sort(arr) - returns copy, doesnt change original -- axis = 0 -sorts columns, axis = 1 sorts rows
        arr.sort() - changes original and saves.          -- axis same
        np.argsort(arr) - returns indices, can be applied to other arrays, very very very useful
        .arange(start,stop,step) -- [start,stop), but in array
        np.isin(arr, test) - checks in keyword
        np.flatten() - flattens into 1d
        np.ravel() - flattens into 1d
2.. RANDOM FUNCTIONS:
        .randint(low,high,size)
        .rand(size) - floats between [0,1)
        .uniform(low,high,size) - same as .rand() but customizable
        .random.choice(possibilites, size, probabilities) -- p must sum to 1 , i use pythons random.choices to avoid this
        .shuffle(arr) - shuffles original arr
        .permutation(arr) - gives new shuffled arr (idk why it just shuffles rows with 2d arrays, not row values, idk how to fix that tho, maybe indexing and slicing)
        -- all the random distributtion functions are a completely seperate topic, cant be covered here. 
s
3.. SEABORN MODULE FUNCTIONS:
        .distplot(data, kind) -- deprecated:
        .displot(data, kind, param) -- new displot, master plotting func, can plot histograms and line graphs
        .histplot(data, param(label, color, alpha, etc)) -- to plot histograms
        .kdeplot(data, param(label, color, alpha, etc)) -- to plot kde 
        parameters:
            .kdeplot -- bw_adjust: adjusts smoothness of graph low - jagged, high - smooth
            .histplot -- bins: same as bwadjust, number of rectanges drawn
            ---- both bwadjust and bins  are ultimately measures of preciseness to show in the graph
            .kdeplot: cut -- defines cutoff. cut = 0 cuts graph where data ends.
            for both: label, alpha, color, etc..


PANDAS------------------------:
    Series, Dataframe = S, D
    create dataframe with pd.dataframe(data, index)
    access with loc, iloc
    to print as dataframe, slicing (with loc, iloc) must be list within list, but ':' are not within list brackets, rows and columns in seperate lists
    .loc, .iloc alterate mask check - df.loc(mask, column) = x ,  sets column to x if mask
    .fillna(int) - fils NaN with int
    df.groupby(col)
    df.astype()
    df.reset_index()
    pd.merge(left, right, how, on) - left df, right df, on - class by which to merge, must be common.
    df.rename(col = {"OLdcolname": "newcolname"})
    df.set_index() here just mention column name not dataset
    df.drop(col)  -returns copy without col
    import numpy as np
import pandas as pd

party_data = {
    "HP": [150, 60, 90, 100],
    "Mana": [0, 200, 50, 150],
    "Gold": [50, 100, 200, 10]
}
party = pd.DataFrame(party_data, index=["Aragorn", "Gandalf", "Bilbo", "Elrond"])

print("\n\n", party, "\n\n")

Gandalf = party.loc[["Gandalf"], :]
Gold = party.loc[:, ["Gold"]]
Bilbo = party.loc[["Bilbo"], ["HP"]]
party.loc["Gandalf", "HP"] = 50
party.loc[:, "Gold"] += 100
party["Status"] = True
print(f"{Gandalf}\n\n{Gold}\n\n{Bilbo}\n\n")
party.loc["Gandalf", "HP"] = 50
party.loc[:, "Gold"] += 100
party["Status"] = True
party.loc["Aragorn", "HP"] -= 30
party["Gold"] += 50
party.loc["Bilbo", "Mana"] = 0
party["XP"] = 0

party.loc["Legolas"] = [120,80,150,True,0]

gimlistats = {
        "HP": 200,
        "Mana": 0,
        "Gold": 300,
        "Status": True,
        "XP": 0
}

party.loc["Gimli"] = gimlistats

party["HP"] -= 80
party.loc[ party['HP'] <= 0, "Status"] = False
party.loc[ party["Status"] == False, ["Gold", "HP"]] = 0
party.loc[ party["Status"] != False, ["XP"]] += 108

party["Shield"] = np.nan

party.loc[["Aragorn", "Gimli"], ["Shield"]] = 150
party = party.fillna(0)
party = party.astype(int)
#I prefer bool values as 1,0 instead of True False, quicker to read
party["Class"] = "Warrior"
party.loc[["Gandalf", "Elrond"], "Class"] = 'Mage'
party.loc["Bilbo", "Class"] = 'Rogue'

classgroup = party.groupby("Class")
classgroupgoldmean = classgroup[["Gold"]].mean().astype(int).reset_index()
classgroupcount = classgroup[["Status"]].count().reset_index()
classreport = pd.merge(classgroupgoldmean,classgroupcount, on="Class")
classreport = classreport.rename(columns = {"Status": "Count"})

richlist = party.sort_values(by = "Gold", ascending=False)
tanklist = party.sort_values(by = "HP", ascending=False)
ranklist = party.sort_values(by = ["Status", "XP", "Gold", "HP"], ascending=[False, False, False, False])

print(party)
print(f'\n\n')
print(f"{richlist}\n\n{tanklist}\n\n{ranklist}\n\n")


MATPLOTLIB--------------------:
    DRAWING GRAPHS:
        .subplot(row, column, graph) - seperates figure into diff graphs
        .axvline()
        .axvspan()
        .gca().set_ - sets param for axes
        .text(x,y,'text')
        .xticks() sets x tickmarks, or labels
        .title()
        .grid(axis, alpha)
        .xlabel()
        .ylabel()
        .legend()- draws legend -- param: loc:'upper left' -- example
        .show() - shows window



'''