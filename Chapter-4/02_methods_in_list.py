friend=["Apple", "3", "Hello","4.4"]

print(friend)
#append method
friend.append("Samiksha") #add in last
print(friend)

#sort method
l1=[1, 100,45, 86,65]
l1.sort()
print(l1)

#reverse method
l1.reverse()
print(l1)

#insert(in this we can add at middle in append it only add at last)
l1.insert(3, 333)  #(index, insert value)
print(l1)

#pop method: will delete the value in index and return the value

l1.pop(2)
print(l1)
print(l1.pop(2))#if we use print with pop it will show only the value of that index

#remove method

friend.remove("apple")
print(friend)