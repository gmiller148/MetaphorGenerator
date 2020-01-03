from string import punctuation
import random

with open('resources/war_peace.txt') as f:
    text = f.read()

text = text.translate(str.maketrans('','',punctuation)).replace('`','',).lower()
words = text.split()
# print(words[100:400])

def generate_markov(words,gram_size=2):
    markov = {}
    for i,word in enumerate(words[:len(words)-gram_size+1]):
        # if i + gram_size < len(words):
        phrase = tuple(words[j] for j in range(i,i+gram_size-1))
        if phrase in markov:
            markov[phrase].append(words[i+gram_size-1])
        else:
            markov[phrase] = [words[i+gram_size-1]]

    return markov

def generate_phrase(markov, phrase_len, gram_size):
    first_section = random.choice(list(markov))
    # print(' '.join(first_section))
    phrase = [word for word in first_section]
    for i in range(gram_size,phrase_len):
        prefix = tuple(phrase[j] for j in range(i-gram_size,i-1))
        if prefix in markov:
            next_word = random.choice(markov[prefix])
        else:
            phrase.append('.')
            phrase.extend(generate_phrase(markov, phrase_len-len(phrase), gram_size))
        phrase.append(next_word)

    return phrase
    # print(phrase)




markov = generate_markov(words, 3)
phrase = generate_phrase(markov, 10, 3)

print((phrase))
# print(markov[('honeymoons',)])


# print(markov[('the',)])