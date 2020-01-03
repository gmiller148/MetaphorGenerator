import ast

with open('resources/terms.txt') as f:
    terms = ast.literal_eval(f.read())

with open('resources/nounlist.txt') as f:
    nouns = f.read()

nouns = set(nouns.split('\n'))

nouns.remove('')

for i in range(10):
    term = terms.pop()
    noun = nouns.pop()
    print(f'The {term} is like a {noun} if you think about it.')

# if __name__ == '__main__':
#     pass