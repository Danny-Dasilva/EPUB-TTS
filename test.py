# import re

# class ChapterTitleFixer:
#     def fix_chapter_title(self, title):
#         # Convert all characters to lowercase
#         title = title.lower()
#         # Capitalize the first letter of each word
#         title = title.title()
#         # Remove extra whitespaces
#         title = ' '.join(title.split())
#         return title

#     def process_chapter_titles(self, title):
#         # Check if the title matches the pattern (all caps with first letter separated by a space)
#         match = re.match(r'^([A-Z])\s([A-Z\s]+)$', title)
#         if match:
#             breakpoint()
#             # Fix the title by joining the parts with a single space between them
#             fixed_title = match.group(2) + ' ' + ''.join(match.group(3, 4))
#             fixed_title = self.fix_chapter_title(fixed_title)
#             return fixed_title
#         else:
#             return title

# # Example usage
# chapter_title_fixer = ChapterTitleFixer()
# title = "Introduction  \n T HIRTY YEARS AGO , if you'd asked someo"
# processed_title = chapter_title_fixer.process_chapter_titles(title)
# print(processed_title)


# import re

# text = "Introduction\n T HIRTY YEARS AGO, if you'd asked someo"
# pattern = r'\b([A-Z])\s([A-Z])'

# # Replace the space after the capital letter with an empty string
# result = re.sub(pattern, r'\1\2', text)

# print(result)

import re

# Function to convert a Roman numeral to an integer
def roman_to_int(s):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    for letter in reversed(s):
        value = roman_numerals[letter]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total

# Function to convert an integer to its English word representation (for numbers 1-39)
def int_to_words(num):
    ones_words = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    tens_words = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    
    if num <= 20:
        words = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
                 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen',
                 'Eighteen', 'Nineteen', 'Twenty']
        return words[num]
    elif num < 40:
        tens = num // 10
        ones = num % 10
        word = tens_words[tens]
        if ones > 0:
            word += " " + ones_words[ones]
        return word

# Define the regex pattern for a Roman numeral at the end of a line
pattern = r'([IVXLCDM]+)\s*\n'

# Your test string
test_string = """
XXXVIII  
In the streets - Brassteeth - Los heréticos - A veteran of the late war 
"""

# Function to convert matched Roman numerals to words and prepend "Section"
def roman_to_words(match):
    numeral = match.group(1)
    # Convert the Roman numeral to an integer
    number = roman_to_int(numeral)
    # Convert the integer to words
    word = int_to_words(number)
    return "Section " + word + "\n"

# Replace Roman numerals with "Section" + words
output = re.sub(pattern, roman_to_words, test_string)

# Print the output
print(output)
