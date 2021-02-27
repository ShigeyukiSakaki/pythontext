import re

text = "the ghost that says boo haunts the loo"

words = re.findall("\s.oo", text)
for word in words:
    print(word)
