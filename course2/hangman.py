import random
words = ["python", "google", "words"]
stages = ["",
"________ ",
"| ",
"| | ",
"| 0 ",
"| /|\ ",
"| / \ ",
"| "
]
while True:
    word = words[random.randint(0, len(words) - 1)]
    current = "-" * len(word)
    lives = 5
    while lives > 0:
        guess = input("Guess a letter!\n")
        if (word.count(guess) > 0):
            print("Great!")
            for (id, value) in enumerate(word):
                if (value == guess):
                    new = list(current)
                    new[id] = value
                    current = ''.join(new)
        else:
            print("Wrong. You lose a life.\n")
            lives -= 1
        print(current)



