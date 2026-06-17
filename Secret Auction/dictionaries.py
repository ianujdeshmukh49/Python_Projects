sample_dictionary = { 
    'anuj' : '123',
    'rookie' : '100'
    }

# getting a specific group
print(sample_dictionary.get('rookie'))

# getting all keys
print(sample_dictionary.keys())

# getting all values
print(sample_dictionary.values())

# getting all items
print(sample_dictionary.items())

#looping through a dictionary
for key,value in sample_dictionary.items():
    print(f"Key : {key}")
    print(f"Value : {value}")

#add an element in a dictionary
#1)               | When a key is missing this raises an error
sample_dictionary["Tony Stark"] = "4562"
print(sample_dictionary)

#2) 
sample_dictionary.update({'Jarvis':'4563'})
print(sample_dictionary)


#removing elements from a dictionary

#1) using del
del sample_dictionary["Tony Stark"]
print(sample_dictionary)

# When a key is missing this raises an error
# del sample_dictionary["Bruce Banner"]
# print(sample_dictionary)

'''
Traceback (most recent call last):
  File "/workspaces/Python_Projects/Secret Auction/dictionaries.py", line 39, in <module>
    del sample_dictionary["Bruce Banner"]
'''

#2) using 'pop'
sample_dictionary.pop('Jarvis')
print(sample_dictionary)

sample_dictionary.pop('Bruce Banner',None)
print(sample_dictionary)

