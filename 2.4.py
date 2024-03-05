def vowels_counter():
    word = input("Write a word: ")
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    counter = 0

    for letter in word:
        if letter in vowels:
            counter = counter + 1

    return counter

print("Number of vowels:", vowels_counter())