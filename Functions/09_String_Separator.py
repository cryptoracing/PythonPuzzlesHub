def separate_words(sentence):
    words = sentence.split()
    return words

def main():
    sentence = input("Sentence: ")
    separated_words = separate_words(sentence)
    print("Separated Words:", separated_words)

main()