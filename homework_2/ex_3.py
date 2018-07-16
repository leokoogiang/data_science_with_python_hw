s = "the output that tells you if the object is the type you think or not"
# break down the string into a list of words
words=s.split()
# sort the list
words.sort()

# display the sorted word
j = ' '.join(words)
print(j)
print(j.title())

# for word in words:
#     print(word)