"""
Python & Regexp

[x] Regexp quick start

[x] Filter text with regexp

[x] Extract parts of text using regexp
"""

# A word that starts with a

# A word that ends in a capital letter

# Same letter that appears multiple times in a row

# ---------
# Pattern Rules
import re
import sys
# . => [all characters in the world]
pat = re.compile(r"\b[A-Z][a-zA-Z]+\b")

# https://docs.python.org/3/howto/regex.html

for line in sys.stdin:
    if m := pat.search(line):
        print(f"🥇️ {line}", end='')
        print(m.group(0))
    else:
        print(f"👎🏼 {line}", end='')





