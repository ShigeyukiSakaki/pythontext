

def hangman(word):
    checkArr = ["_"] * len(word)
    wordArr = [c for c in word]
    wordIndicater = word

    mistake = 0
    while(mistake<7):
        c = input("estimate character: ")
        if c in word:
            index = wordArr.index(c)
            checkArr[index] = c
            print(" ".join(checkArr))
        mistake += 1

        if  "_" not in checkArr:
            print("you win!")
            break

    if mistake == 7:
        print("you lose! The answer is {}.".format(word))

hangman("dog")