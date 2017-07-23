# Initialize your dictionary with keys and values
wordDict = {
	"ramify": "spread or branch out", 
	"consequence" : "a result or affect" 
}

# Print the dictionary
for word, meaning in wordDict.items():
	print ("The word is: ", word, " and the meaning is: ", meaning)

# Ask for input to search a word
findWord = input("Enter word to find: ")

# Finding the value for a key in a dictionary 
print ("Meaning is: ", wordDict[findWord])

# Add a new word to the dictionary
newWord = input("Enter word to add: ")
newWordMeaning = input("Enter meaning for new word: ")

# Add to dictionary
wordDict[newWord] = newWordMeaning

# Print the dictionary
for word, meaning in wordDict.items():
	print ("The word is: ", word, " and the meaning is: ", meaning)
