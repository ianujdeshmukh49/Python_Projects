
# The Dirty Way
input_string = "Hello Harry! Hello Ron ! Hello Hermione! Hello Ron again!"
count_dict = {}
# convert the string into an array
string_list = input_string.split()
# print(new_list)

for i in range(len(string_list) - 1):
    word_count = 0
    for j in range(len(string_list) - 1):
        if string_list[i] == string_list[j]:
            word_count += 1
    
    count_dict.update({string_list[i] : word_count})

print(count_dict)
    

# #Simple 
from collections import Counter


stripped_string = [word.strip("!") for word in string_list]
counts = Counter(stripped_string)
print(counts)

