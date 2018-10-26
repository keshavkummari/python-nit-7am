import re

text = 'abbaaabbbbaaaaaab'

pattern = 'ab'

for i in re.findall(pattern, text):
    print('Found "%s"' % i)
