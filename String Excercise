EXERCISE 5

def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

This function is wrong. It doesn't put '' around the printed words
        
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

This function is the correct version of the function above. It takes a letter value from a string and tell you 'True' if it is lowercase and 'False' if it is an uppercase letter

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

This fucntion equates flag to the function that determines if a letter is lowercase. Then it returns the fucntion.

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

This function is wrong. It codes flag as palse but also as lowercase.

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

This fucntion returns 'True' unless the letter is lowercase. This was my favorite one.

EXERCISE 6

def rotate_word(word, n):
    result = ''
    for i in word:
        i = chr(ord(i) + n)
        result = result + i
    return (result)

word =input("Enter a string: ")
n = int(input("Enter rotate number: "))
print (Rotate_word(word,n))
