

def isPureString(data):
    for i in data:
        if i.isdigit():
            return False
        elif i == ' ':
            return False
    return True

def reverseString(data):
    if isPureString(data):
        reversedStr = ''.join(reversed(data))
        return reversedStr
    return 'Uncorrect string! Try again...'
