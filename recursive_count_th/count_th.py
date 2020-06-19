'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    """
    function which counts the number of occurrences of substring 'th'
    in given string 'word'
    """
    # if the word is less than 2 letters it can't contain "th"
    if len(word) < 2:
        return 0
    # now we check word, starting with the first 2 letters
    # case "th" found: increase count by 1, recursively check next 2 letters in word
    if word[:2] == "th":
        return 1 + count_th(word[2:])
    # case "th" not found: don't increase count, recursively check next 2 letters in word
    # we include the 2nd letter in word since it could be 't'
    return count_th(word[1:])
    
    
# can't we just use .find() method?
# something like word.find("th")
# if word.find("th") doesnt find the substring, return 0
# otherwise if found, +1 to the count and recurse thru next letters