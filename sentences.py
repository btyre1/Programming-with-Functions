import random

def main():

    i = 0

    while i < 6:

        quantity = int(input("\nEnter the quantity (1 = single, any other int = plural): "))
        tense = input("\nEnter the tense (past, present, or future): ")
        final_sentence = make_sentence(quantity, tense)

        print(final_sentence)
        i += 1

    print("")

def make_sentence(quantity, tense):

    determiner = get_determiner(quantity).capitalize()
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase1 = get_prepositional_phrase(quantity)
    prepositional_phrase2 = get_prepositional_phrase(quantity)

    sentence = (f"\n{determiner} {noun} {verb} {prepositional_phrase1} {prepositional_phrase2}.")

    return sentence

def get_determiner(quantity):

    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):

    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    noun = random.choice(nouns)
    return noun


def get_verb(quantity, tense):

    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    
    if tense == "present" and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]

    if tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    
    verb = random.choice(verbs)
    return verb

def get_preposition():

    prepositions =["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    preposition = random.choice(prepositions)

    return preposition

def get_prepositional_phrase(quantity):

    d = get_determiner(quantity)
    p = get_preposition()
    n = get_noun(quantity)

    p_phrase = (f"{p} {d} {n}")

    return p_phrase

main()

