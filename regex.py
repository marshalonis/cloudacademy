import re

pattern = r'a\d+'
text = 'a123b a1234b a12345b'

matches = re.findall(pattern, text)

print(f"Pattern: {pattern}\nText: {text}\nMatches: {matches}\n")