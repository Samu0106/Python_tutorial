marks={
    "Samu": 100,
    "Ritu": 70,
    "Dudu": 85
}

print(marks.items())  #Returns a list of (key,value) in tuples.
print(marks.keys()) # print the keys
print(marks.values()) # print the values of keys

# update : Updates the dictionary with supplied key-value pairs
marks.update({"Samu": 99})
print(marks) # we can add key pair by update({"Samu":99, "R: 100"})

# get: Returns the value of the specified keys (and value is returned )

print(marks.get("Samu"))

# what is the differnce in 
print(marks.get("Samu"))
print(marks["Samu"])  
# when we run this it will show same value and answer is right
#but if we change the key that does not exist [] will return error and get() will print none