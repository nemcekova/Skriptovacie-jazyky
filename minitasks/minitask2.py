import re
pattern = re.compile(r'du')
text = ['du du du', 'du po ledu', 'dopředu du', 'i dozadu du', 'dudu dupl']
for row in text:
    print(re.sub(pattern, 'DU', row))
