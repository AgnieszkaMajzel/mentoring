def duplicate_letters():
    sentence = input("Write a sentence: ")
    words = sentence.split()

    for word in words:

        letters = set()

        for letter in word:
            if letter in letters:
                return True
            else:
                letters.add(letter)
    return False

print(duplicate_letters())