# Q no. 1.)
# Define the string
s = "PythonPractice"

# Indexing and slicing
print("s[1] =", s[1]) # Output: 'y'
print("s[-3:] =", s[-3:]) # Output: 'ice'
print("s[2:7] =", s[2:7]) # Output: 'thonP'

# 2.) Reverse a string.
#one liner code to reverse "developer"
print("developer"[::-1])

# 3.)Count Vowels
  # Write a function that counts the number of vowels in a given string.

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
text=input("Enter a string:")
vowel_count=count_vowels(text)
print("Number of vowels:", vowel_count)

#4.) Check for Palindrome
   #Write a function to check if a given string is a palindrome. Ignore spaces and capitalization.
def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

user_input = input("Enter a string to check if it's a palindrome: ")

if is_palindrome(user_input):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

# 5.) Clean and Format String
   #Given text = " hello world! welcome to Python. ", write code to:
#    - Remove leading/trailing spaces
#    - Capitalize each word
#    - Replace the word "Python" with "Programming"
text = " hello world! welcome to Python. "

text = text.strip()

text = text.title()

text = text.replace("Python", "Programming")

print(text)

# 6.) Find Longest Word
   #Write a function that takes a sentence and returns the longest word in it.
def find_longest_word(sentence):
    words = sentence.split()
    cleaned_words = [word.strip(".,!?;:") for word in words]
    
    if cleaned_words:
        return max(cleaned_words, key=len)
    else:
        return ""
user_input = input("Enter a sentence: ")

longest = find_longest_word(user_input)
print("The longest word is:", longest)

#7.) String Operators
#    Given s1 = "Py" and s2 = "thon", what are the results of:
#    - s1 + s2
#    - s1 * 3
#    - "y" in s1

# Given strings
s1 = "Py"
s2 = "thon"

result1 = s1 + s2           
result2 = s1 * 3            
result3 = "y" in s1          

print("s1 + s2 =", result1)
print("s1 * 3  =", result2)
print('"y" in s1 =', result3)

#8.)Remove Duplicate Characters
  # Write a function that removes all duplicate characters from a string but keeps the first occurrence.

def remove_duplicates(s):
    result = ""
    seen = set()
    for char in s:
        if char not in seen:
            seen.add(char)
            result += char
    return result

user_input = input("Enter a string: ")

output = remove_duplicates(user_input)
print("String after removing duplicates:", output)

#9. Check for Anagram
  # Write a function that returns True if two strings are anagrams of each other.
def are_anagrams(str1, str2):

    cleaned_str1 = ''.join(c.lower() for c in str1 if c.isalnum())
    cleaned_str2 = ''.join(c.lower() for c in str2 if c.isalnum())
    

    return sorted(cleaned_str1) == sorted(cleaned_str2)

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if are_anagrams(s1, s2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

# 10.) #Word Frequecy Counter
#wriet a functon that takes a sentence and returns a dictiionary of word frequencies.
def word_frequencies(sentence):
    
    words = sentence.lower().split()
    
    freq = {}
    for word in words:
        # Remove common punctuation from each word
        word = word.strip(".,!?;:\"'()[]{}")
        if word:  # skip empty strings
            freq[word] = freq.get(word, 0) + 1
    return freq


user_sentence = input("Enter a sentence: ")


frequencies = word_frequencies(user_sentence)


print("Word frequencies:")
print(frequencies)


