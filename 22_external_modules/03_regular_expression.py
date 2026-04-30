# If you gonna dive deeper into regular expression there is an website that you can populate is:  # https://regexr.com/

import re

text = "The quick brown fox jumps over the lazy dog."

# Search for the pattern.

match = re.search("brown", text)
if match:
    print("Match found")
    print("Start Index", match.start())
    print("End Index",  match.end())

# Find all occurrences

match = re.findall("the", text, re.IGNORECASE) # case insensitive
print("Matches:", match)

# Let's change the word from the above sentence.

new_text = re.sub("fox", "cat", text)
print("New Text is:", new_text)  # In this case all the occurrences of any word will be replaced.
