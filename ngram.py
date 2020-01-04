from string import punctuation
import random

with open('resources/speeches.txt') as f:
    text = f.read().replace('\n',' ').lower()

# text = text.translate(str.maketrans('','',punctuation)).replace('','',)
words = text.split()

def generate_markov(words,gram_size=2,markov=None):
    markov = {} if markov is None else markov
    for i,word in enumerate(words[:len(words)-gram_size+1]):
        # if i + gram_size < len(words):
        phrase = tuple(words[j] for j in range(i,i+gram_size-1))
        if phrase in markov:
            markov[phrase].append(words[i+gram_size-1])
        else:
            markov[phrase] = [words[i+gram_size-1]]

    return markov

def generate_markov_sentences(text, gram_size=2):
    markov = {}
    sentences = text.split('.')
    for sentence in sentences:
        words = sentence.split()
        # print(sentence)
        # words.append('.')
        markov = generate_markov(words,gram_size,markov)
    
    return markov


def generate_phrase(markov, phrase_len, gram_size):
    first_section = random.choice(list(markov))
    # print(' '.join(first_section))
    phrase = [word for word in first_section]
    for i in range(gram_size,phrase_len):
        prefix = tuple(phrase[j] for j in range(i-gram_size,i-1))
        if prefix in markov:
            next_word = random.choice(markov[prefix])
            phrase.append(next_word)
        else:
            phrase.append('.')
            phrase.extend(generate_phrase(markov, phrase_len-len(phrase), gram_size))
        

    return phrase
    # print(phrase)




markov = generate_markov_sentences(text, 3)
phrase = generate_phrase(markov, 10, 3)
# print(markov[('going','plays')])
# print(markov)

print((' '.join(phrase).replace(' . ','. ')))
# print(markov[('honeymoons',)])


# print(markov[('the',)])