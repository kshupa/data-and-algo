phrase1 = "publi relations"
phrase2 = "crap built on lies"


def anagram_check(str1, str2):
    # strip of all spases
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # check if length is the same
    if len(str1) != len(str2):
        return "No anagram was found!"

    count = {}

    for letter in str1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in str2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return "No anagram was found!"
        else:
            return "This is an anagram!!!"


print(anagram_check(phrase1, phrase2))


# get 1st letter if in phrase2, pop it and go to next letter
