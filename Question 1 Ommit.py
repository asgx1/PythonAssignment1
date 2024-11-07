def remove_vowel(text):
    vowels="aiuoeAOUEI"#vowels in upper and lower case
    result= ''.join([char for char in text if char not in vowels])#join char with out vowels
    return result
text=input("enter your text: ")#input the text
print(remove_vowel(text)) # text withou vowels