# dictionary uses the key, value relationship.  you can retrieve the value by using the
# key but you cannot retrieve the key by using the value.  anything can be used as a key
# and you can store anything as a value.
#
# dictionaries can also be referred to as:
# - lookup-table
# - map
# - content-addressible storage
# - relation
# - hash
# - also: associative array, symbol, table
#
# although the above list are names that may be used to refer to a dictionary, it does not
# mean that they are the same as dictionary. important to note is that dictionaries do not
# actually store the data in any sorted order, and even though you may create a dictionary
# with a certain order, when you call or get back the dictionary it may not resemble the
# order in which you put it in.
#
# below i am building a simple dictionary:

# for reading purposes i am breaking up the length of the line for the dictionary definition.
# this is only for readability.
dictionary = {"one": "uno",
              "two": "dos",
              "three": "tres"}

# to return a value then you must use the name of the dictionary and the key and that will retrieve
# the value associated to that key. below i will be retrieving the value for the "three" key.
print dictionary["three"]

# to delete from the dictionary you can use the 'del' keyword. below i am deleting some of the entries
# again by using the key of the dictionary and not the value.
# first i will print what the dictionary actually currently looks like.
print dictionary
# now i will use the del command to remove entries in the dictionary
del dictionary["one"]
del dictionary["two"]
# and now reprint to show what the new dictionary looks like
print dictionary
print "#####################################################################"
print

########################################################################################################################
# here i will looking at dictionaries as a map. in the first dictionary i am creating a key value relationship
# of courses to professors. now because the course is the key then only one course can exist per key, however
# there may be multiple entries for the same professor. therefore it is important to think of the key as a type
# primary key in database.
course_professors = {"calculus":        "Prof. Kotter",
                     "diff eq":         "Prof. Feeny",
                     "linear algebra":  "Prof. Kotter",
                     "real analysis":   "Prof. Crabtree"}
# the second dictionary is a key value relationship of student to list of courses. interesting because this
# is the first time that i am using a list as value.
student_courses = {"vinnie":    ["calculus", "diff eq"],
                   "arnold":    ["calculus", "linear algebra"],
                   "juan luis": ["real analysis"]}
# now in the above example i created the "student_courses" dictionary by using a list. however, the problem is
# that lists do not enforce uniqueness and therefore a student may show up as taking the same course more than
# once and this is not possible.  therefore the re-assignment of the student_courses dictionary below will use a
# set which uses the {} curly braces, much like the dictionary, however have no key, value stored. only one
# set of unique data.
student_courses = {"vinnie":    {"calculus", "diff eq"},
                   "arnold":    {"calculus", "linear algebra"},
                   "juan luis": {"real analysis"}}
# now i am going to print both dictionaries that i have created so far:
print student_courses
print course_professors

# now this code will create a student_professors dictionary by using the above two dictionaries. first i wil
# start off with a blank dictionary.
student_professors = {} # which student has which professor

# in the for loop below the first line is actually iterating over the keys in the dictionary. so if you have
# a dictionary and you want to iterate through each key then all that one has to do is simply use the name
# of the dictionary with nothing else in order to iterate through each key. now notice the second line actually
# has the square brackets [] and in the square brackets is the key that is coming from the first for loop.
for student in student_courses:
    for course in student_courses[student]:
        # this if statement will look to see if a student key has already been created
        # if it has not then it will go ahead and create that key. however, if it does
        # already exist then it will skip because that means that we can just add information
        # to an already defined key.
        if student not in student_professors:
            # create the student as a key and then create a set to place the professor values in
            student_professors[student] = set()
        # now add the set value to the student key.
        student_professors[student].add(course_professors[course])
# now i will print "student_professors" new dictionary to see what it looks like.
print student_professors
print "#####################################################################"
print

########################################################################################################################
# creating dictionaries
# simple:
xs = {1: 1, 2: 4, 3: 9}
print xs
# using the dict() method:
xs = dict(one="uno", two="dos") # the key must be a valid string cannot be a number or int.
print xs
# another way to create dictionaries is to use a list of tuples: [(),(),()] - in this example the list is the square
# brackets and the tuple is the round brackets found inside the list.  the first value in the tuple inside the list,
# will be the key. in the example below "uno", "dos", "tres" area all the keys and the others are the values.
xs = dict([("uno", "one"),
           ("dos", "two"),
           ("tres", "three"),])
print xs
# now we will create a dictionary using a collection as its keys. in the example below first i import from the
# string module the ascii_lowercase. then when i create the dictionary i use the ascii_lowercase to create the keys
# using the .fromkeys method available to the dict. the second parameter in the fromkeys method is the value in the
# dictionary that i just created.
from string import ascii_lowercase
xs = dict.fromkeys(ascii_lowercase, 0)
print xs

# in dictionaries it is important to remember that keys need to be hashable, however, values are not restricted.
# so you can map a key to list, but not a list to a value.
#
# in the below example i am passing an existing copy to a new dictionary. this is known as a shallow copy of the
# dictionary.
xs = {1: 1, 2: 4, 3: 9}
ys = dict(xs)
print ys
# now the .update function actually updates the dictionary using the .update method with another dictionary.
# if the dictionary already has a value for a key in the dictionary that we are copying from, then it will
# overwrite the value for that key. if there is a key in the dictionary that is using the .update method
# then it will still be there after the update. see examples below:
xs = {1: 1, 2: 4, 3: 9}
ys = {}
# in this case the ys dictionary is empty so using the .update will just copy over all the key value pairs
# from the xs dictionary.
ys.update(xs)
print "the ys dictionary: ", ys
# resetting the ys dictionary.
ys = {}
# now i will add two key value pairs. one that will be replace when using the .update method and the other
# that will not be replaced because it is not in the dictionary that we are updating from.
ys = {1:0, 4:16}
print "the original ys: ", ys
# after the next line the key value pair 1:0 should be changed to 1:1 and the 4:6 should stay the same.
ys.update(xs)
print "the ys dictionary: ", ys
print "#####################################################################"
print

