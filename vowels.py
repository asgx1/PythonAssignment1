def remove_vowels(text):
    vowels = "AEIOUaeiou"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result

input_text = input("Enter text: ")
output_text = remove_vowels(input_text)
print("Text without vowels:", output_text)
