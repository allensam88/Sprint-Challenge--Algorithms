'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # Base condition: if no letters in the word, throw 0 and stop
    if len(word) == 0:
        return 0

    # check if first 2 letters are 'th'
    if word[0:2] == 'th':
        # if yes, add 1 to stack count, invoke function again, but with first 2 letters sliced off
        return 1 + count_th(word[2:])
    else:
        # if no, don't add anything to stack count, but trim off first letter in word
        return count_th(word[1:])