########################################################################################################################
# below is a bit of code that will show all the methods that are available to the dictionary. this piece of
# code can be used with other stuff in python as well just need to change what is inside the dir(changethis)/
#
# this will print out all the methods including the internal implementation methods. the ones with the
# double underscore.
print dir({})
# and this will only print the methods that do not have the double underscore
print [attr for attr in dir({}) if '__' not in attr]
print "#####################################################################"
print

########################################################################################################################
# dict.clear clears the contents of the dictionary without actually destroying the dictionary. therefore the
# dictionary object will still exist. in contrast the reassignment will actually create a new object in memory
# and will orphan the one that it was assigned to. the clear keeps the same dictionary but wipes it clean

########################################################################################################################
# dict.copy creates a shallow copy. what this means is that only the keys will copied and if the values are
# at the level of the keys, meaning the values are not another dictionary, then they too will be copied to
# the new dictionary. however if the value of the dictionary is actually another dictionary and you clear based
# on the key then it will reflect in the ys dictionary.
xs = {1:1, 2:4, 3:9}
ys = xs.copy()
print "the ys before i clear out the xs ", ys
# no i will clear the xs and then reprint the ys to see what it looks like.  you will see that it is still all
# there.
xs.clear()
print "the ys after i clear out the xs ", ys
# however in the next example i am creating a dictionary that has a value another dictionary.
xs = {"one": {"spanish":"uno",
              "german":"ein",
              "french":"un"}}
ys = xs.copy()
# now i am clearing the second dictionary in xs:
xs["one"].clear()
print "the ys after clearing the second dictionary: ", ys
print "#####################################################################"
print

########################################################################################################################
# the dict.get method gets the value if one exist and if it does not then by default returns None. however, we
# can get the dict.get method to return a default method of our choosing. this method should only be used if
# there is a sensible default and not to be used to bypass an exception.
xs = {1:1, 2:4, 3:9}
# if i use the xs.get method here and actually use a correct key then i will get the corresponding
# value.
print xs.get(2)
# however if i use a key that is not in the dictionary i will get None returned.
print xs.get(9)
# to avoid the None i can set my own default, in this case i choose what i want to return if the key
# is not in the dictionary
print xs.get(9, "my_default")
print "#####################################################################"
print

########################################################################################################################
# the dict.pop method retrieves the element at the key and also removes it at the same time.
# in the example below there are three key value pairs and the pop method will pop the element that matches the key.
xs = {"uno":"one", "dos":"two", "tres":"three"}
# print out the dictionary to see what I get
print "printing the xs dictionary before i pop ", xs # i get {'dos': 'two', 'tres': 'three', 'uno': 'one'}
xs.pop("uno") # this will not print unless i use the print method
print "print the xs dictionary after the pop", xs
# with the pop method we can also send as a parameter a default value that we want displayed if the key is not
# there. in the example below i will be trying to pop the value with the "uno" key again but will set a default.
xs.pop("uno", "myDefault") # this will not print unless i use the print method
# use the print method for the line above
print xs.pop("uno", "myDefault") # this line will actually print "myDefault"
# the popitem method is similar, however, when used with the print method it will print out both the key and the
# value. this method cannot guarantee which item is being popped, because the popitem method only takes
# self as a parameter.
print xs.popitem() # don't know which one it will pop
print "#####################################################################"
print

########################################################################################################################
# in this segment we will be looking at iterkeys, itervalues, iteritems, viewkeys, viewvalues, viewitems.
# when iterating over a dictionary it will always iterate over the keys. the next example shows this to
# be true
xs = {"uno":"one", "dos":"two", "tres":"three"}
for key in xs: # the word key is arbitrary and does not mean it is there to specify we want the key from the dictionary
    print(key)
# in python 2 the .keys() method actually creates a copy of the list and therefore may take an impact on
# performance depending the size of the dictionary. therefor a solution is to use the iterkeys, itervalues and
# iteritems instead so that no copy is taken and only the key is looked at in the for loop.
print "going to iterate through the keys of ",xs
for key in xs.iterkeys():
    print key
# look at the values in the dictionary
print "going to iterate through the values of ",xs
for value in xs.itervalues():
    print value
# look at the items (key value pair)
print "going to iterate through the items of ",xs
for item in xs.iteritems():
    print item
# the viewkeys, viewvalues and viewitems are actual views into the dictionary. what this means is that if the
# dictionary changes then it will retain the changes in the new dictionary
xs = {"uno":"one", "dos":"two", "tres":"three"}
# creating the dictionary ys and passing it a view (a view in this case is constant, so what this means
# is that if xs is changed in any way then it will reflect in dictionary ys. however if xs is reassigned
# a new dictionary object then it will not reflect in ys
ys = xs.viewkeys()
print "printing the original ys after the viewkeys method ", ys
# manipulating xs to add another item {"cuatro":"four"}
xs["cuatro"] = "four"
print "printing out the xs dictionary with the changes ", xs
print "printing out the ys dictionary after the changes to xs ", ys
# now i will assign xs a whole new dictionary object
xs = {"not":"in", "the":"first", "dict":"xs"}
print "the new xs ", xs
# when i print ys dictionary i should see the old xs values
print "the ys dictionary after the xs was changed ", ys
# watch the last part of Dict.Keys, Dict.Values and Dict.Items for the last example of deleting items from
# a dictionary
