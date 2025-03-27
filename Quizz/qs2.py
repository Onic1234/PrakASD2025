sentence = "Programming in python is fun and beneficial."

# Count the number of words in the sentence
def count_words(sentence):
    count = sentence.split()
    return len(count)
print("Number of words in the sentence: ", count_words(sentence))

# Find and count the number of vowel letter (a, i, u, e, o) in the sentence
vowels = "aiueo"
vowel_count = 0
for i in sentence:
    if i in vowels:
        vowel_count += 1
print("Number of vowels in the sentence: ", vowel_count)

# Reserve the order of words in the sentence without using.split() and .reverse().
sentence = sentence + " "
word = ""
sentence_baru = ""
for i in sentence:
    if i != " ":
        word += i
    else:
        sentence_baru = word + " " + sentence_baru
        word = ""
print("Reversed sentence: ", sentence_baru)

# Replace every vowel letter with the character * and print the results
sentence_baru = ""
for i in sentence:
    if i.lower() in vowels:
        sentence_baru += "*"
    else: 
        sentence_baru += i
print("New sentence: ", sentence_baru)
